from rest_framework import serializers
from django.contrib.auth.models import Permission
from .models import User, Role


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["username", "password"]


    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        role, created = Role.objects.get_or_create(name='candidate')

        if created:
            role.description = 'Can create, edit, and view only their own resumes'
            role.save()
            view_resume = Permission.objects.get(codename='view_resume')
            add_resume = Permission.objects.get(codename='add_resume')
            change_resume = Permission.objects.get(codenam='change_resume')
            delete_resume = Permission.objects.get(codename='delete_resume')
            role.permissions.set([view_resume, add_resume, change_resume, delete_resume])

        user.role = role
        user.save()

        return user