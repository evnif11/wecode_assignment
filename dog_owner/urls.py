from django.urls import path
from dog_owner.views import OwnerView, DogView

urlpatterns = [
    path('owner', OwnerView.as_view()),
    path('dog', DogView.as_view()),
]
