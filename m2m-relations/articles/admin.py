from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Сategory, Membership


class MembershipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter=0
        for form in self.forms:
            if len(form.cleaned_data) != 0:
                if  form.cleaned_data['is_main']:
                    counter+=1
        if counter > 1:
            raise ValidationError('Основной раздел может быть только один')
        elif counter == 0:
            raise ValidationError('Укажите основной раздел')
        else:
            pass
        return super().clean()


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 3
    formset = MembershipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'published_at')
    list_display_links = ('id','title')
    inlines = (MembershipInline,)

@admin.register(Сategory)
class СategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = (MembershipInline,)

@admin.register(Membership)
class MembershipInline(admin.ModelAdmin):
    list_display = ('article', 'tag', 'is_main')
    pass
