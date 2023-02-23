from django.db import models


class Posts(models.Model):
    post_content = models.CharField(max_length=500,blank=False,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    post_img = models.ImageField(upload_to='static/uploads/posts',blank=True)
    likes_count = models.PositiveIntegerField(default=0)



