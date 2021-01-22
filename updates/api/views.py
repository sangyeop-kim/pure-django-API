from ..models import UpdateModel
from django.http import HttpResponse
from django.views.generic import View
'''
model에서 serialize 진행했음!
class의 method를 분리해서 class로 정의하면 해석에 편의성은 있지만 추천하는 방식은 아님
ex) class UpdataModelChangeAPIView():
    def put(self, request, *args, **kwargs):
        return #json
'''
class UpdateModelDetailAPIView(View):
    '''
    Retrieve, Update, Delete --> Object related stuff
    '''
    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')
    
    
    def put(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')
    
    def delete(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')
    
    
    
class UpdateModelListAPIView(View):
    '''
    List View
    Create View
    '''
    def get(self, request, *args, **kwargs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data, content_type='application/json')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse({}, content_type='application/json')