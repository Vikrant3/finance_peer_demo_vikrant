from django.conf.urls import url
from . import views

app_name = 'demo_app'
urlpatterns = [
    url('register/', views.register_page, name="register"),
    url('login/', views.login_page, name="login"),
    url('retrieve/', views.retrieve_page, name="retrieve"),
]