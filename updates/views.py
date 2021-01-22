from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.
# def detail_view(request):
#     return render() # return JSON data or XML, JSON = JS object notation

'''
return render(request, template, {}) <- return HttpResponse(get_template().render({}))
'''



# function view

def json_example_view(request):
    '''
    URI for a rest API
    GET - Retrieve
    
    # 원래는 아래의 코드처럼 json을 직접 만들어줬어야 함!!
    import json
    def update_model_detail_view(request):
        data = {
            "count": 1000,
            "content": "some new content"
        }
        json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
    '''
    data = {
        "count": 1000,
        "content": "example some new content"
    }
    return JsonResponse(data)




# class based view
from django.views.generic import View
from lecture_django_api.mixins import JsonResponseMixin

class JsonCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "1 some new content"
        }
        return JsonResponse(data)
    
    

        
        
class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 3000,
            "content": "some new content"
        }
        
        return self.render_to_json_response(data)
    
    
    
    
# serialize
from .models import UpdateModel
import json
from django.core.serializers import serialize

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = UpdateModel.objects.get(id=6) # pk 기준
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')
        # return JsonResponse(data) <-- data type == 'dict'
    
class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        json_data = UpdateModel.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')