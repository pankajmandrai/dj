from django.shortcuts import render

# Create your views here.
from guideline.models import Patientdata, Patientguidelines, Recommendations
from rest_framework import viewsets
from guideline.serializers import PatientdataSerializer, PatientguidelinesSerializer, RecommendationsSerializer


class PatientdataViewSet(viewsets.ModelViewSet):
    queryset = Patientdata.objects.all()
    serializer_class = PatientdataSerializer

class PatientguidelinesViewSet(viewsets.ModelViewSet):
    queryset = Patientguidelines.objects.all()
    serializer_class = PatientguidelinesSerializer

class RecommendationViewSet(viewsets.ModelViewSet):
    queryset = Recommendations.objects.all()
    serializer_class = RecommendationsSerializer