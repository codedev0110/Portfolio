from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def get_previous(self):
        return BlogPost.objects.filter(
            created_at__lt=self.created_at,
            published=True
        ).first()

    def get_next(self):
        return BlogPost.objects.filter(
            created_at__gt=self.created_at,
            published=True
        ).order_by('created_at').first()