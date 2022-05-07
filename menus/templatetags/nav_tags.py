from django import template
from wagtail.core.models import Site
from ..models import Menu

register = template.Library()

# @register.simple_tag()
# def get_navbar(slug):
#     return Menu.objects.get(slug=slug) 

@register.inclusion_tag("tags/nav_bar.html")
def get_navbar():
    site= Site.objects.get(is_default_site=True)
    home_page=site.root_page
    pages=home_page.get_siblings(inclusive=True).live().in_menu()
    return {
        "pages":pages,
    }