from django.contrib import admin
from .models import ImageUpload, Comment
# Register your models here.
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'createDate')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'createDate')

admin.site.register(ImageUpload, ImageUploadAdmin)
admin.site.register(Comment, CommentAdmin)
