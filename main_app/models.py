from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone # 6, see if you spend more or less.



# Create your models here.

# create a budget model for expenses
class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.IntegerField(default=0)
    name = models.CharField(max_length=100, default='something')
    price = models.FloatField(default=0.0)
    created_at = models.DateTimeField(default=timezone.now) # 6.

    







# # make a list of different categories where i spend my money, like food, rent, etc
# class Category(models.Model): # creating a category model, can save in database
#     name = models.CharField(max_length=50) # categoy name like food, rent, etc
#     # budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
# # these 2 lines are when someone ask what this category is, it will return its name
#     def __str__(self):
#         return self.name
    
# # write down each transaction, like how much i spent, what category, etc    
# class Transaction(models.Model):
#     TYPE_CHOICES = (
#         ('Income', 'Income'), # money coming in
#         ('Expense', 'Expense'), # money going out
#     )
# # transactions belongs to a user, if delete user, means delete all transactions
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
# # means which category does this transaction belongs to, grocery, rent, etc
# # if delete category, delete all transactions
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
# # how much money spent or earned
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
# # means was it income(you got money) or expense(you spent money)
#     type = models.CharField(max_length=10, choices=TYPE_CHOICES)
# # when did this transaction happen
#     date = models.DateField()
# # write a note about it like bought milk, or got salary
#     note = models.TextField(blank=True, null=True)
# # when someone ask what this transaction is, it will return its expense, $25, grocery
#     def __str__(self):
#         return f"{self.type} - {self.amount} - {self.category}"
# # line 17-37, every transaction will have a category, amount, type, date, note, so we know what it is
    
    
# class SubCategory(models.Model):
#     name = models.CharField(max_length=50)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    
    
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     address = models.TextField()
#     city = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     zip_code = models.CharField(max_length=10)
#     country = models.CharField(max_length=50)

#     def __str__(self):
#         return self.first_name + " " + self.last_name
    

# class Budget(models.Model):
#     name = models.CharField(max_length=100)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name
    


    
# class Income(models.Model):
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     budget = models.ForeignKey(Budget, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.description
    
# class IncomeCategory(models.Model):
#     income = models.ForeignKey(Income, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.category.name

    
# class ExpenseCategory(models.Model):
#     expense = models.ForeignKey(Expense, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.category.name


