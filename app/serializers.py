from rest_framework import serializers
from .models import Club
from django.contrib.auth import get_user_model

User = get_user_model()
class ClubSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if 'name' not in attrs.keys():
            raise serializers.ValidationError('Name not provided')
        if 'age' not in attrs.keys():
            raise serializers.ValidationError('Age not provided')
        
        if 'bio' not in attrs.keys():
            raise serializers.ValidationError('Bio not provided')
        return attrs
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField(min_value=0)
    bio = serializers.CharField(max_length=500)
    class Meta:
        model = Club
        fields = ["id", "name", "age", "bio"]

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','password','first_name', 'last_name')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def validate(self, attrs):
        if len(attrs.get('password')) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters')
        return attrs
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], password = validated_data['password'])
        return user