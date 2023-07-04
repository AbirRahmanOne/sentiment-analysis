from django.urls import path
from sentiment_analysis.views import SentimentAnalysisApiView


urlpatterns = [
    path('analyze/', SentimentAnalysisApiView.as_view())
]