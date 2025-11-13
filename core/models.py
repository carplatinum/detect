from django.db import models


class Image(models.Model):
    original_image = models.ImageField(upload_to='original_images/')
    translated_image = models.ImageField(upload_to='translated_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    text_original = models.TextField(blank=True, null=True)
    text_translated = models.TextField(blank=True, null=True)
    is_translated = models.BooleanField(default=False)

    def __str__(self):
        return f"Image {self.pk} uploaded at {self.created_at}"
