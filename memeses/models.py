from django.db import models
from django.urls import reverse
# Create your models here.


class Tags(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Tags, self).save(*args, **kwargs)


def memes_file_name(instance, filename):
    if not instance.id:
        Memes = instance.__class__
        new_id=None
        try:
            new_id = Memes.objects.order_by("id").last().id
            if new_id:
                new_id += 1
            else:
                pass
        except:
            new_id=1
    else:
        new_id = instance.id
    return 'images/{0}.jpg'.format(new_id)



class Memes(models.Model):
    name = models.CharField(max_length=250)
    meme_image = models.ImageField(upload_to=memes_file_name)
    tags = models.ManyToManyField(Tags)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meme-detail', kwargs={'slug': self.slug})
    
    def display_tags(self):
        return ', '.join([ tags.name for tags in self.tags.all() ])

    display_tags.short_description = 'Tags'
