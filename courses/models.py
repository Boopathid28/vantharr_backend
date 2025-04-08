from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class CourseCategory(models.Model):

    category_name = models.CharField(max_length=150,verbose_name="Category Name")

    class Meta:
        db_table = 'course_category'
        verbose_name = 'course_category'
        verbose_name_plural = 'course_category'

    def __str__(self):
        return self.category_name
    

class CourseDetails(models.Model):

    category = models.ForeignKey(CourseCategory,verbose_name="Category",on_delete=models.PROTECT)
    course_url = models.CharField(max_length=150,verbose_name="URL",unique=True,null=True,blank=True)
    course_title = models.CharField(max_length=150,verbose_name="Course Title")
    course_image = models.FileField(verbose_name="Course Image",upload_to='courses',null=True,blank=True)
    course_content = RichTextField(verbose_name="Course Content",null=True,blank=True)
    is_active = models.BooleanField(verbose_name="Status",default=True)
    seo_title = models.TextField(max_length=150,verbose_name="SEO Title",null=True,blank=True)
    seo_description = models.TextField(max_length=150,verbose_name="SEO Description",null=True,blank=True)
    seo_keywords = models.TextField(max_length=150,verbose_name="SEO Keywords",null=True,blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        course_title_name = self.course_title.split(' ')
        couse_url_name ='-'.join(s.lower() for s in course_title_name)
        self.course_url = couse_url_name
        super().save(update_fields=['course_url'])

    class Meta:
        db_table = 'course_details'
        verbose_name = 'course_details'
        verbose_name_plural = 'course_details'

    def __str__(self):
        return self.course_title
