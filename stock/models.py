from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=71)

    def __str__(self):
        return self.name


class Stock(models.Model):
    nama = models.CharField(max_length=155)
    kategori = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="kategori")
    date = models.DateTimeField(default=timezone.now)
    jumlah = models.IntegerField(null=True, blank=True)
    harga = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nama

    def get_absolute_url(self):
        return reverse('detailstock', args=[str(self.id)])
