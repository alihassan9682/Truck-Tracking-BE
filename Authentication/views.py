from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,ProfileSerializer,LoginSerializer
from .models import Profile
import re
from django.contrib.auth import get_user_model
User = get_user_model()



class signuppage(APIView):
    def post(self, request):
        data = request.data
        print(data)
        if User.objects.filter(email=data.get('email')).exists():
            return Response({'message': 'This E-mail already exists'})
        
        if not data.get('password1') or not data.get('password2'):
            return Response({'message': 'Password is required'},status=404)
        
        if data.get('password1') != data.get('password2'):
            return Response({'message':'Password does not match'},status = 400)
        check_password = bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$', data.get('password1')))
        
        if check_password:
            data['password'] = data['password1']
            SerializerUser = UserSerializer(data=data)
            if SerializerUser.is_valid():
                user = SerializerUser.save()
                id = user.id
                data['user_id'] = id
                SerializerProfile = ProfileSerializer(data=data)
                if SerializerProfile.is_valid():
                    SerializerProfile.save()
                    return Response({'message': 'Profile created Successfully','id':id})
                else:
                    Person_exist = User.objects.get(id = id)
                    Person_exist.delete()
                    return Response(SerializerProfile.errors)
            else:
                return Response(SerializerUser.errors)
        else:
            return Response({'message':'Password should meet the following criteria:\n - Be at least 8 characters long (e.g., 12abAB!@)\n - Contain at least one lowercase letter (e.g., abcdef)\n- Contain at least one uppercase letter (e.g., ABCDEF)\n- Contain at least one number (e.g., 12345)\n- Contain at least one special character (e.g., !@#$%)'},status=400)

class loginpage(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            return Response({'message':'LogIn Successfull','user':UserSerializer(user).data['id']},status=200)
        else:
            return Response({'message': serializer.errors}, status=400)

class person_data(APIView):
    def post(self, request):
        data = request.data
        person_id = data['id']
        if person_id:
            try:
                profile = Profile.objects.get(user_id=person_id)
                serializer = ProfileSerializer(profile)
                return Response({'message': 'Profile fetched successfully', 'profile': serializer.data})
            except Profile.DoesNotExist:      
                return Response({'message':'Person does not exist'},status = 404)
        else:
            return Response({'message': 'id is required'}, status=400)
