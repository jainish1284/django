from django.http import HttpResponse, request
from project.com.dao.SubCategoryDAO import CategoryDAO
from django.shortcuts import render, redirect


class SubCategoryVO:

    def adminLoadDashboard(request):
        categorydao = CategoryDAO()
        print(categorydao)
        if request.method == 'GET':
            return render(request, "home.html", {'result': categorydao.searchCategory})
