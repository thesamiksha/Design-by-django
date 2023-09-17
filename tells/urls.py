from django.contrib import admin
from django.urls import path
from tells import views

urlpatterns = [
    path("",views.home,name = "home"),
    path("dailyneeds",views.dailyneeds,name = "dailyneeds"),
    path("electronics",views.electronics,name = "electronics"),
    path("lifestyle",views.lifestyle,name = "lifestyle"),
    path("mens",views.mens,name = "mens"),
    path("kiddo",views.kiddo,name = "kiddo"),
    path("womens",views.womens,name = "womens"),
    path("books",views.books,name = "books"),
    path("globals",views.globals,name = "globals"),
    path("RICE",views.RICE,name = "RICE"),
    path("contact",views.contact,name='contact'),
    path("ourstore",views.ourstore,name = "ourstore"),
    path("careers",views.careers,name = "careers"),
    path("FAQ",views.FAQ,name ="FAQ"),
    path("signin",views.signin,name = "signin"),
    path("signup",views.signup,name = "signup"),
    path("profile",views.profile,name = "profile"),
]
