from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.forms import models as model_forms
from .models import Post, Category
from .forms import PostForm, ContactForm
from django.views.generic import ListView, CreateView, UpdateView, \
    DetailView, DeleteView, TemplateView


class PostListView(ListView):
    model = Post
    template_name = 'mainapp/home.html'
    ordering = ['-created_at']
    paginate_by = 7

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Home'
        return context

    def get_queryset(self):
        # print(self.kwargs)
        if 'cat_id' in self.kwargs:
            return Post.objects.filter(
                category__in=[
                    self.kwargs['cat_id']],
                is_active=True).order_by('-updated_at')
        else:
            return Post.objects.filter(is_active=True).order_by('-updated_at')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'mainapp/post_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Detail Views'
        return context


class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/success/'
    template_name = 'mainapp/post_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Create New Post'
        return context

    def post(self, request, *args, **kwargs):
        post = Post.objects.create(user=self.request.user,
                                   title=self.request.POST['title'],
                                   description=self.request.POST[
                                       'description'])
        post.save()
        for _ in dict(self.request.POST)['category']:
            category = int(_)
            # print(f'категория из реквеста ---> {category}')

            category_obj = Category.objects.get(pk=category)
            # print(f'объект категории ---> {category_obj}')

            post.category.add(category_obj)
            # print(f'пост.категория ---> {post.category}')

        self.object = None
        # return super().get(request, *args, **kwargs)
        return HttpResponseRedirect('/success/')


class PostSuccessMessageView(TemplateView):
    template_name = 'mainapp/success_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Success'
        return context


class PostDashboardView(ListView):
    model = Post
    context_object_name = 'total_post'
    ordering = ['-created_at']
    paginate_by = 10
    template_name = 'mainapp/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Dashboard'
        return context


class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/success/'
    template_name = 'mainapp/update_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Update'
        return context


class Contact(CreateView):
    form_class = ContactForm
    success_url = '/success/'
    template_name = 'mainapp/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Blog | Contact'
        return context


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/dashboard/'
    template_name = 'mainapp/post_delete.html'


class HelpView(TemplateView):
    """Страница помощь"""
    template_name = 'mainapp/help_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Помощь'
        return context
