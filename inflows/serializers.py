from rest_framework import serializers
from inflows.models import Inflow

class InflowsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Inflow
        fields = '__all__'