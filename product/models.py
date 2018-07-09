from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse



class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    image = models.FileField(upload_to='product/image', blank=True, null=True)
 
    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'
 
    def __unicode__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])
 
 
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True, null=True)
    addition = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.FileField(upload_to='product/image', blank=True, null=True)
    
 
    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)
 
    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])



class Try(models.Model):
    image = models.FileField(upload_to='product/image', blank=True, null=True)

    
