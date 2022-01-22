from django.db import models

# Create your models here.


class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=10) 
    date_created = models.DateField(verbose_name="Created on date", auto_now_add="True")
    SUBJECTS_LIST = {
        ('Order status', 'Order status'),
        ('Payment', 'Payment'),
        ('Products', 'Products'),
        ('Complaints', 'Complaints'),
        ('Other', 'Other'),
    }
    subject = models.IntegerField(choices=SUBJECTS_LIST, default=1)

    def __str__(self):
        return self.user.username
