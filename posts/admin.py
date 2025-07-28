from django.contrib import admin
from .models import Post, Attachments

class AttachmentsInline(admin.TabularInline):
    model = Attachments
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [AttachmentsInline]

admin.site.register(Attachments)