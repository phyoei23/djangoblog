from django.db import models

class POst(models.Model):
    STATUS_CHOICES = [
        ('draft','Draft'),('published','Published')
    ]
    titel = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.titel

