from django.urls import path
from .views import  home
from .views import delete_log_message
from mainapp.models import LogMessage
from . import views
from .views import log_message
from .views import HomeListView


home_list_view = HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],
    context_object_name="message_list",
    template_name="yourappname/home.html",
)


urlpatterns = [
    path('', home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('log/', log_message, name='log_message'),
    path("log/", views.log_message, name="log"),
    path("", home_list_view, name="home"),
    path('delete_log_message/<int:log_id>/', delete_log_message, name='delete_log_message'),
    
]
