from django.contrib import admin

# Register your models here.
from .models import Customer, Token
# Create your views here.
admin.site.register(Customer)
admin.site.register(Token)