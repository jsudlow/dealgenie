from django.db import models
# Create your models here.
class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=9, decimal_places=2)
    product_pub_date =  models.DateTimeField('date published')

    def __unicode__(self):
    	return self.product_title

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    product_image_name = models.CharField(max_length=200)
    product_image =  models.ImageField(upload_to='product_images')
    def __unicode__(self):
    	return self.product_image_name


class ProductReview(models.Model):
    product = models.ForeignKey(Product)
    product_review_pub_date = models.DateTimeField('date published')
    rating = models.IntegerField()
    product_review_text = models.TextField()
    product_review_author = models.CharField(max_length=200)