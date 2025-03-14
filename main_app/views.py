# Import necessary libraries
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User  # Import User model
from .models import Expense
from django.http import HttpResponse 
from django.shortcuts import render

from django.utils import timezone # 6, see if you spend more or less
from datetime import timedelta    # 6.


    # <!-- 6, see if you spend more or less  -->
@login_required(login_url='/login/')
def expenses(request):
    # Create a new expense (same as before)
    if request.method == 'POST':
        data = request.POST
        salary = float(data.get('salary', 0))
        name = data.get('name')
        price = float(data.get('price', 0))

        Expense.objects.create(
            user=request.user,
            salary=salary,
            name=name,
            price=price,
        )
        return redirect('/')

    # Filter by current and previous month
    now = timezone.now()
    start_of_month = now.replace(day=1)
    start_of_last_month = (start_of_month - timedelta(days=1)).replace(day=1)
    end_of_last_month = start_of_month - timedelta(days=1)

    this_month_expenses = Expense.objects.filter(user=request.user, created_at__gte=start_of_month)
    last_month_expenses = Expense.objects.filter(user=request.user, created_at__range=[start_of_last_month, end_of_last_month])

    total_this_month = sum(e.price for e in this_month_expenses)
    total_last_month = sum(e.price for e in last_month_expenses)

    comparison_message = ""
    if total_last_month:
        difference = total_this_month - total_last_month
        if difference > 0:
            comparison_message = f"You spent ${difference:.2f} more than last month."
        elif difference < 0:
            comparison_message = f"You saved ${abs(difference):.2f} compared to last month."
        else:
            comparison_message = "Your spending is exactly the same as last month."
    else:
        comparison_message = "No data from last month to compare."

    queryset = Expense.objects.filter(user=request.user)

    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    total_sum = sum(exp.price for exp in queryset)

    context = {
        'expenses': queryset,
        'total_sum': total_sum,
        'comparison_message': comparison_message,
    }
    return render(request, 'expenses.html', context)

    # <!-- 6, see if you spend more or less  ENDS HERE-->




def about(request):
    return render(request, 'about.html')

# Create Expense page
@login_required(login_url='/login/')
def expenses(request):
    salary = 0 
    if request.method == 'POST':
        data = request.POST
        salary = float(data.get('salary', 0)) # alows decimal
        name = data.get('name')
        price = float(data.get('price', 0)) # allows decimal

        Expense.objects.create(
            user=request.user,# this line will make the expenses loads when you added one
            salary=salary,
            name=name,
            price=price,
        )
        return redirect('/')
# this line will make it so only a user see their expenses after login in and out.
    queryset = Expense.objects.filter(user=request.user)

    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    # Calculate the total sum
    total_sum = sum(expense.price for expense in queryset)
    
    context = {
        'expenses': queryset, 
        'total_sum': total_sum
    }
    return render(request, 'expenses.html', context)


# Update the Expenses data
@login_required(login_url='/login/')
def update_expense(request, id):
    # this line also make it so only users gets to see their expenses after login in and out
    queryset = Expense.objects.get(id=id, user=request.user)


    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        price = float(data.get('price', 0))

        queryset.name = name
        queryset.price = price
        queryset.save()
        return redirect('/')

    context = {'expense': queryset}
    return render(request, 'update_expense.html', context)

# Delete the Expenses data
@login_required(login_url='/login/')
def delete_expense(request, id):
    # this line make it so only users get to see their expeses after login in and out
    queryset = Expense.objects.get(id=id, user=request.user)

    queryset.delete()
    return redirect('/')

# Login page for user
def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username).first()
            if not user_obj:
                messages.error(request, "Username not found")
                return redirect('/login/')
            user_auth = authenticate(username=username, password=password)
            if user_auth:
                login(request, user_auth)
                return redirect('expenses')
            messages.error(request, "Wrong Password")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    return render(request, "login.html")

# Register page for user
def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('/login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register')
    return render(request, "register.html")

# Logout function
def custom_logout(request):
    logout(request)
    return redirect('login')

# Generate the Bill
@login_required(login_url='/login/')
def pdf(request):
    if request.method == 'POST':
        data = request.POST
        salary = float(data.get('salary', 0))
        name = data.get('name')
        price = float(data.get('price', 0))

        Expense.objects.create(
            user=request.user,
            salary=salary,
            name=name,
            price=price,
        )
        return redirect('pdf')
# this line will set it so only users get to see their expenses after login in and out
    queryset = Expense.objects.filter(user=request.user)

    if request.GET.get('search'):
        queryset = queryset.filter(
            name__icontains=request.GET.get('search'))

    # Calculate the total sum
    total_sum = sum(expense.price for expense in queryset)
    # Get the username
    username = request.user.username

    context = {'expenses': queryset, 'total_sum': total_sum, 'username':username}
    return render(request, 'pdf.html', context)







        




# # Define the home view function
# def home(request):
#     # Send a simple HTML response
#     return HttpResponse('<h1>My Budget App</h1>')

# def about(request):
#     # django knows to look for about.html
#     # in the templates folder in our app
#     return render(request, 'about.html')
