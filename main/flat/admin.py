from django.contrib import admin

# Register your models here.
from mezzanine.core.admin import TabularDynamicInlineAdmin 
from mezzanine.pages.admin import PageAdmin
# Register your models here.
from .models import (HomePage,IconBlurb,
                    Slide,Service,Program,
                    AsideLink,AsidePage)

class SlideInline(TabularDynamicInlineAdmin):
    model = Slide
    

class IconBlurbline(TabularDynamicInlineAdmin):
    model = IconBlurb
    
class ServiceInline(TabularDynamicInlineAdmin):
    model = Service
    
class ProgramInline(TabularDynamicInlineAdmin):
    model = Program
    
class AsideLinkInline(TabularDynamicInlineAdmin):
    model = AsideLink
    
class AsidePageAdmin(PageAdmin):
    inlines = (AsideLinkInline,)

class HomePageAdmin(PageAdmin):
    inlines = (SlideInline,ServiceInline,IconBlurbline,ProgramInline)


admin.site.register(HomePage, HomePageAdmin)
admin.site.register(AsidePage,AsidePageAdmin)
