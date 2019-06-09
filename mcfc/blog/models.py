from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    meta_description = models.TextField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(upload_to='blog/images', blank=True, null = True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "Blog"
        ordering = ['-date']
