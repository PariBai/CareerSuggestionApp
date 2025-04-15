from django.contrib import admin
from django.urls import path
from careers.views import SuggestCareerView , index, career_results, about, contact
from django.http import JsonResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('suggest-career/', SuggestCareerView.as_view(), name='suggest_career'),
    path('career-results/', career_results, name='career_results'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
