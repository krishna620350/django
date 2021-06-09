from django.db import models

# Create your models here.
class Contact(models.Model):
    username = models.CharField(max_length=122)
    recipt = models.CharField(max_length=122)
    cost = models.CharField(max_length=122)
    urlname = models.CharField(max_length=122)
    username1 = models.CharField(max_length=122)
    textarea = models.TextField()

    def __str__(self):
        return self.username
#after creating models run "python manage.py makemigration"
#makemigraton means create changes and store in file
#and than "python manage.py migration"
#migrate = apply the pending chjanges create by makemaigration