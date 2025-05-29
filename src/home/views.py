from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'base.html')

def products(request):
    return render(request, 'home/products.html')

def products(request):
    context ={
        'products' : [
            {'name': 'apple watch',
             'price': 599.00,
             'description': 'aluminium case,starlight sport'},

             {'name': 'iphone 14',
              'price': 799.00,
              'description': '128gb storage 12gb ram'},

              {'name': 'airpods pro',
               'price': 78.00,
               'description':'active noise collection'}
        ]
    }
    return render(request, 'home/products.html', context)