from rest_framework import serializers
from app.models import Contact


### Creating a Serializer class
# class ContactSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     title = serializers.CharField(max_length=100)
#     email = serializers.EmailField(max_length=50)

#     def create(self, validated_data):
#         return Contact.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.title = validated_data.get("title", instance.title)
#         instance.email = validated_data.get("email", instance.email)

#         instance.save()
#         return instance


### Using ModelSerializers
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Contact
        fields = ["name", "title", "email", "url", "owner"]
