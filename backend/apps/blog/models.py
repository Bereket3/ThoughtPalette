from django.db import models
from taggit.managers import TaggableManager
from user.models import AuthUserModel as User


class BlogComponent(models.Model):
    """
    individual componet of blog
    """

    content_type = models.CharField(max_length=225)
    file_content = models.FileField(upload_to="file_content", null=True, blank=True)
    text_content = models.TextField(blank=True, null=True)
    next_node = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        related_name="next_node_block",
    )

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk) + " " + str(self.content_type)


class BlogTree(models.Model):
    """
    Tree like structure where different contents are
    pluged like a branch
    """

    blog_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=225)
    blog_root = models.ForeignKey(BlogComponent, on_delete=models.SET_NULL, null=True)
    blog_tags = TaggableManager()
    isPublished = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title.__str__()
