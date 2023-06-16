from django.contrib import admin

from models import Book, Author, Member

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Member)

@admin.register(Book)
class BookAdmin (admin.ModelAdmin):
    list_display = ('title','publication_date','display_author')
    list_filter = ('publication_date','authors')
    search_fields = ('title','authors__name')

    def display_authors(self,obj):
        return f', '.join([author.name for author in obj.author.all()])
    display_auhtors.short_description = 'Authors'