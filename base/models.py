from django.core.validators import RegexValidator
from django.db import models
import uuid
import os


class Category(models.Model):
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position',)

class Dish(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('dishes/', new_filename)

    slug = models.SlugField(max_length=200, db_index=True)
    name = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField()
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    descriotion = models.TextField(max_length=500, blank=True)
    ingredients = models.CharField(max_length=200)
    spesial = models.BooleanField(default=False)
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position','price',)
        index_together = (('id', 'slug'),)

class UserReservation(models.Model):
    mobile_re = RegexValidator(regex=r'^(\d{3}[-.]?){2}\d{4}$', message="Phone in format xxx xxx xxxx")
    email_re = RegexValidator(regex=r'^[^@\s]+@[^@\s]+\.[^@\s]+$', message="Email in format *@*.*")
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=30, validators=[email_re], blank=True)
    phone = models.CharField(max_length=15, validators=[mobile_re])
    persons = models.PositiveSmallIntegerField()
    message = models.TextField(max_length=200 ,blank=True)
    #dateonly = models.DateField()
    #timeonly = models.TimeField()
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} ,{self.phone}, {self.email}, {self.message[:50]}'

    class Meta:
        ordering = ('-date','-is_processed',)


#class Events(models.Model):

    #def get_file_name(self, filename: str) -> str:
    #    ext_file = filename.strip().split('.')[-1]
     #   new_filename = f'{uuid.uuid4()}.{ext_file}'
    #    return os.path.join('dishes/', new_filename)

  #  name = models.CharField(unique=True, max_length=50, db_index=True)
  #  position = models.SmallIntegerField(unique=True)
  #  is_visible = models.BooleanField(default=True)
  #  price = models.IntegerField(max_digits=8)
  #  descriotion = models.TextField(max_length=1600, blank=True)
  #  photo = models.ImageField(upload_to=get_file_name)

  #  def __str__(self):
 #       return f'{self.name}'

  #  class Meta:
  #      ordering = ('position',)


#class Gallery(models.Model):

   # def get_file_name(self, filename: str) -> str:
   #     ext_file = filename.strip().split('.')[-1]
   #     new_filename = f'{uuid.uuid4()}.{ext_file}'
   #     return os.path.join('dishes/', new_filename)

  #  name = models.CharField(unique=True, max_length=50, db_index=True)
   # position = models.SmallIntegerField(unique=True)
  #  photo = models.ImageField(upload_to=get_file_name)

 #   def __str__(self):
  #      return f'{self.name}'

 #   class Meta:
  #      ordering = ('position',)