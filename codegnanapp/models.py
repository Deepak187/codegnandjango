from django.db import models
from django.contrib.auth.models import User

"""if we are adding new feilds to the model we can write null = True , blank=True then we will not get this message
You are trying to add the field 'created_at' with 'auto_now_add=True' to post without a default; the database 
needs something to populate existing rows."""


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # here i am creating meta class because i dont want this table to be created in the database
    class Meta:
        abstract = True


class Post(Timestamp):
    title = models.CharField(max_length=100, verbose_name='MovieName')
    description = models.TextField()
    image = models.ImageField(upload_to='')
    likes= models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(Timestamp):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment
