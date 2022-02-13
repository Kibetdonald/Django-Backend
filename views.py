from delegates import serialize
from delegates.models import Delegates
from delegates.serialize import DelegatesSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class DelegatesTable(APIView):
    def get(self,request):
        delegatesObj=Delegates.objects.all()
        dlSerializeObj=DelegatesSerializer(delegatesObj,many=True)
        return Response(dlSerializeObj.data)
    
    def post(self,request):
        serializeobj=DelegatesSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)

class DelegatesUpdate(APIView):
    def post(self,request,pk):
        try:
            delegatesObj=Delegates.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")

        serializeobj=DelegatesSerializer(delegatesObj,data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors)


class DelegatesDelete(APIView):
    def post(self,request,pk):
        try:
            delegatesObj=Delegates.objects.get(pk=pk)
        except:
            return Response("Not Found in Database")
        delegatesObj.delete()
        return Response(200)