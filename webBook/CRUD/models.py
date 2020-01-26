from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=50,null=False)
    author = models.CharField(max_length=50,null=False)
    pub_date = models.DateField(null=True)
    pages = models.IntegerField("Pages")
    type_choice = (
        ('Novel', 'Novel'),
        ('Documentation', 'Documentation'),
        ('Comic','Comic'),
        ('Biography', 'Biography'),
        ('Encyclopedia', 'Encyclopedia'),
    )
    types = models.CharField(max_length=25, choices=type_choice, default='Novel')

def __unicode__(self):
    return self.title