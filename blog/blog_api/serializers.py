from ..models import Category, Tag, SubContent, SubContentImage, Comment, Article
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class ArticlePostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'category', 'category_name', 'view', 'tags', 'image', 'description', 'created_date']

    # def create(self, validated_data):
    #     instance = super().create(validated_data)
    #     instance.save()
    #     return instance


class MineSubContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContentImage
        fields = ['id', 'image', 'is_wide']


class MineSubContentSerializer(serializers.ModelSerializer):
    sub_image = MineSubContentImageSerializer(read_only=True, many=True)

    class Meta:
        model = SubContent
        fields = ['id', 'content', 'article', 'sub_image']


class ArticleGetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    sub_content = MineSubContentSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'category', 'tags', 'view', 'image', 'description', 'sub_content', 'created_date']


class SubContentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContentImage
        fields = ['id', 'sub_content', 'image', 'is_wide']


class SubContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubContent
        fields = ['id', 'content', 'article']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'article', 'description', 'created_date']
        extra_kwargs = {
            "article": {"required": False}
        }

    # def create(self, validated_data):
    #     request = self.context['request']
    #     article_id = self.context['article_id']
    #     author_id = request.user.profile.id
    #     description = validated_data.get('description')
    #     instance = Comment.objects.create(article_id=article_id, author_id=author_id, description=description)
    #     return instance

