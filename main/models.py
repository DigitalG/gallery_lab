from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)

    def thumbnail_object(self):
        artworks = Artwork.objects.filter(category=self)

        return artworks[0]

    def __str__(self):
        return self.name


class Artwork(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField('Зображення',
                              upload_to='images',
                              null=False,
                              blank=False)
    description = models.TextField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Tags = models.CharField(max_length=500)
    post_date = models.DateField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name
