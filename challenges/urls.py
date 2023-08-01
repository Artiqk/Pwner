from django.urls import path

from . import views

urlpatterns = [
    path('', views.ChallengeCategoryListView.as_view(), name='index'),
    path('<str:category>', views.ChallengeListView.as_view(), name='list'),
    path('<str:category>/<uuid:challenge_uuid>', views.ChallengeDetailsView.as_view(), name='details')
]
