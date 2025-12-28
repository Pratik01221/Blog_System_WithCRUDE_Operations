from .models import Category
from Core_features.models import Sociallinks

def get_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}


def get_sociallinks(request):
     
    sociallinks = Sociallinks.objects.all()
    return dict(sociallinks=sociallinks)