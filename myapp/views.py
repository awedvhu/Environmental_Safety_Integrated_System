from django.shortcuts import render
from myapp.models import User
from myapp.serializers import UserSerializer
from rest_framework import viewsets


# Create your views here.
def homepage(request):
    return render(request, "homePage.html", locals())


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
