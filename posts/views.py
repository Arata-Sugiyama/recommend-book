from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import InquiryForm, PostCreateForm
from django.urls import reverse_lazy
from django.contrib import messages
import logging

from .models import Post

# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class PenguinView(generic.TemplateView):
    template_name = "penguin.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy("posts:inquiry")

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class PostListView(LoginRequiredMixin, generic.ListView):
    model = Post
    template_name = 'post_list.html'
    paginate_by = 2

    def get_queryset(self):
        posts = Post.objects.order_by('-created_at')
        return posts

class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('posts:post_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        messages.success(self.request, '投稿を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "投稿の作成に失敗しました。")
        return super().form_invalid(form)

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = PostCreateForm

    def get_success_url(self):
        return reverse_lazy('posts:post_detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, '投稿を更新しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "投稿の更新に失敗しました。")
        return super().form_invalid(form)

class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:post_list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "投稿を削除しました。")
        return super().delete(request, *args, **kwargs)


