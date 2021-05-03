from django import forms
from .models import ImageUpload, Comment

class UploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = '__all__'
        #field = {'title', 'uid', 'sourceType', 'source', 'wcImage', 'createDate', 'updateDate'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'message')


