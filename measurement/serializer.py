from rest_framework import serializers
from measurement.models import Temp_sensor, Temp_measure


class Temp_measureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temp_measure
        fields = ['id', 'temperature', 'date_current', 'temp_sensor_id']


class Temp_sensorSerializer(serializers.ModelSerializer):
    measurements = Temp_measureSerializer(read_only=True, many=True)

    class Meta:
        model = Temp_sensor
        fields = ['id', 'name', 'date_create', 'description', 'measurements']
