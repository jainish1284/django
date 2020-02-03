from django.contrib import admin
from django.urls import path
from project.com.vo.SubCategoryVO import SubCategoryVO

urlpatterns = [
    path('', SubCategoryVO.adminHome, name="adminhome"),
    # path('admin/', admin.site.urls),
]
