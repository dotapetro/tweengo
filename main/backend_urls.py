from django.conf.urls import url
from .backend_ajax import login_user

urlpatterns = [
    url(r'^user/login/$', login_user)
]
