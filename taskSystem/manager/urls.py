from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.ManagerList.as_view(), name="mhomepage"),
    path('mlist/', views.MReportList.as_view(), name="mReportList"),
    path('add/', views.MangerAdd.as_view(), name="addtask"),
    path('delete/<int:pk>', views.ManagerDelete.as_view(), name="deletetask"),
    path('update/<int:pk>', views.ManagerUpdate.as_view(), name="updatetask"),
    path('', views.Login.as_view(), name="login"),
    path('choose/', views.choose, name="choosing"),
    path('employee/', views.EmployeeList.as_view(), name="ehomepage"),
    path('eadd/', views.EmployeeAdd.as_view(), name="report"),
    path('rlist/', views.ReportList.as_view(), name="reportList"),
    path('deleter/<int:pk>', views.EmployeeDelete.as_view(), name="deletereport"),
    path('updater/<int:pk>', views.EmployeeUpdate.as_view(), name="updatereport"),
]
