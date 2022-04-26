from django.db import models
from streams import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class HomePage(Page):
    is_creatable = False

class BlogIndexPage(Page):
    """Blog Listings Page"""
    parent_page_types = ['HomePage']
    subpage_types = ['BlogArticlePage']

class BlogArticlePage(Page):
    """Blog Articles"""
    parent_page_types = ['BlogIndexPage']
    subpage_types = []
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    content = StreamField([
        ('title_and_text',blocks.TitleAndTextBlock()),
        ('full_richtext',blocks.RichTextBlock()),
        ("cards",blocks.CardBlock()),
        ],null=True,blank=True)

    blog_image = models.ForeignKey("wagtailimages.Image",blank=False,null=True, related_name="+", on_delete=models.SET_NULL,)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        StreamFieldPanel('content'),
        ImageChooserPanel("blog_image"),
        FieldPanel('body', classname="full"),
    ]

