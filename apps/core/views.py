from django.shortcuts import render
from apps.store.models import Product

def frontpage(request):
    products = Product.objects.all() #Product pour récupérer tous les objets (produits) de la base de données.
    context = {
        'products':products
    }
    return render(request, 'frontpage.html', context)

def contact(request):
    return render(request, 'contact.html')