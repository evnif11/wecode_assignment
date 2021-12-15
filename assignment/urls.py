from django.urls import path, include

urlpatterns = [
    path('', include('dog_owner.urls')),
    path('', include('movies.urls')),
]
