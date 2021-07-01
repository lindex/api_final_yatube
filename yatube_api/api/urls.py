from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (PostViewSet, CommentViewSet, GroupViewSet,
                    FollowViewSet)

router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, 'Posts')
router_v1.register(r'posts/(?P<id>[0-9]+)/comments', CommentViewSet, 'Post')
router_v1.register('group', GroupViewSet, 'Group')
router_v1.register('follow', FollowViewSet, 'Follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path(
        'v1/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'v1/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'v1/redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
