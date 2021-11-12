
# Create your models here.

from django.db import models
from django.urls import reverse
# Create your models here.


class Blog(models.Model):

    # relation's
    author = models.ForeignKey('Author', null=True, on_delete=models.CASCADE)

    # information's
    title = models.CharField(max_length=127, null=True, blank=True)
    text = models.TextField(help_text='Bura esas melumati daxil edin...')
    slug = models.SlugField(max_length=255, null=True)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs' # 
        ordering = ('-created_at',)

    def get_absolute_url(self):
        return reverse('blog:blog-detail', args=[self.slug])


    def __str__(self):
        return f'Blog {self.title}'


class Author(models.Model):

    # information's
    name = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)

    # moderation's
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Elave edilme tarixi')
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name='Duzelis edilme tarixi')

    class Meta:
        verbose_name = 'Müəllif'
        verbose_name_plural = 'Müəlliflər' 
        ordering = ('-created_at',)


    def __str__(self):
        return f'Author {self.name}'
