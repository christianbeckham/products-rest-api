from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer
from products.models import Product

# Create your views here.


@api_view(['GET', 'POST'])
def reviews_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        # query_param to test retrieving all reviews by specific product
        # product_id_param = request.query_params.get('product_id')
        # if product_id_param:
        #     reviews = reviews.filter(product__id=product_id_param)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def product_reviews(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_reviews = Review.objects.select_related(
        'product').filter(product=product)
    serializer = ReviewSerializer(product_reviews, many=True)
    return Response(serializer.data)
