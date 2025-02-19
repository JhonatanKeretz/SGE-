from rest_framework import serializers
from suppliers.models import Supplier

class SuppliersSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Supplier
        fields = '__all__'