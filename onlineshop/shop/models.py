from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

# Create your models here.

# Category - 중첩, 레벨이 있게
"""
name
slug
description
image
"""

class Category(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True, related_name='sub_categories')
    image = models.FileField(upload_to='media/%Y/%m/%d', blank=True)
    # description = models.TextField()
    description = RichTextUploadingField()
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=120, )

    class Meta:
        ordering = ['name']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_in_category', args=[self.slug])

# Product
"""
category
name
slug
image
description

price
stock
available_display
available_order

created
updated
"""

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    name = models.CharField(max_length=30)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=120, )
    image = models.FileField(upload_to='media/%Y/%m/%d', blank=True)
    description = RichTextUploadingField()

    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    available_display = models.BooleanField(default=True)
    available_order = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-created']
        index_together = [['id','slug']]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])