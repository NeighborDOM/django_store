from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': "DOM's Store",
        'is_promotion': True,
    }
    return render(request, 'products/index.html', context)


def products(request):
    return render(request, 'products/products.html')