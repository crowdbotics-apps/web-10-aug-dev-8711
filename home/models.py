from django.conf import settings
from django.db import models

# Create your models here.

from django.db import models


class CustomText(models.Model):
    nfghgfhgf = models.BigIntegerField(null=True, blank=True,)
    hvghgjgjhgfhjg = models.TextField(null=True, blank=True,)
    demoUser = models.ForeignKey(
        "home.HomePage",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="customtext_demoUser",
    )

    def __str__(self):
        return self.title

    @property
    def api(self):
        return f"/api/v1/customtext/{self.id}/"

    @property
    def field(self):
        return "title"


class HomePage(models.Model):
    jhgfhjgjhgjhg = models.BigIntegerField(null=True, blank=True,)
    demoUser = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="homepage_demoUser",
    )

    @property
    def api(self):
        return f"/api/v1/homepage/{self.id}/"

    @property
    def field(self):
        return "body"
