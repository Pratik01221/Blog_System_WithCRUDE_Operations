from django.shortcuts import get_object_or_404, render
from .models import Blog, Category
from django.shortcuts import redirect
from django.db.models import Q

def posts_by_category(request, category_id):
# ferch posts based on category_id
    posts = Blog.objects.filter(status='Published',Category__id=category_id)
# use try except when we wants to do some custome actions if object not found
    try:
        category = Category.objects.get(id=category_id)
    except:
    # redirect to some other page if category not found
        return redirect('404.html')
    
    # user get_object_or_404 to fetch object or return 404 error if not found
    # category = get_object_or_404(Category, id=category_id)

    context = {'posts': posts,'category': category,}

    return render(request, 'posts_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {'single_blog': single_blog,}
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')

    blogs = Blog.objects.filter( Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published') 
    context = {'blogs': blogs, 'keyword': keyword}  
    return render(request, 'search.html', context)
