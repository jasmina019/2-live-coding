from django.contrib import admin

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name', 'description')