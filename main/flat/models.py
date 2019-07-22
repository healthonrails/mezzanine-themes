from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page
from mezzanine.utils.models import upload_to
from django.template.defaultfilters import default


class HomePage(Page, RichText):
    '''
    A page representing the format of the home page
    '''
    heading = models.CharField(max_length=400,
        help_text="The heading under the icon blurbs")
    subheading = models.CharField(max_length=400,
        help_text="The subheading just below the heading")
    featured_works_heading = models.CharField(max_length=200,
        default="Featured Works")
    featured_works_sub_heading = models.CharField(max_length=200,
                                                  default="recent research projects")
    content_heading = models.CharField(max_length=200,
        default="What We Offer")
    content_sub_heading = models.CharField(max_length=200,
                                           default="BMEII applies and validates imaging modalities")
    
    program_heading = models.CharField(max_length=200,
                                       default="OUR PROGRAMS")
    program_sub_heading = models.CharField(max_length=200,
                                           default="BMEII combines state-of-the-art facilities")

    latest_posts_heading = models.CharField(max_length=200,
        default="Latest Posts")

    class Meta:
        verbose_name = _("Home page")
        verbose_name_plural = _("Home pages")


class AsidePage(Page,RichText):
    '''
    A Page with side element customizable
    '''
    picture = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Aside.image", "asidePics"),
        format="Image", max_length=255, null=True, blank=True)
    picture_discription = models.CharField(max_length=200,null=True,
                                           blank=True)
    picture_link = models.URLField(null=True
                           ,blank=True)
    
    class Meta:
        verbose_name = _("Aside page")
        verbose_name_plural = _("Aside pages")


class AsideLink(Orderable):
    '''
    A link class for aside
    '''
    asidepage = models.ForeignKey(AsidePage,related_name="asides")
    atitle = models.CharField(max_length=200,blank=True)
    acontent = models.TextField(blank=True)
    alink = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the link will go here.") 



class Slide(Orderable):
    '''
    A slide in a slider connected to a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="slides")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Slide.image", "slider"),
        format="Image", max_length=255, null=True, blank=True)
    caption = models.CharField(max_length=200,null=True,blank=True)
    link = models.URLField(null=True
                           ,blank=True)


class IconBlurb(Orderable):
    '''
    An icon box on a HomePage
    '''
    homepage = models.ForeignKey(HomePage, related_name="blurbs")
    icon = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.IconBlurb.icon", "icons"),
        format="Image", max_length=255)
    title = models.CharField(max_length=200)
    content = models.TextField()
    link = models.CharField(max_length=2000, blank=True,
        help_text="Optional, if provided clicking the blurb will go here.")
    
    
class Service(Orderable):
    """
    A service provided by BMEII on a HomePage
    """
    homepage = models.ForeignKey(HomePage,related_name="services")
    title = models.CharField(max_length=200,
                             default="BMEII occupies approximately 20,000 square feet.")
    description = models.CharField(max_length=400,
                                   default="BMEII is responsible for coordinating \
                                    and executing all research projects")
    link = models.URLField(null=True,blank=True)
    icon = models.CharField(max_length=100,
                            default="icon-globe icon-medium")
    

class Program(Orderable):
    '''
    A Program at BMEII on a HomePage
    '''
    homepage = models.ForeignKey(HomePage,related_name="programs")
    image = FileField(verbose_name=_("Image"),
        upload_to=upload_to("theme.Program.image", "program"),
        format="Image", max_length=255, null=True, blank=True)
    title = models.CharField(max_length=200,
                             default="BMEII Imaging")
    description = models.CharField(max_length=200,
                                   default="BMEII programs at Mount Sinai")
    link = models.URLField(null=True,blank=True)
