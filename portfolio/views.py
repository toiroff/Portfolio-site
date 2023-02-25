from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def home(request):
    service = Service.objects.all()[0:4]
    blogs = Blog.objects.all()
    team = OurTeam.objects.all()
    clients = Client.objects.all()
    my = MyProject.objects.all()
    context = {'service':service,'blogs':blogs,'team':team,'client':clients,'projects':my}
    return render(request,'base/index.html',context)


def About(request):
    service = Service.objects.all()[0:2]
    clients = Client.objects.all()
    my = MyProject.objects.all()
    team = OurTeam.objects.all()
    context = {'service':service,'client':clients,'projects':my,'team':team}
    return render(request, 'base/about.html', context)


def blog(request):
    blog = Blog.objects.all()
    context = {'blog':blog}
    return render(request, 'base/blog.html', context)

def BlogDetails(malumot,pk):
    blog = Blog.objects.get(id=pk)
    blogs = Blog.objects.all()[0:3]

    comments = blog.comment_set.all()
    if malumot.method== 'POST':
        Comment.objects.create(
            name=malumot.POST.get('name'),
            blog=blog,
            comment= malumot.POST.get('comment')
        )

        return redirect('blog-details',pk=blog.id)
    context = {'blog':blog,'blogs':blogs,'comments':comments}
    return render(malumot,'base/blog-details.html',context)


def portfolio(malumot):

    model =Portfolio.objects.all()
    topic = Topic.objects.all()
    context = {'portfolio':model,'topic':topic}
    return render(malumot, 'base/portfolio.html', context)

def Services(request):
    model = Service.objects.all()
    sponsor = Sponsor.objects.all()
    context = {'service':model,'sponsor':sponsor}
    return render(request, 'base/services.html', context)

def contact(malumot):
    if malumot.method == 'POST':
        message = Contact.objects.create(
            name=malumot.POST.get('name'),
            email=malumot.POST.get('email'),
            website=malumot.POST.get('website'),
            text=malumot.POST.get('text')
        )
        return redirect('contact')


    context = {}
    return render(malumot, 'base/contact.html', context)