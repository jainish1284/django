from django.contrib import admin
from django.urls import path
from project.com.vo.SubCategoryVO import SubCategoryVO

urlpatterns = [
    path('', SubCategoryVO.adminLoadDashboard, name="adminLoadDashboard"),
    path('admin/loadDashboard/', SubCategoryVO.adminLoadDashboard, name="adminLoadDashboard"),
]
