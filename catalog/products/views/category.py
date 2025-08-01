from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from ..models import Category
from ..serializers import CategorySerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer