from rest_framework  import serializers
from app.models import *


class CelebratyMS(serializers.ModelSerializer):
    class Meta:
        model=Celebraties
        fields='__all__'

