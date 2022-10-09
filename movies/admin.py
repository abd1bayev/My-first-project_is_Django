from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Kategoriya"""
    list_display = ("id", "name", "url")
    list_display_links = ("name", )

class ReviewInline(admin.TabularInline):
    """kino sahifasini ko'rib chiqish """
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")

class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Tasvirlar"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """Film"""
    list_display = ("title", "category", "url", "draft")
    list_filter = ("category", "year")
    search_fields = ("title", "category__name")
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ("draft",)
    readonly_fields = ("get_image",)
    # fields = (("actors", "directors", "genres"), )
    fieldsets = (
        (None, {
            "fields": (("title", "tagline"),)
        }),
        (None, {
            "fields": ("description", ("poster", "get_image"))
        }),
        (None, {
            "fields": (("year", "world_premiere", "cauntry"),)
        }),
        ("Actors", {
            "classes": ("collapse",),
            "fields": (("actors", "derectors", "genres", "category"),)
        }),
        (None, {
            "fields": (("budget", "fees_in_usa", "fees_in_world"),)
        }),
        ("Options", {
            "fields": (("url", "draft"),)
        }),
    )
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110"')

    get_image.short_description = "Plakat"
@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """ko'rib chiqish"""
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Жанры"""
    list_display = ("name", "url")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Aktyor"""
    list_display = ("name", "age", "get_image")
    readonly_fields = ("get_image", )
    def get_image(self,obj):
        return mark_safe(f'<img src={obj.image.url} width = "50" height = "60"')

    get_image.short_description = "Tasvirlar"


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Reyting"""
    list_display = ("movie", "ip")

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    """kadr va film"""
    list_display = ("title", "movie", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width = "50" height = "60"')

    get_image.short_description = "Tasvirlar"



admin.site.register(RatingStar)


admin.site.site_title = "Django Filmlar"
admin.site.site_header = "Django Filmlar"
