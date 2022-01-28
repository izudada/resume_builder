from django.db import models

from account.models import User, TrackingModel


class Profile(TrackingModel, models.Model):
    """
        Model for singular resume details
    """
    about_me = models.TextField()
    belongs_to = models.ForeignKey(User, related_name="belongs_to", on_delete= models.CASCADE, null=False)