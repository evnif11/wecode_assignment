import json

from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from dog_owner.models import Owner, Dog

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)

        Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'message':'created'}, status=201)


class DogView(View):
    def post(self, request):
        data = json.loads(request.body)

        Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner = Owner.objects.get(id=data['owner_id'])
        )
        return JsonResponse({'message':'created'}, status=201)
