from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, mixins
from .serializers import TravelSerializer, MehmonhonaSerializer, KlassSerializer
from .models import Travel, Mehmonhona, Klass

def index(request):
    response_content = '''
    <h1>TRAVEL LINK : <a href="http://127.0.0.1:8000/api/v1/travel/">127.0.0.1:8000/api/v1/travel/</a></h1>
    <h1>HOTEL LINK : <a href="http://127.0.0.1:8000/api/v2/mehmonhona/">127.0.0.1:8000/api/v2/mehmonhona/</a></h1>
    <h1>CLASS LINK : <a href="http://127.0.0.1:8000/api/v3/class/">127.0.0.1:8000/api/v3/class/</a></h1>
    '''
    return HttpResponse(response_content)

class TravelView(mixins.ListModelMixin, 
                 mixins.CreateModelMixin, 
                 mixins.RetrieveModelMixin, 
                 mixins.UpdateModelMixin, 
                 mixins.DestroyModelMixin, 
                 generics.GenericAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class KlassView(mixins.ListModelMixin, 
                mixins.CreateModelMixin, 
                mixins.RetrieveModelMixin, 
                mixins.UpdateModelMixin, 
                mixins.DestroyModelMixin, 
                generics.GenericAPIView):
    queryset = Klass.objects.all()
    serializer_class = KlassSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class MehmonhonaView(mixins.ListModelMixin, 
                     mixins.CreateModelMixin, 
                     mixins.RetrieveModelMixin, 
                     mixins.UpdateModelMixin, 
                     mixins.DestroyModelMixin, 
                     generics.GenericAPIView):
    queryset = Mehmonhona.objects.all()
    serializer_class = MehmonhonaSerializer

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
