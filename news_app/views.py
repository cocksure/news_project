from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News, Category, PublishedManager
from .forms import ContactForm


def news_list(request):
    news_list = News.objects.filter(status=News.Status.Published)
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)


def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)

    context = {
        "news": news
    }

    return render(request, "news/news_detail.html", context)

#bu homepage funksiyalisi#
def homePageView(request):
    categories = Category.objects.all()
    news_list = News.published.get_queryset().order_by('-publish_time')[:10]
    politic_news = News.published.all().filter(category__name="Политика").order_by('-publish_time')[1:5]
    context = {
        'news_list': news_list,
        'categories': categories,
        'politic_news': politic_news
    }

    return render(request, 'news/home.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.get_queryset().order_by('-publish_time')[:10]
        context['politic_news'] = News.published.all().filter(category__name="Политика").order_by('-publish_time')[:5]
        context['local_news'] = News.published.all().filter(category__name="Общество").order_by('-publish_time')[:5]
        context['sport_news'] = News.published.all().filter(category__name="Спорт").order_by('-publish_time')[:5]
        context['economic_news'] = News.published.all().filter(category__name="Экономика").order_by('-publish_time')[:5]
        context['internet_news'] = News.published.all().filter(category__name="Интернет").order_by('-publish_time')[:5]

        return context


# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Благодарим Вас за обращение к нам! ")
#
#     context = {
#         "form": form
#     }
#     return render(request, 'news/contact.html', context)


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
            return  HttpResponse('<h2> Благодарим Вас за обращение к нам!')
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)


class InternetNewsView(ListView):
    model = News
    template_name = 'news/internet.html'
    context_object_name = 'internet_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Интернет')
        return news


class LocalNewsView(ListView):
    model = News
    template_name = 'news/local.html'
    context_object_name = 'local_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Общество')
        return news


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Спорт')
        return news


class EconomicNewsView(ListView):
    model = News
    template_name = 'news/economic.html'
    context_object_name = 'economic_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Экономика')
        return news


class PoliticNewsView(ListView):
    model = News
    template_name = 'news/politic.html'
    context_object_name = 'politic_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Политика')
        return news


