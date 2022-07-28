from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    # path("home/", views.homepage, name='homepage'),
    path('<str:name>', views.index_name, name="Index_Name")
]