from django.urls import path
from . import views

urlpatterns = [
	path('animationeng/',views.animationeng_view,name='animationeng'),
    path('animation/',views.animation_view,name='animation'),
    path('',views.home_view,name='home'),
    path('image/', views.image_view, name='image'),
	path('pronoun/', views.pronoun_view, name='pronoun'),
	path('verb/', views.verb_view, name='verb'),
	path('most/', views.most_view, name='most'),
	path('emotional/', views.emotional_view, name='emotional'),
	path('place/', views.place_view, name='place'),
	path('cons/', views.cons_view, name='cons'),
	path('vowel/', views.vowel_view, name='vowel'),
	path('tone/', views.tone_view, name='tone'),
	path('family/', views.family_view, name='family'),
	path('stoA/', views.stoA_view, name='stoA'),
]
