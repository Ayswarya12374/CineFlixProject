from django.urls import path

from . import views

urlpatterns=[

    path('',views.HomeView.as_view(),name='home'),

    path('movie-list/',views.MoviesView.as_view(),name='movie-list'),

    path('movie-create/',views.MoviewCreateView.as_view(),name='movie-create'),

    # path('movie-details/<int:id>/',views.MovieDetailsView.as_view(),name='movie-details'),
    
    path('movie-details/<str:uuid>/',views.MovieDetailsView.as_view(),name='movie-details'),

    
]