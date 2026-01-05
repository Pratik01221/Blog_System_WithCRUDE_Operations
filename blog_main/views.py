from django.shortcuts import render
from blogs.models import Category,Blog
from Core_features.models import About  
from .forms import UserRegisterForm


def home(request):
   
    featured_posts = Blog.objects.filter(is_featured=True,status='Published' ).order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published') 
    
    # featch about us
    try:
        about= About.objects.get()
    except:
        about = None   

    context = {
        
        'featured_posts' : featured_posts,
        'posts':posts, 
        'about': about ,

    }
    return render(request,'home.html',context)

def register(request):
    form = UserRegisterForm()
    context = {'form': form}

    return render(request, 'register.html', context)