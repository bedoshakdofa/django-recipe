from django.urls import path
from django.views.generic import TemplateView
from . import views
urlpatterns = [
    path('home/',TemplateView.as_view(template_name='recipe/home.html'),name='home'),
    path('signup/',views.sign_views,name='signup'),
    path('login/',views.login_view,name='login'),
    path('search/',views.search_view,name="search"),
    path('logout/',views.logout_view,name='logout'),
    path('detial/',views.recipe_detial,name="detial"),
]

