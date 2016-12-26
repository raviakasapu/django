from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template import loader

#using a function based view
# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('I am called from a GET Request')
#     elif request.method == 'POST':
#         return HttpResponse('I am called from a POST Request')

#using a class based view
class Index(View):
    def get(self,request):
        params = {}
        params['name']="Ravi Django"
        return render(request, 'base.html',params)

