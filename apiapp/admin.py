from django.contrib import admin
# Register your models here.
# apiapp/admin.py → SUPER MODERN ADMIN PANEL

from django.contrib import admin
from django.utils.html import format_html
from .models import Employee, APIKey

# Custom Admin for APIKey
@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'key_preview', 'created_at', 'is_active']
    list_filter = ['created_at', 'is_active']
    search_fields = ['name', 'user__username']
    readonly_fields = ['key', 'created_at']
    
    def key_preview(self, obj):
        return format_html(f"<code style='background:#e9ecef;padding:5px;border-radius:5px;'>{obj.key[:20]}...</code>")
    key_preview.short_description = "API Key"

    def has_add_permission(self, request):
        return True

# Custom Employee Admin – BEAUTIFUL
# apiapp/admin.py → FINAL 100% WORKING VERSION (NO ERRORS!)

from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'salary', 'department')
    list_filter = ('department',)
    search_fields = ('name', 'email', 'department')
    ordering = ('-id',)
    list_per_page = 25
    
    def colored_name(self, obj):
        return format_html(f"<strong style='color:#667eea;'>{obj.name}</strong>")
    colored_name.short_description = "Name"

    def salary_formatted(self, obj):
        return format_html(f"<span style='color:green;font-weight:bold;'>${obj.salary:,}</span>")
    salary_formatted.short_description = "Salary"

    def department_badge(self, obj):
        colors = {
            'IT': '#667eea', 'HR': '#f093fb', 'Finance': '#a8e6cf', 
            'Marketing': '#ff9ff3', 'Engineering': '#54a0ff'
        }
        color = colors.get(obj.department, '#95a5a6')
        return format_html(
            f"<span style='background:{color};color:white;padding:5px 12px;border-radius:20px;font-size:11px;'>{obj.department}</span>"
        )
    department_badge.short_description = "Department"

    # Custom CSS & JS for ultra-modern look
    class Media:
        css = {"all": ("https://cdn.jsdelivr.net/npm/adminlte@3.2/dist/css/adminlte.min.css",)}
        js = ("https://cdn.jsdelivr.net/npm/adminlte@3.2/dist/js/adminlte.min.js",)