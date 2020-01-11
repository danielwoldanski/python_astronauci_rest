from django.contrib import admin


from django.utils.translation import gettext_lazy as _
from astronauts.models import Astronaut

admin.site.site_header = _('AstronautsBook')
admin.site.index_title = _('Dashboards')


@admin.register(Astronaut)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth']
    list_display_links = ['first_name', 'last_name']
    ordering = ['first_name', 'last_name']
    search_fields = ['^last_name']

    fieldsets = [
        (None, {'fields': ['first_name', 'last_name']}),
        (_('Personal data'), {'fields': ['date_of_birth']}),
        (_('Other'), {'fields': ['homepage']}),
    ]

    def field_born_in_90(self, model):
        if model.date_of_birth:
            return model.date_of_birth.strftime('%Y')[:3] == "199"

    field_born_in_90.boolean = True

    class Media:
        js = [
            'astronauts/astronaut.js'
        ]
        css = {'all': [
            'astronauts/astronaut.css'
        ]}
