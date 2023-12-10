from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, ProductReview
from .serializers import ProductSerializer, ProductReviewSerializer
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import AdminOrReadOnly, ReviewerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['price']
    

class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [ReviewerOrReadOnly]
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['rating'] #akhane jotogula iccha toto gula attribute diye filter kora jabe
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    
    
    # ai function ti o filter r jonno use kora hoi
    # def get_queryset(self):
    #     queryset = ProductReview.objects.all()
    #     username = self.request.query_params.get('username')
    #     if username is not None:     #user__username means=> review model a user foreign key hisebe ache, tai user r bitoror username k access korar jonno __ use kora hoi.
    #         queryset = queryset.filter(user__username__icontains=username)  # icontains use kora hoi jate small and capital letter hole problem na hoi
    #     return queryset
    
