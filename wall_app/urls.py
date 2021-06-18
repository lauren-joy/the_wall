from django.urls import path
from . import views
#  ******URLS.PY IS THE ONLY PLACE WHERE INITAL / IS NOT NEEDED******
urlpatterns = [
    path('home', views.home), #localhost:8000/wall/home
    path('flush', views.flush), #localhost:8000/wall/flush
    path('message', views.message), #localhost:8000/wall/message
    path('comment/<int:message_id>', views.comment), #localhost:8000/wall/int/comment
    path('delete/<int:message_id>', views.delete), #localhost:8000/wall/delete
]