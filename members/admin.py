from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from members.models import Member, Team, Section


class MemberAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email',
                                         ('first_name', 'last_name'),
                                         ('ja_last_name', 'ja_first_name'),
                                         'team', 'felica_idm',
                                         'executive_generation',
                                         'profile_image')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email',
                    'first_name', 'last_name',
                    'executive_generation', "team",
                    "is_staff")
    list_filter = ('is_staff', 'is_active', 'groups',
                   "executive_generation", "team")
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(Member, MemberAdmin)
admin.site.register(Team)
admin.site.register(Section)
