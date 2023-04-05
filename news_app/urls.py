from django.urls import path
from .views import news_list, news_detail, homePageView, ContactPageView, HomePageView, LocalNewsView, \
    PoliticNewsView, SportNewsView, InternetNewsView, EconomicNewsView


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('contacts-us/', ContactPageView.as_view(), name='contact_page'),
    path('local-news/', LocalNewsView.as_view(), name='local_news_page'),
    path('politic-news/', PoliticNewsView.as_view(), name='politic_news_page'),
    path('sport-news/', SportNewsView.as_view(), name='sport_news_page'),
    path('internet-news/', InternetNewsView.as_view(), name='internet_news_page'),
    path('economic-news/', EconomicNewsView.as_view(), name='economic_news_page'),
]