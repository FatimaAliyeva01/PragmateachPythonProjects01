from django.contrib import admin

# Register your models here.
from . models import Blog, Author


class BlogAdminSection(admin.AdminSite):
    site_header = 'My custom site header'

blog = BlogAdminSection(name = 'Blog App Section')
blog.register(Blog)
admin.site.register(Blog)
admin.site.register(Author)