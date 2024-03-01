from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')


# Create your views here.
@login_required(login_url='/auth/login')
def projects(request):
    projects = ['Project1', 'Project2', 'Project3', 'Project4']
    description = ["NLP Based App for Stk1", "Project 2 Description", "Project3 is a trading platform", "Porject4 is a agent platform"]
    return render(request, 'projects.html', context={'projects': projects, 'description': description})

# Create your views here.
@login_required(login_url='/auth/login')
def agents(request):
    return render(request, 'agents.html')

# Create your views here.
@login_required(login_url='/auth/login')
def team(request):
    return render(request, 'team.html')

# Create your views here.
def test(request):
    return render(request, 'copy2.html')

