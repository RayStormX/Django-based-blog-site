from django.urls import path
from . import views
<<<<<<< HEAD

=======
>>>>>>> master
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('privacypolicy/', views.privacyPolicy, name='blog-privacyPolicy'),

]