from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User  # Pro propojení s uživateli


# Tabulka pro kraje
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Název kraje

    def __str__(self):
        return self.name


# Tabulka pro města
class City(models.Model):
    name = models.CharField(max_length=100)  # Název města
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities')  # Propojení s krajem

    def __str__(self):
        return f"{self.name} ({self.region.name})"


# Main table for partners
class Partner(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='partner_images/', null=True, blank=True)
    coints = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(999)])
    description = models.TextField(null=True, blank=True)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='partners',
        null=True,  # Pokud chcete povolit, aby bylo pole volitelné
        blank=True  # Pokud chcete povolit prázdné hodnoty ve formulářích
    )

    def __str__(self):
        return self.name

# Contact information for each partner
class Contact(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.name


# Payment information related to contacts
class Payment(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.CharField(max_length=50)  # e.g., payment, refund, bonus, etc.

    def __str__(self):
        return f'{self.type} - {self.amount}'


# Categories for partners
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Portfolio for each partner
class Portfolium(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    type = models.ForeignKey('PortfoliumType', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.partner.name} - {self.type.name}'


# Types of portfolio entries
class PortfoliumType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Content directly linked to Partner
class Content(models.Model):
    partner = models.OneToOneField(Partner, on_delete=models.CASCADE, related_name='content')  # Napojení na partnera
    html_content = models.TextField()  # Obsah s HTML

    def __str__(self):
        return f"Content for {self.partner.name}"


# Registered customers
class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Reviews given by customers
class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    rating = models.IntegerField()  # e.g., number of stars
    review_content = models.TextField()

    def __str__(self):
        return f'Review by {self.customer.name} for {self.partner.name}'


# Staff members
class Staff(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Permissions for staff members
class StaffRule(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    permission_level = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.staff.name} - {self.permission_level}'


# Post
class Post(models.Model):
    title = models.CharField(max_length=200)  # Nadpis příspěvku
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # Kdo postoval
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)  # Fotka příspěvku
    content = models.TextField()  # Hlavní dlouhý text
    created_at = models.DateTimeField(auto_now_add=True)  # Datum postování

    def __str__(self):
        return self.title


# OpeningHours
class OpeningHours(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Pondělí'),
        ('Tuesday', 'Úterý'),
        ('Wednesday', 'Středa'),
        ('Thursday', 'Čtvrtek'),
        ('Friday', 'Pátek'),
        ('Saturday', 'Sobota'),
        ('Sunday', 'Neděle'),
    ]
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='opening_hours')
    day = models.CharField(choices=DAYS_OF_WEEK, max_length=10)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f"{self.partner.name} - {self.day}"


# Feature
class Feature(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)  # Např. fa-wheelchair, fa-paw

    def __str__(self):
        return self.name


# PartnerFeature
class PartnerFeature(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='features')  # Nechat původní
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.partner.name} - {self.feature.name}"


# PriceList
class PriceList(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='price_list')
    service_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.partner.name} - {self.service_name}"


# Partner_Gallery
class Gallery(models.Model):
    partner = models.ForeignKey(Partner, on_delete=models.CASCADE, related_name='gallery')
    image = models.ImageField(upload_to='partner_gallery/')

    def __str__(self):
        return f"{self.partner.name} - {self.image.url}"
