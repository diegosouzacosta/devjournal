# coding: utf-8

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from webhooks.builders import builder


class PingView(APIView):
    '''
    Endpoint to receive github requests.
    '''
    def get(self, request, format=None):
        return Response({'ping?': 'pong!'}, status=status.HTTP_201_CREATED)


class ReceiveRequestsView(APIView):
    '''
    Endpoint to receive github requests.
    '''
    def post(self, request, format=None):
        github_event = request.META.get('HTTP_X_GITHUB_EVENT')
        if builder(github_event, request.data):
            return Response({}, status=status.HTTP_201_CREATED)
        return Response({}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
