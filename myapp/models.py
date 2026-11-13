from django.db import models


def gen_unique_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f'{uuid.uuid4()}.{ext}'
    return f'products/{new_filename}'

CATEGORIES = [
    ('Food', 'Food Category'),
    ('Toiletry', 'Toiletry Category'),
    ('Spices', 'Spices Category'),
    ('Hardware', 'Hardware Category'),

]

# Create your models here.
# logic that interacts with the database

class Product(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField(default=0)
    for_sale = models.BooleanField(default=True)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    pic = models.ImageField(upload_to='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # provides additional info
    class Meta:
        db_table = 'product'

# run your migrations
#python manage.py makemigrations
# python manage.py migrate