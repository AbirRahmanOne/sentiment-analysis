from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
import logging
from rest_framework.views import APIView
import torch
from setfit import SetFitModel

model = SetFitModel.from_pretrained("StatsGary/setfit-ft-sentinent-eval")

logger = logging.getLogger(__name__)


# Create your views here.

class SentimentAnalysisApiView(APIView):

    def post(self, request):
        text = request.data.get('text', None)
        try:
            sentiment_analysis = model([text])
            sentiment = torch.tensor(sentiment_analysis)

            if sentiment.item() == 1:
                response = {
                    'sentiment': 'positive'
                }
            elif sentiment.item() == 0:
                response = {
                    'sentiment': 'negative'
                }
            else:
                response = {
                    'sentiment': 'negative'
                }
            return Response(response, status=status.HTTP_200_OK)

        except Exception or KeyError as e:
            logger.error(e, exc_info=True)
            return Response({"message": "Serve side error!"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
