from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
from userreg.models import Profile

class Post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    imgg = models.ImageField(default='default1.jpg', upload_to='posts_media')

    
    def save(self):
        super().save()

        imgg = Image.open(self.imgg.path)

        
        if imgg.height > 300 or imgg.width > 300:
            output_size = (300, 300)
            imgg.thumbnail(output_size)
            imgg.save(self.imgg.path)


    def __str__(self, *args, **kwargs):
        return f'{self.caption} {self.author} {self.imgg}'


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    