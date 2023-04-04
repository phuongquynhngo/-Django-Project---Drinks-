from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])

def drink_list(request):

    # GET request function
    if request.method == 'GET': 
    # get all the drinks
    # serialize them
    # return json
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        #return JsonResponse( serializer.data, safe =False)
        return JsonResponse({'drinks': serializer.data})
    
    if request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id ):

    #pk: primary key
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    #get specific drink by id
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    #updating data
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    #delete data
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)