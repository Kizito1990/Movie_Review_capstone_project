from rest_framework import serializers
from.models import User, Review

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password':{'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user
        
class Reviewseializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Review
        fields = ['movie_title', 'content','rating', 'user', 'created_date' ]
        read_only_fields = ['user', 'created_date']

        def rating(self, value):
            if not (1 <= value <= 5):
                raise serializers.ValidationError("Rating must be between 1 and 5.")
            return value