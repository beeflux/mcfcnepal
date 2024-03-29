from django.db import models

# Create your models here.
class MemberactiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

class ActiveAdminMemberManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

CHOICES = [
    (1,'International'),
    (2,'National'),
]


class Members(models.Model):
    full_name = models.CharField(max_length=100)
    member_type = models.IntegerField(choices = CHOICES, default=1)
    image = models.ImageField(upload_to='member/images', default='member/images/propic.png')
    email = models.EmailField()
    dob = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    objects = MemberactiveManager()

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'Member'
    
    

class AdminMember(models.Model):
    position = models.CharField(max_length=20)
    image = models.ImageField(upload_to='member/admin/images', default='member/images/propic.png')
    name = models.CharField(max_length=20)
    contact_no = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    objects = ActiveAdminMemberManager()
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'admin_member'

