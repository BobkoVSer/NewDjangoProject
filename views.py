from django.shortcuts import render



# Create your views here.
def shop(request):
    return render(request, 'forth_task/shop.html')

def games(request):
    return render(request, 'forth_task/games.html')

def basket(request):
    return render(request, 'forth_task/basket.html')
# Create your views here.
