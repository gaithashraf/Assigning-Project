from django.shortcuts import render
from django.views.generic import CreateView,DeleteView,UpdateView,ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Task, Report
from .forms import TaskForm, ReportForm

class Login(LoginView):
    template_name = "login.html"
    success_url =reverse_lazy("choosing")

class EmployeeList(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "ePage.html"

class ReportList(ListView):
    model = Report
    context_object_name = "report"
    template_name = "listReport.html"

class EmployeeAdd(CreateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy("reportList")
    template_name = "employeeReport.html"

class EmployeeDelete(DeleteView):
    model = Report
    success_url = reverse_lazy("ehomepage")
    def get(self,request,*args,**kwargs):
        return self.delete(request,*args, **kwargs)

class EmployeeUpdate(UpdateView):
    model = Report
    form_class = ReportForm
    success_url = reverse_lazy("reportList")
    template_name = "employeeReport.html"

class ManagerList(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "mainPage.html"

class MReportList(ListView):
    model = Report
    context_object_name = "report"
    template_name = "managerList.html"

class MangerAdd(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("mhomepage")
    template_name = "taskPage.html"

class ManagerDelete(DeleteView):
    model = Task
    success_url = reverse_lazy("mhomepage")
    def get(self,request,*args,**kwargs):
        return self.delete(request,*args, **kwargs)

class ManagerUpdate(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("mhomepage")
    template_name = "taskPage.html"

def choose(request):
    return render(request,"choosing.html")
