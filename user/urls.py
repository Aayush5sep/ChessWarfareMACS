from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('loginpage/',views.loginpage),
    path('login/',views.loginuser),
    path('newaccnt/',views.signupuser),
    path('newaccntpage/',views.signuppage),
    path('logout',views.logoutuser),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
