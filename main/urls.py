from django.conf.urls import url
from .views import main_view

urlpatterns = [
    url(r'^$', main_view),
    url(r'^(?P<pages_user>\w+)/$', main_view)
]
