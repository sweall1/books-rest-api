from .views import BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', BookViewSet)