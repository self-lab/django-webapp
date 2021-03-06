from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User                                     # User is predefined in Django
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)                                    # Title with maximium lenght
    content = models.TextField()                                                # Unrestricted Text
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)                  # If a user is deleted, earse all posts, also

    def __str__(self):
        '''
        Overwrites existing Function. Use python manage.py shell
        -> from blog.models import Post
        -> from django.contrib.auth.models import User
        -> user = User.objects.all.filter(username='milan').first()
        -> post = Post.objects.all() -> Will now display the title
        '''
        return self.title

    def get_absolute_url(self):                                                 # Tells django how to find url to a post
        '''
        Redirect will redirect to a route, reverse returns the url as a string.
        The view will handle the redirect.
        '''
        return reverse('post-detail', kwargs={'pk': self.pk})
