from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=60, null=True)
    image = models.ImageField(upload_to="images/")
    summary = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.summary
