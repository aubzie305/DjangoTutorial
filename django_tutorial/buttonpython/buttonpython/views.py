from django.shortcuts import render
import requests

def button(request):
    return render(request, 'home.html')

def first_output(request):
    first_data=requests.get("https://reqres.in/api/users")
    print(first_data.text)
    first_data=first_data.text
    return render(request, 'home.html', {'first_data':first_data})

def second_output(request):
    second_data='Heeyyy'
    print(second_data)
    return render(request, 'home.html', {'second_data': second_data})