from django.db import models
from datetime import date

from django.urls import reverse


# Create your models here.


class Category(models.Model):
    """Kategoriya"""
    name = models.CharField("Kategoriya", max_length=150)
    description = models.TextField("tavsifi")
    url = models.SlugField(max_length=160)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriy"


class Actor(models.Model):
    """Aktior va rejisiyor"""

    name = models.CharField("Ism", max_length=100)
    age = models.PositiveSmallIntegerField("Yosh", default=0)
    description = models.TextField("Tavsifi")
    image = models.ImageField("Tasvirlar", upload_to="actors/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Aktyor va rejissor"
        verbose_name_plural = "Aktyor va rejissor"

class Genre(models.Model):
    """Janiri"""
    name = models.CharField("Ism", max_length=100)
    description = models.TextField("Tavsifi")
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Janr"
        verbose_name_plural = "Janr"

class Movie(models.Model):
    """Film"""
    title = models.CharField("Nomlash", max_length=100)
    tagline = models.CharField("shiori",max_length=100, default='')
    description = models.TextField("Tavsifi")
    poster = models.ImageField("Afisha", upload_to="movies/")
    year = models.PositiveSmallIntegerField("Ma'lumotlarni kiritish",default=2019)
    cauntry = models.CharField("Sahifa", max_length=30)
    derectors = models.ManyToManyField(Actor, verbose_name="rejissor", related_name="kino_rejissyor")
    actors = models.ManyToManyField(Actor, verbose_name="aktyor", related_name="kino_aktyor")
    genres = models.ManyToManyField(Genre, verbose_name="janr")
    world_premiere = models.DateField("Jahon premyerasi", default=date.today)
    budget = models.PositiveIntegerField("Byudjet", default=0, help_text="dollar miqdorini kiriting")
    fees_in_usa = models.PositiveIntegerField(
        "AQSh to'lovlari",default=0, help_text="dollar miqdorini kiriting"
    )
    fees_in_world = models.PositiveIntegerField(
        "Dunyodagi to'lovlar", default=0, help_text="dollar miqdorini kiriting"
    )
    category = models.ForeignKey(
        Category, verbose_name="Kategoriya",on_delete=models.SET_NULL,null=True
    )

    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Qoralama", default=False)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.url})


    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kino"

class MovieShots(models.Model):
    """Kino kadrlar"""
    title = models.CharField("Sarlavha", max_length=100)
    description = models.TextField("Tavsifi")
    image = models.ImageField("Tasvir", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Kino", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Kino ramka"
        verbose_name_plural = "Kino ramka"


class RatingStar(models.Model):
    """Yulduz reytingi"""
    value = models.PositiveSmallIntegerField("Manosi", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Reyting yulduzi"
        verbose_name_plural = "Reyting yulduzi"


class Rating(models.Model):
    """Reyting"""
    ip = models.CharField("IP manzili", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="yulduz")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="kino")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Reyting"
        verbose_name_plural = "Reyting"

class Reviews(models.Model):
    """Sharhlar"""
    email = models.EmailField()
    name = models.CharField("Ism", max_length=100)
    text = models.TextField("Xabar", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Ota-ona", on_delete=models.SET_NULL, blank=True, null=True
    )
    movie = models.ForeignKey(Movie, verbose_name="Kino", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"


    class Meta:
        verbose_name = "Ko‘rib chiqish"
        verbose_name_plural = "Ko‘rib chiqish"


