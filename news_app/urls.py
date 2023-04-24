from django.urls import path
from .views import news_list, news_detail, ContactPageView, HomePageView, LocalNewsView, \
    PoliticNewsView, SportNewsView, InternetNewsView, EconomicNewsView, NewsDeleteView, NewsUpdateView, NewsCreateView, \
    admin_page_view, SearchResultView

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('contacts-us/', ContactPageView.as_view(), name='contact_page'),
    path('local-news/', LocalNewsView.as_view(), name='local_news_page'),
    path('politic-news/', PoliticNewsView.as_view(), name='politic_news_page'),
    path('sport-news/', SportNewsView.as_view(), name='sport_news_page'),
    path('internet-news/', InternetNewsView.as_view(), name='internet_news_page'),
    path('economic-news/', EconomicNewsView.as_view(), name='economic_news_page'),
    path('adminpage/', admin_page_view, name='admin_page'),
    path('searchresult/', SearchResultView.as_view(), name='search_results'),
]
