from django.contrib import admin

from books.models import Book, Genre

# Register your models here.

# admin.site.register(Book)


def make_published(modeladmin, request, queryset):
    queryset.update(is_published=True)


make_published.short_description = "Дата создания"


def make_unpublished(modeladmin, request, queryset):
    queryset.update(is_published=False)


make_unpublished.short_description = "Не опубликовано"


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    actions = [make_published, make_unpublished]
    search_fields = ('name',)
    list_editable = ['slug', 'is_published']
    list_display = ['pk','name', 'slug', 'is_published']
    list_display_links = ('name',)
    list_filter = ('is_published',  'name', 'slug', )

    def get_list_display(self, request):
        l_d = ['name', 'slug', 'pk']
        if (request.user.is_superuser):
            l_d += ['is_published']
        return l_d

    def get_search_fields(self, request):
        s_d = ['name']
        if (request.user.is_superuser):
            s_d += ['slug']
        return s_d

    def get_list_display_links(self, request, list_display):
        if (not request.user.is_superuser):
            return None
        else:
            return ['name']

    def get_list_filter(self, request):
        f_d = ['is_published']
        if (request.user.is_superuser):
            f_d += ['name', 'slug', ]
        return f_d


# admin.site.register(Book, AdminBook)
admin.site.register(Genre)
