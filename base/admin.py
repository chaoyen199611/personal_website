from django.contrib import admin

# Register your models here.
from .models import Article,Profile,Tag

class ArticleAdmin(admin.ModelAdmin):
    list_display= ('title','category','pub_date')

class TagAdmin(admin.ModelAdmin):
    list_display=('tagname',)


admin.site.register(Article,ArticleAdmin)
admin.site.register(Profile)
admin.site.register(Tag,TagAdmin)