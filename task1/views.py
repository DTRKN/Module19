from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from django.views.generic import TemplateView
from .models import Buyer, Game

class GamesView(TemplateView):
    template_name = "fourth_task/games.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Game.objects.all()
        return context

class CartView(TemplateView):
    template_name = "fourth_task/cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = []
        return context


class PlatformView(TemplateView):
    template_name = "fourth_task/platform.html"

Game.objects.all().delete()
game1 = Game.objects.create(title="Game A", cost=100.00, size=1.5, description="An exciting RPG.", age_limited=True)
game2 = Game.objects.create(title="Game B", cost=50.00, size=0.8, description="A fun puzzle game.", age_limited=False)
game3 = Game.objects.create(title="Game C", cost=150.00, size=2.0, description="A challenging strategy game.", age_limited=True)


def sign_up_by_django(request):
    info = {'form': UserRegister()}
    
    if request.method == 'POST':
        form = UserRegister(request.POST)
    
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if (password == repeat_password 
                and age >= 18 
                and not Buyer.objects.filter(name=username, age=age).exists()):

                Buyer.objects.create(name=username, balance=0, age=age)
                
                return HttpResponse(f"Приветствуем, {username}!")
            else:
                return HttpResponse(f"НЕЕА, {username}!")
            
    return render(request, 'fifth_task/registration_page.html', info)

def sign_up_by_html(request):
    info = {}
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        if (password == repeat_password 
            and len(password) >= 8 
            and age >= 18  
            and not Buyer.objects.filter(name=username, age=age).exists()
            and len(username) <= 30):

            Buyer.objects.create(name=username, balance=0, age=age)
            
            return HttpResponse(f"Приветствуем, {username}!")
            
    return render(request, 'fifth_task/registration_page.html', info)

Buyer.objects.all().delete()
buyer1 = Buyer.objects.create(name="John", balance=500.00, age=25)
buyer2 = Buyer.objects.create(name="Mike", balance=300.00, age=17)
buyer3 = Buyer.objects.create(name="Alice", balance=700.00, age=30)
