from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet, \
    FollowViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, 'Posts')
router.register(r'posts/(?P<id>[0-9]+)/comments', CommentViewSet, 'Post')
router.register('group', GroupViewSet, 'Group')
router.register('follow', FollowViewSet, 'Follow')
urlpatterns = [
    path('v1/', include(router.urls)),
]
