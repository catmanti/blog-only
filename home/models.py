from django.db import models
from streams import blocks
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel,StreamFieldPanel,MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index


class HomePage(Page):
    is_creatable = False

class BlogIndexPage(Page):
    """For pages like About page Directors massage"""
    parent_page_types = ['HomePage']
    subpage_types = ['BlogArticlePage']
    content = StreamField([
        ('title_and_text',blocks.TitleAndTextBlock()),
        ('full_richtext',blocks.RichTextBlock()),
        ("message",blocks.MessageBlock()),
        ],null=True,blank=True)
    # blog_image = models.ForeignKey("wagtailimages.Image",blank=True,null=True, related_name="+", on_delete=models.SET_NULL,)
        
    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
        # ImageChooserPanel("blog_image"),
    ]


class BlogAuthorsOrderable(Orderable):
    """
    This allow us to select one or more authors from snippets (BlogAuthor)
    With ParentalKey it relate with BlogArticlePage model so that one article 
    can have many authors 
    """
    page= ParentalKey("home.BlogArticlePage", related_name="blog_authors")
    author = models.ForeignKey("home.BlogAuthor", on_delete=models.CASCADE)

    panels=[
       SnippetChooserPanel("author") 
    ]



class BlogAuthor(models.Model):
    """Authors for our Blog post maybe many aurthors for one post"""
    name=models.CharField(max_length=100)
    website=models.URLField(null=True,blank=True)
    image=models.ForeignKey("wagtailimages.Image", on_delete=models.SET_NULL,null=True,blank=False,related_name="+")

    panels=[
        MultiFieldPanel([
            FieldPanel("name"),
            ImageChooserPanel("image")
        ],heading="Name & Image",
        ),
        MultiFieldPanel([
            FieldPanel("website"),
        ],heading="Links")
    ]

    def __str__(self):
        return self.name
# add or relate this class with Wagtail admin
register_snippet(BlogAuthor)    

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
        MultiFieldPanel([
           InlinePanel("blog_authors",label="Author",max_num=3,min_num=1) 
        ],heading="Author(s)"),
        StreamFieldPanel('content'),
        ImageChooserPanel("blog_image"),
        FieldPanel('body', classname="full"),
    ]

