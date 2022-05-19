from django.db import models

# Create your models here.
class messagetb(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    messages = models.TextField()
    updated_at= models.DateTimeField(auto_now = True, blank = True)
    owner = models.ForeignKey('auth.User', related_name='mess', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']