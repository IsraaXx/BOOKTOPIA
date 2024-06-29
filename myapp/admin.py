from django.contrib import admin
from .models import BookDetails
from .models import register3

admin.site.register(register3)

class BookAdmin(admin.ModelAdmin):
    
    def get_list_display(self, request):
        return ('title', 'author', 'isbn10', 'isbn13','overview1','overview2','image_url','authorImage_url', 'category', 'available', 'btn', 'pdf')
    
admin.site.register(BookDetails,BookAdmin)