from django.contrib import admin

from .models import Author, Category, Post

admin.site.register(Author)
admin.site.register(Category)



from django.contrib import admin
from .models import Tag

admin.site.register(Tag)  # Tag modelini admin panelinə əlavə et
from django.contrib import admin
from .models import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','overview','content','author')
    search_fields = ('title','slug','overview','content','author')
    list_filter = ('title', 'overview', 'content', 'author')
    
