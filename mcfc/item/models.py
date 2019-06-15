from django.db import models

# Create your models here.

class ItemCategory(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Item(models.Model):
    category = models.ForeignKey(ItemCategory, on_delete = models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to='item/images', default="item/images/defaultitem.png")
    date = models.DateTimeField(auto_now=True)
    expiry_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Item'
        ordering = ['-date']

class ItemOffer(models.Model):
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE, related_name='itemoffers')
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Item Offer'
        ordering = ['start_date']



