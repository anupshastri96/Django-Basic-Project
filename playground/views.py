from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request handler
#action
#request --> response
def calculate():
    x=1
    y=2
    return x


def say_hello(request):
#Pull data from db
#transform
#send email
    x=calculate()
    return render(request,'hello.html',{'name':'Mosh'})

