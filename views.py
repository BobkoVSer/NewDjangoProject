from django.shortcuts import render

def shop(request):
        return render(request, 'shop.html')


def games(request):
    return render(request, 'games.html')

def basket(request):
    return render(request, 'basket.html')

# Create your views here.
