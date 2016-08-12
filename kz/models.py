# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)  # 博客题目
    category = models.CharField(max_length=50, blank=True)  # 博客标签
    date_time = models.DateTimeField(auto_now_add=True)  # 博客日期
    content = RichTextUploadingField(blank=True, null=True)  # 博客文章正文

    # python2使用__unicode__, python3使用__str__
    def __str__(self):
        return self.title

    class Meta:  # 按时间下降排序
        ordering = ['-date_time']


class Post(models.Model):
    content = RichTextField()

class Article_test(models.Model):
    '''日志'''
    title = models.CharField(verbose_name='标题', max_length=150, blank=False, null=False)
    content = RichTextField('正文') # 使用ckeditor中的RichTextField

class Entry(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    images = models.ImageField(upload_to='static/upload/images/%Y/%m/%d', blank=True)
    # tags = models.ManyToManyField('Tag')
    body = RichTextUploadingField() #RichTextField()