from django.contrib import admin
from .models import Category, Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published', 'author') # Campos que se mostrarán 
    ordering = ('author',) # Se podra ordenar por autor
    search_fields = ('title', 'author__username', 'categories__name') # se podra buscar desde estos campos
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name') # lista de filtrado 


    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

