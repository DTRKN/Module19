from django.urls import path
from .views import (GamesView, 
                    CartView, 
                    PlatformView,
                    sign_up_by_django,
                    sign_up_by_html)
app_name = "task1"

urlpattern_shop = [
    path('', PlatformView.as_view(), name='platform'),
    path('games/', GamesView.as_view(), name='games'),
    path('cart/', CartView.as_view(), name='cart'),
]

urlpattern_registration = [
    path('signup-django/', sign_up_by_django, name='signup_django'),
    path('signup-html/', sign_up_by_html, name='signup_html'),
]