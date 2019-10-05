from guideline.models import Patientdata, Patientguidelines, Recommendations
from rest_framework import serializers
#from guideline import models, Patientdata, Patientguidelines, Recommendations

class PatientdataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patientdata
        fields = ['name', 'date', 'gender','systolic_BP', 'diastolic_BP', 'smoking_years', 'no_of_packs', 'fasting_blood_sugar', 'hypothyroid','obese', 'intravenous_drug_abuse']


class PatientguidelinesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patientguidelines
        fields = ['id','url', 'patient']


class RecommendationsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recommendations
        fields = ['id','url', 'recommendation', 'conditions', 'references']