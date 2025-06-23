from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('signup',views.signup,name="signup"),
    path('expenses',views.Expenses_list,name="Expenses_list"),
    path('Create_expenses',views.Create_expenses,name="Create_expenses"),
    path('delete/<int:id>/',views.delete, name="delete"),
    path('filter_expenses',views.filter_expenses, name="filter_expenses"),
    path('expenses_history',views.filtered_expenses, name="filtered_expenses"),
    # path('admin/',admin.site.urls),
]

