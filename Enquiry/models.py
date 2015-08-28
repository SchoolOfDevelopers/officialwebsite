from django.db import models

# Create your models here.
class Enquiry(models.Model):
    enquiry_id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=60)
    email = models.EmailField('Email',max_length=75)
    subject = models.CharField('Subject', max_length=125)
    message = models.TextField('Message',max_length=500)
    time = models.DateTimeField(auto_now_add=True, verbose_name='enquiry Time')
    resolved = models.BooleanField(default=False)
    remarks = models.TextField(max_length=512, blank=True,null=True)

    def __str__(self):
        return self.subject