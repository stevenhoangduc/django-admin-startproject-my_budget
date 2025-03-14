from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Expense
from django.http import HttpResponse
from django.utils import timezone
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from django.utils.dateformat import DateFormat


def about(request):
    return render(request, 'about.html')


@login_required(login_url='/login/')
def expenses(request):
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

    queryset = Expense.objects.filter(user=request.user)

    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    total_sum = sum(expense.price for expense in queryset)

   

    print("=== RAW CREATED_AT VALUES ===")
    for e in Expense.objects.filter(user=request.user).order_by('created_at'):
        print(f"{e.name} => {e.created_at}")
    print("==== END RAW DATES ====")

    print("=== ALL EXPENSES (NO USER FILTER) ===")
    
    for e in Expense.objects.all().order_by('created_at'):
        print(f"{e.user} | {e.name} => {e.created_at}")




    # Bar Chart Data
    monthly_totals = (
        Expense.objects.filter(user=request.user)
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(total=Sum('price'))
        .order_by('month')
    )

    chart_labels = [DateFormat(item['month']).format('F') for item in monthly_data]
    chart_expenses = [item['total_expenses'] for item in monthly_data]
    chart_salaries = [item['total_salary'] for item in monthly_data]



    print("==== DEBUG MONTHS ====")
    for item in monthly_totals:
        print("Month:", item['month'], "Total:", item['total'])


    chart_labels = [DateFormat(item['month']).format('F') for item in monthly_totals]
    chart_data = [item['total'] for item in monthly_totals]

    context = {
        'expenses': queryset,
        'total_sum': total_sum,
        'chart_labels': chart_labels,
        'chart_expenses': chart_expenses,
        'chart_salaries': chart_salaries,
}


    return render(request, 'expenses.html', context)


@login_required(login_url='/login/')
def update_expense(request, id):
    queryset = Expense.objects.get(id=id, user=request.user)

    if request.method == 'POST':
        data = request.POST
        queryset.name = data.get('name')
        queryset.price = float(data.get('price', 0))
        queryset.save()
        return redirect('/')

    context = {'expense': queryset}
    return render(request, 'update_expense.html', context)


@login_required(login_url='/login/')
def delete_expense(request, id):
    queryset = Expense.objects.get(id=id, user=request.user)
    queryset.delete()
    return redirect('/')


def login_page(request):
    if request.method == "POST":
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

    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is taken")
            return redirect('/register/')

        user_obj = User.objects.create(username=username)
        user_obj.set_password(password)
        user_obj.save()
        messages.success(request, "Account created")
        return redirect('/login')

    return render(request, "register.html")


def custom_logout(request):
    logout(request)
    return redirect('login')


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

    queryset = Expense.objects.filter(user=request.user)

    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains=request.GET.get('search'))

    total_sum = sum(expense.price for expense in queryset)
    username = request.user.username

    context = {
        'expenses': queryset,
        'total_sum': total_sum,
        'username': username,
    }

    return render(request, 'pdf.html', context)
