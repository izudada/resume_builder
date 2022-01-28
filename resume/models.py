from django.db import models

from account.models import User, TrackingModel


class Profile(TrackingModel, models.Model):
    """
        Model for singular resume details
    """
    about_me = models.TextField()
    belongs_to = models.ForeignKey(User, related_name="belongs_to", on_delete= models.CASCADE, null=False)
    address = models.CharField(max_length=150)
    blog_url = models.CharField(max_length=200, null=True)
    facebook_profile = models.CharField(max_length=120, null=True)
    twitter_profile = models.CharField(max_length=120, null=True)
    linkedin_profile = models.CharField(max_length=120, null=True)
    portfolio_url = models.CharField(max_length=120, null=True)