from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class BlogDetails(models.Model):

    blog_title = models.CharField(max_length=150,verbose_name="Blog Title")
    blog_image = models.FileField(verbose_name="Blog Image",upload_to='blogs',null=True,blank=True)
    blog_content = RichTextField(verbose_name="Blog Content",null=True,blank=True)
    is_active = models.BooleanField(verbose_name="Status",default=True)

    class Meta:
        db_table = 'blog_details'
        verbose_name = 'blog_details'
        verbose_name_plural = 'blog_details'

    def __str__(self):
        return self.blog_title
