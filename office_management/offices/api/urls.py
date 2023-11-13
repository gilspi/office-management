from django.urls import include, path
from rest_framework import routers
from .views import OfficeViewSet, RoomAPIView, EmployeeAPIView


router = routers.DefaultRouter()
router.register(r'offices', OfficeViewSet, basename='offices')
# router.register(r'rooms', RoomViewSet)
# router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', OfficeViewSets.as_view({'get': 'list'})),
    # path('<int:pk>/', OfficeViewSets.as_view({'put': 'update'})),
    # path('employees/', EmployeeAPIView.as_view()),
    # path('rooms/', RoomAPIView.as_view()),
    # path('rooms/<int:id>/', RoomAPIView.as_view()),
]
