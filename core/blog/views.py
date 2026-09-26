from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView, ListView ,DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Post
from .forms import PostForm


# Create your views here.
# def indexView(request):
#     '''
#     A function based view to show index page
#     '''
#     name = "Mohammad"
#     context = {"name":name}
#     return render(request, 'index.html', context)


class IndexView(TemplateView):
    '''
        A class based view to show index page
        '''
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Mohammad'
        context['posts'] = Post.objects.all()
        return context


# class RedirectToMaktab(RedirectView):
#     url = 'https://maktabkhooneh.com'

#     def get_redirect_url(self, *args, **kwargs):
#         posts = get_object_or_404(Post, pk=kwargs["pk"])
#         print(posts)
#         return super().get_redirect_url(*args, **kwargs)


class PostListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    permission_required = 'blog.view_post'
    model = Post
    context_object_name = 'posts'
    ordering = '-id'

    # def get_queryset(self):
    #     posts = Post.objects.filter(status=True)
    #     return posts
    

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

'''
class PostCreateView(FormView):
    template_name = 'contact.html'
    form_class = PostForm
    success_url = '/blog/post'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
'''

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # fields = ['author', 'title', 'content', 'status', 'category', 'published_date']
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/blog/post/'