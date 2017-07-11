from django.conf.urls import url
from .backend_ajax import login_user, tweet, add_image_to_tweet, like_unlike, follow_un_follow, load_more_posts

urlpatterns = [
    url(r'^user/login/$', login_user),
    url(r'^user/tweet/$', tweet),
    url(r'^user/tweet/add_image$', add_image_to_tweet),
    url(r'^user/like_unlike$', like_unlike),
    url(r'^user/follow_un_follow$', follow_un_follow),
    url(r'^user/load_more_posts$', load_more_posts)
]
