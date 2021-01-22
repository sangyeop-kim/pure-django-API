from django.http import JsonResponse

class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)
    
    def get_data(self, context):
        # fot transformation
        context['add'] = 'mixin test'
        return context