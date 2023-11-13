from rest_framework import serializers

from offices.models import Office, Room, Employee


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class EmployeeSerializer(serializers.Serializer):
    room = serializers.IntegerField()
    name = serializers.CharField(max_length=40)
    start_date = serializers.DateTimeField(read_only=True)
    end_date = serializers.DateTimeField(read_only=True)
    # rooms_history = serializers.ManyRelatedField(Room, blank=True)
