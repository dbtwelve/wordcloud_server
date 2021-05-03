from wordcloudAPI.models import ImageUpload, Comment, WordCloud
from rest_framework.serializers import ModelSerializer

class ImageUploadSerializer(ModelSerializer):
    class Meta:
        model = ImageUpload
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class WordCloudSerializer(ModelSerializer):
    class Meta:
        model = WordCloud
        fields = ('uid', 'sourceType', 'source', 'imageURL')