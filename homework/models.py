from django.db import models
from django.contrib.auth.models import User


TYPE_CHOICES = (('1', u'本科生'), ('2', u'研究生'), ('3', u'教师'), ('4', u'访客'),)


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique = True)
    phone = models.CharField(max_length = 20)
    address = models.CharField(max_length = 100)
    type1 = models.CharField(max_length=50, choices=TYPE_CHOICES, )
    stu_num = models.CharField(max_length = 20) 