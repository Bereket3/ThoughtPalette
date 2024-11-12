from django.db import models


class BlogComponent(models.Model):
    """
    individual componet of blog
    """

    content_type = models.CharField(max_length=225)
    file_content = models.FileField(upload_to="file_content", null=True, blank=True)
    text_content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return str(self.pk) + " " + str(self.content_type)


class BlogNode(models.Model):
    _priv = models.ForeignKey(BlogComponent, on_delete=models.CASCADE, null=True)
    _next = models.ForeignKey(BlogComponent, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f"From {self._priv.__str__()} to {self._next.__str__()}"


class BlogTree(models.Model):
    """
    Tree like structure where different contents are
    pluged like a branch
    """

    blog_title = models.CharField(max_length=225)
    blog_genre = models.CharField(max_length=225)
    blog_content = models.ForeignKey(BlogNode, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.blog_title.__str__()
