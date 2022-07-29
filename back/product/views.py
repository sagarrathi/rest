# Rest Framework
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Django related
from .models import Product
from .serializers import ProductSerializer
# from django.http import Http404
from django.shortcuts import get_object_or_404

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field  = 'pk

    def perform_create(self, serializer):
        # print(serializer.validated_data)  
        title= serializer.validated_data.get('title')
        content=serializer.validated_data.get('content') or None
        print("content is none")
        if content is None:
            content=title          
        serializer.save(content=content)

product_list_create_view=ProductListCreateAPIView.as_view()


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field  = 'pk

product_detail_view=ProductDetailAPIView.as_view()



class ProductListAPIView(generics.ListAPIView):
    """
    Not going to use this 
    because we will use list with create
    """
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    # lookup_field  = 'pk

product_list_view=ProductListAPIView.as_view()

@api_view(["GET","POST"])
def product_alt_view(request,pk=None,  *args, **kwargs):
    method=request.method
    if method=='GET':
        if pk is not None:
            # Detail
            queryset=Product.objects.filter(pk=pk)
            if not queryset.exist():
                raise Http404

            return Response()
       
        # list data 
        queryset=Product.objects.all()
        data=ProductSerializer(queryset, many=True).data
        return Response(data)
    if method=='POST':
        # make data
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): #Raise expection provides frindly error
            # serializer.save() this creates the instance
            # ehile .data does not
            print("serializer.data",serializer.data)
            return Response(serializer.data)
        else: 
            return Response({"message":"title cannot be empty "})
