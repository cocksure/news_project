from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from hitcount.utils import get_hitcount_model
from news_project.custom_permissions import OnlyLoggedSuperUser
from .models import News, Category, Comment
from .forms import ContactForm, CommentForm, NewsForm, NewsUpdateForm
from hitcount.views import HitCountMixin
from django.contrib import messages


def news_list(request):
    newslist = News.objects.filter(status=News.Status.Published)
    context = {
        "news_list": newslist
    }
    return render(request, "news/news_list.html", context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {}
    # hitcount logika
    hit_count = get_hitcount_model().objects.get_for_object(news)
    comments = news.comments.filter(active=True)
    hits = hit_count.hits
    hitcontext = context['hitcount'] = {'pk': hit_count.pk}
    hit_count_response = HitCountMixin.hit_count(request, hit_count)
    if hit_count_response.hit_counted:
        hits = hits + 1
        hitcontext['hit_count'] = hit_count_response.hit_counted
        hitcontext['hit_message'] = hit_count_response.hit_message
        hitcontext['total_hits'] = hits

    comments = news.comments.filter(active=True)
    comment_count = comments.count()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # yengi comment obyekt yaratadi lekin databasega save qimidi
            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            # comment egasini request yuvorvotgan odamga boglab qoyish
            new_comment.user = request.user
            # endi databasega save qilish
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    context = {
        "news": news,
        'comments': comments,
        'comment_count': comment_count,
        'new_comment': new_comment,
        'comment_form': comment_form
    }

    return render(request, "news/news_detail.html", context)


class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.get_queryset().order_by('-publish_time')[:10]
        context['politic_news'] = News.published.all().filter(category__id=1).order_by('-publish_time')[:5]
        context['local_news'] = News.published.all().filter(category__id=3).order_by('-publish_time')[:5]
        context['sport_news'] = News.published.all().filter(category__id=2).order_by('-publish_time')[:5]
        context['economic_news'] = News.published.all().filter(category__id=4).order_by('-publish_time')[:5]
        context['internet_news'] = News.published.all().filter(category__id=5).order_by('-publish_time')[:5]

        return context


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            messages.success(request, 'Сообщение успешно отправлено!')
            return render(request, 'news/contact.html')
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)


class InternetNewsView(ListView):
    model = News
    template_name = 'news/internet.html'
    context_object_name = 'internet_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__id=5)
        return news


class LocalNewsView(ListView):
    model = News
    template_name = 'news/local.html'
    context_object_name = 'local_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__id=3)
        print(news)
        return news


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__id=2)
        return news


class EconomicNewsView(ListView):
    model = News
    template_name = 'news/economic.html'
    context_object_name = 'economic_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__id=4)
        return news


class PoliticNewsView(ListView):
    model = News
    template_name = 'news/politic.html'
    context_object_name = 'politic_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__id=1)
        return news


class NewsUpdateView(OnlyLoggedSuperUser, UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'crud/news_edit.html'


class NewsDeleteView(OnlyLoggedSuperUser, DeleteView):
    model = News
    template_name = 'crud/news_delete.html'
    success_url = reverse_lazy('home_page')


class NewsCreateView(OnlyLoggedSuperUser, CreateView):
    model = News
    form_class = NewsForm
    template_name = 'crud/news_create.html'

    success_url = reverse_lazy('home_page')


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def admin_page_view(request):
    admin_users = User.objects.filter(is_superuser=True)

    context = {
        'admin_users': admin_users
    }

    return render(request, 'pages/admin_page.html', context)


class SearchResultView(ListView):
    model = News
    template_name = "news/search_result.html"
    context_object_name = 'Все_новости'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)

        )
