from django.shortcuts import render
from .tasks import add

# Create your views here.
def action(request):
    add.delay(2,2)