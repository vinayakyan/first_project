from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def first_api(request):
    return Response(data={'message':"This is first api"})


@api_view(http_method_names=['POST', 'GET','PUT'])
def second_api(request):
    if request.method == 'POST':
        data = request.data
        print(data)
        return Response(data=data)
    if request.method =='PUT':
        data = request.data
        print(data)
        return Response(data=data)
    return Response(data={'detail': 'This is Get request of second Api'})
     