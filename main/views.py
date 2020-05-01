from django.shortcuts import render,HttpResponse,redirect
from .models import BlogPost
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms


class NewPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['name','description','image']
        widgets = {
            'description': SummernoteWidget(),
        }
    def prepare_form(self):
        self.fields['name'].label = ''
        self.fields['image'].label = 'Загрузите изображение'
        self.fields['description'].label = ''
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название статьи'




def main_page(request):
    context = {}
    context['posts'] = BlogPost.objects.all().order_by('-date')[:10]
    context['last'] = context['posts'][:1][0]

    return render(
        request,
        'main/main_page.html',
        context,
    )

def new_post(request):
    context = {}
    form = NewPostForm
    if request.method == 'GET':
        form = form()
    if request.method == 'POST':
        form = form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    form.prepare_form()
    context['form'] = form
    return render(
        request,
        'main/new_post.html',
        context,
    )

# Create your views here.
