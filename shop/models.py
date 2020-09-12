from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True,
                            verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True,
                            verbose_name='URL-путь')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField(max_length=255, db_index=True,
                            verbose_name='Наименование')
    slug = models.SlugField(max_length=255, db_index=True,
                            verbose_name='URL-путь')
    image = models.ImageField(upload_to='products', blank=True,
                              verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')
    updated = models.DateTimeField(auto_now=True, verbose_name='Обновленно')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
