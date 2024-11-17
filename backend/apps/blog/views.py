from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .models import BlogTree
from .serializers import BlogTreeSerializer


class BlogTreeListView(ListAPIView):
    queryset = BlogTree.objects.all()
    serializer_class = BlogTreeSerializer


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog_tree(request: Request):
    serialized = BlogTreeSerializer(data=request.data, context={"user": request.user})
    if serialized.is_valid():
        serialized.save()
        return Response({"data": serialized.data}, status=201)

    return Response({"error": "invalid data"}, status=400)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog_node(request: Request):
    
    return Response({"test": "test"})
