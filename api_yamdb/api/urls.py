from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    GenreViewSet,
    CommentViewSet,
    CategoryViewSet,
    TitleViewSet,
    ReviewViewSet,
    user_sign_up,
    TokenObtainView,
    UserViewSet,
)


router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet, basename='users')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('categories', CategoryViewSet, basename='categories')
router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='reviews'
)

router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments',
)

auth_urls = [
    path('auth/signup/', user_sign_up, name='sign_up'),
    path('auth/token/', TokenObtainView.as_view(), name='token_obtain'),
]

urlpatterns = [
    path('v1/', include(auth_urls)),
    path('v1/', include(router_v1.urls)),
]
