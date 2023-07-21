from rest_framework import generics, permissions
from .serializers import ArticleGetSerializer, ArticlePostSerializer, CategorySerializer, TagSerializer, \
    SubContentSerializer, SubContentImageSerializer, CommentSerializer, MineSubContentSerializer, \
    MineSubContentImageSerializer
from ..models import Article, Category, Tag, Comment, SubContent, SubContentImage
from .permissoin import IsAdminUserOrReadonly


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadonly]


class TagListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadonly]


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ArticlePostSerializer
        return ArticleGetSerializer

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     q = self.request.GETget('q')
    #     if q:
    #         qs = qs.filter(title__icontains=q)
    #     return qs


class BlogRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.order_by('-id')
    permission_classes = [IsAdminUserOrReadonly]
    lookup_field = "pk"

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ArticlePostSerializer
        return ArticleGetSerializer


class SubContentListCreateAPIView(generics.ListCreateAPIView):
    queryset = SubContent.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SubContentSerializer
        return MineSubContentSerializer


class SubContentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubContent.objects.all()
    serializer_class = SubContentSerializer
    permission_classes = [IsAdminUserOrReadonly]


class SubContentImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = SubContentImage.objects.all()
    serializer_class = SubContentImageSerializer


class SubContentImageRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubContentImage.objects.all()
    serializer_class = SubContentImageSerializer
    permission_classes = [IsAdminUserOrReadonly]


class CommentListCreateAPIView(generics.ListCreateAPIView):
    # http://127.0.0.1:8000/api/blog/article/{article_id}/comment-list-create/
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset()
    #     article_id = self.kwargs.get('article_id')
    #     if article_id:
    #         qs = qs.filter(article_id=article_id)
    #         return qs
    #     return []
    #
    # def get_serializer_context(self, *args, **kwargs):
    #     ctx = super().get_serializer_context()
    #     ctx['article_id'] = self.kwargs.get('article_id')
    #     return ctx
