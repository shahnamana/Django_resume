from django.db import models



# Create your models here.

# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to='about')

    class Meta:
        verbose_name = 'About Me'
        verbose_name_plural = 'About Me'

    def __str__(self):
        return "About Me"


class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name='Service name')
    description = models.TextField(verbose_name="About Service")

    def __str__(self):
        return self.name


# Recent Work Model

class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name='Work Title')
    image = models.ImageField(upload_to='works')

    def __str__(self):
        return self.title


class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name='Client Say')
    image = models.ImageField(upload_to='clients', default='default.png')

    def __str__(self):
        return self.name


class Certificate(models.Model):
    title = models.CharField(max_length=100, verbose_name='Certificate Title')
    credential_id = models.TextField(verbose_name="Credential ID")
    credential_url = models.URLField(verbose_name="Credential ID")
    issuing_organization = models.CharField(max_length=100, verbose_name="Issuing Organization")
    issue_date = models.DateTimeField(verbose_name="Issue Date")
    certification_image = models.ImageField(upload_to="certificateimage")

    def __str__(self):
        return self.title

