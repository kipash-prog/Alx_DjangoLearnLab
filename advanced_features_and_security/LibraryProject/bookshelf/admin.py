# bookshelf/admin.py
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    search_fields = ('title', 'author')  # Enable searching by title and author
    list_filter = ('publication_year',)  # Enable filtering by publication year

# Alternatively, you can register the model directly:
# admin.site.register(Book, BookAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(publication_year__gte=2000)
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.save()
        
    def delete_model(self, request, obj):
        obj.delete()
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_view_permission(self, request, obj=None):
        return True
    
    def has_module_permission(self, request):
        return True
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        del actions['delete_selected']
        return actions
    
    def get_list_display(self, request):
        return super().get_list_display(request) + ('created_by',)
    
    def created_by(self, obj):
        return obj.created_by.username
    
    created_by.short_description = 'Created By'
    
    def get_list_filter(self, request):
        return super().get_list_filter(request) + ('created_by',)
    
    def get_search_fields(self, request):
        return super().get_search_fields(request) + ('created_by__username',)
    
    
    
    admin.site.register(Book, BookAdmin)