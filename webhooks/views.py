# coding: utf-8

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
    def get(self, request, format=None):
        return Response({}, status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        print(1)
        # TODO
        return Response({}, status=status.HTTP_201_CREATED)
