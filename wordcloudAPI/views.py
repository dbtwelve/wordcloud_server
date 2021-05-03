from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from wordcloudAPI.forms import UploadForm, CommentForm
from wordcloudAPI.generator import generation
from wordcloudAPI.models import ImageUpload, Comment, WordCloud
from wordcloudAPI.serializer import ImageUploadSerializer, WordCloudSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ImageUploadSerializer
'''
class ImageViewSet(APIView):
    def get(self, request):
        serializer = ImageUploadSerializer(ImageUpload.objects.all(), many=True)
        return Response(serializer.data, status=201)
    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ImageViewSetDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(ImageUpload, pk=pk)

    def get(self, request, pk):
        img = self.get_object(pk)
        serializer = ImageUploadSerializer(img)
        return Response(serializer.data)
    def put(self, request, pk):
        img = self.get_object(pk)
        serializer = ImageUploadSerializer(img)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def delete(self,request, pk):
        img = self.get_object(pk)
        img.delete()
        return Response(status=204)
'''


def index(request):
    upload_list = ImageUpload.objects.all()
    return render(request, 'index.html', {
        'image_list': upload_list,
    })


def image_list(request):
    return render(request, 'list.html')


def image_detail(request, pk):
    img = ImageUpload.objects.get(pk=pk)
    return render(request, 'image_detail.html', {
        'image': img,
    })

def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = ImageUpload.objects.get(pk=pk)
            comment.save()
            return redirect(image_detail, pk)
    else:
        form = CommentForm()
    return render(request, 'post_form.html', {
        'form': form,
    })


def comment_edit(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = ImageUpload.objects.get(pk=post_pk)
            comment.save()
            return redirect(image_detail, post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'post_form.html', {
        'form': form,
    })


def comment_delete(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment.delete()
            return redirect(image_detail, post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'post_form.html', {
        'form': form,
    })


def upload_image(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.uid = request.user

            form.save()
            return redirect('image_list')
        else:
            form = UploadForm()
    return render(request, 'upload.html', {
        #'form': form
    })


class WordCloudViewSet(viewsets.ModelViewSet):
    queryset = WordCloud.objects.all()
    serializer_class = WordCloudSerializer
    def create(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.initial_data['imageURL'] = 'http://127.0.0.1:8000/media/' + generation(request.data)
        print(serializer)
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=200)
        else:
            print(serializer.errors)
            return Response(status=400)

    '''
    if request.method == 'POST':
        request = {
            'type': request.POST['s_type'],
            'textURL': request.POST['textURL'],
            'uid': request.POST['uid']
        }
    img = generation(request)
    data = []
    response = HttpResponse(minetype="image.png")
    img.save(response,"PNG")
    '''

