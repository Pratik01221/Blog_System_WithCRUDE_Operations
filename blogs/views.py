from django.shortcuts import render
from .models import Blog, Category
from django.shortcuts import redirect

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
