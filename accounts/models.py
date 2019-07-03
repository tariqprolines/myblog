from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    BEGINNER = 1
    AVERAGE = 2
    EXPERT = 3
    EXPERIENCE_CHOICES=(
        (BEGINNER,'Beginner'),
        (AVERAGE, 'Average'),
        (EXPERT, 'Expert')
    )
    BEGINNER = 1
    AVERAGE = 2
    EXPERT = 3
    English_LEVEL = (
        (BEGINNER, 'Beginner'),
        (AVERAGE, 'Average'),
        (EXPERT, 'Expert')
    )

    user= models.OneToOneField(User, on_delete=models.CASCADE)
    avatar= models.ImageField(upload_to='users/images', null=True, blank=True)
    phone= models.CharField(max_length=20 , default='')
    profession= models.CharField(max_length=20, default='')
    skills= models.CharField(max_length=50, null=True, blank= True)
    experience= models.PositiveSmallIntegerField(choices=EXPERIENCE_CHOICES, null= True, blank= True)
    hourly_rate= models.CharField(max_length= 10, default = '')
    total_project= models.CharField(max_length= 10, default= '')
    english_level= models.PositiveSmallIntegerField(choices=English_LEVEL, null= True, blank= True)
    availability=models.CharField(max_length= 10, default='')
    bio=models.TextField(max_length=500, blank= True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

