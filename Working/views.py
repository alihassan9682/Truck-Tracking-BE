from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import DriverInfoSerializer,LocationInfoSerializer
from .models import LocationInfo, DriverInfo

class Driver(APIView):
    def post(self, request):
        data = request.data
        serializer = DriverInfoSerializer(data=data)
        if serializer.is_valid():
            data = serializer.save()
            return Response({'message':'Successfully uploaded','data':DriverInfoSerializer(data).data},status = 200)
        else:
            return Response({'message':serializer.errors},status=200)
    def get(self, request):
        id = request.GET.get('id','')
        if id:
            data = DriverInfo.objects.first()
            serializer = DriverInfoSerializer(data)
            return Response({'data':serializer.data},status=200)
        else:
            return Response({'message':'id is required'},status = 200)
    
class Locations(APIView):
    def post(self, request):
        data = request.data
        serializer = LocationInfoSerializer(data=data)
        if serializer.is_valid():
            data = serializer.save()
            return Response({'message':'Successfully uploaded','data':LocationInfoSerializer(data).data}, status = 200)
        else:
            return Response({'message':serializer.errors}, status=200)
    def get(self, request):
        id = request.GET.get('id','')
        if id:
            data = LocationInfo.objects.first()
            serializer = LocationInfoSerializer(data)
            return Response({'data':serializer.data},status=200)
        else:
            return Response({'message':serializer.errors}, status=200)

