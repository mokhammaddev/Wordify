from django.urls import path
from .views import BlogListCreateAPIView, BlogRUDAPIView, CategoryRUDAPIView, CategoryListCreateAPIView, \
 TagListCreateAPIView, TagRUDAPIView, SubContentImageListCreateAPIView, SubContentImageRUDAPIView, \
 SubContentRUDAPIView, SubContentListCreateAPIView, CommentListCreateAPIView

urlpatterns = [
    # CATEGORY
    path('list-create/category/', CategoryListCreateAPIView.as_view()),
    path('rud/category/<int:pk>/', CategoryRUDAPIView.as_view()),
    # TAG
    path('list-create/tag/', TagListCreateAPIView.as_view()),
    path('rud/tag/<int:pk>/', TagRUDAPIView.as_view()),
    # ARTICLE
    path('list-create/article/', BlogListCreateAPIView.as_view()),
    path('rud/article/<int:pk>/', BlogRUDAPIView.as_view()),
    # SUB-CONTENT
    path('list-create/sub-content/', SubContentListCreateAPIView.as_view()),
    path('rud/sub-content/<int:pk>/', SubContentRUDAPIView.as_view()),
    # SUB-CONTENT-IMAGE
    path('list-create/sub-content-image/', SubContentImageListCreateAPIView.as_view()),
    path('rud/sub-content-image/<int:pk>/', SubContentImageRUDAPIView.as_view()),
    # COMMENT
    path('article/<int:article_id>/comment-list-create/', CommentListCreateAPIView.as_view()),
]
