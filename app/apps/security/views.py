```python
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"message": "Logged in successfully"}, status=status.HTTP_200_OK)
    else:
        return Response({"message": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@login_required
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

@login_required
@api_view(['GET'])
def user_details(request):
    return JsonResponse({
        'username': request.user.username,
    })
```