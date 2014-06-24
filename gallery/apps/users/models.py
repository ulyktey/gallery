import os
import uuid

from gallery import settings

from django.db import models
from django.contrib.auth.models import User

def get_image_path(instance, fname):
    new_fname, ext = os.path.splitext(fname)
    return os.path.join('files', str(instance.user.id),
                            'profile', '%s%s' % (uuid.uuid4().hex, ext))

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    picture = models.ImageField(upload_to=get_image_path,
                                max_length=2500,
                                blank=True)

    def admin_image(self):
        return '<img src="%s%s/%s"/>' % (settings.MEDIA_URL,
                                         os.path.join('files',
                                                      str(self.user.id),
                                                      'profile'),
                                         self.picture)

    admin_image.allow_tags = True

    def save(self, *args, **kwargs):
        self.picture.name = os.path.basename(self.picture.name)
        super(UserProfile, self).save(*args, **kwargs)


    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

