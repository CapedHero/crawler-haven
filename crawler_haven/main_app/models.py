from django.contrib.auth.models import User
from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'main_app/user_{0}/{1}'.format(instance.user.id, filename)


class WebCrawler(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    script = models.FileField(upload_to=user_directory_path)
