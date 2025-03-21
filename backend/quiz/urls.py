from django.urls import path
from .views import QuestionListCreateView, QuestionDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('questions/', QuestionListCreateView.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetailView.as_view(), name='question-detail'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
