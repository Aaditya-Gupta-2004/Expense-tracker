from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import Exp, Signup
from datetime import datetime
from django.db.models import Sum  
from django.contrib.auth.decorators import login_required

# Home page that requires login
@login_required
def index(request):
    return render(request, 'index.html')

# Login view
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Logout view
def logoutUser(request):
    logout(request)
    return redirect("/login")

# Sign-up view
def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists.'})
        
        user2 = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password)
        user2.save()
        return redirect('/login')
    return render(request, 'signup.html')
 

# View to list expenses for the logged-in user
@login_required
def Expenses_list(request):
    expenses = Exp.objects.filter(user=request.user).order_by('-id')
    return render(request, 'expenses.html', {'Expense': expenses})

# Create expenses for the logged-in user
@login_required
def Create_expenses(request):     
    if request.method == "POST":    
        title = request.POST.get('title')
        amount = request.POST.get('amount')
        expense_type = request.POST.get('type')
        category = request.POST.get('category')
        date = datetime.today()
        
        expense = Exp.objects.filter(user=request.user, Title=title, Amount=amount, Type=expense_type, Category=category, date=date).first()
        if not expense:
            expense = Exp(user=request.user, Title=title, Amount=amount, Type=expense_type, Category=category, date=date)
            expense.save()
    return redirect('Expenses_list')

# Delete an expense for the logged-in user
@login_required
def delete(request, id):
    expense = Exp.objects.filter(id=id, user=request.user).first()
    if expense:
        expense.delete()
    return redirect('Expenses_list')

# Filtered expenses for the logged-in user
@login_required
def filtered_expenses(request):
    expenses = Exp.objects.filter(user=request.user).order_by('-date')
    return render(request, 'expenses_history.html', {'Expense': expenses})

# Filter expenses with date range and category/type filters for the logged-in user
@login_required
def filter_expenses(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    expense_type = request.GET.get('type')
    category = request.GET.get('category')

    filtered_expenses = Exp.objects.filter(user=request.user)

    if start_date:
        filtered_expenses = filtered_expenses.filter(date__gte=start_date)
    if end_date:
        filtered_expenses = filtered_expenses.filter(date__lte=end_date)
    if expense_type:
        filtered_expenses = filtered_expenses.filter(Type=expense_type)
    if category:
        filtered_expenses = filtered_expenses.filter(Category=category)

    total_expenses = filtered_expenses.filter(Type="expense").aggregate(Sum('Amount'))['Amount__sum'] or 0
    total_credits = filtered_expenses.filter(Type="credit").aggregate(Sum('Amount'))['Amount__sum'] or 0

    context = {
        'filtered_expenses': filtered_expenses,
        'total_expenses': total_expenses,
        'total_credits': total_credits,
    }

    return render(request, 'expenses_history.html', context)
