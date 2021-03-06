"""Custom StreamField blocks for our apps"""
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
class TitleAndTextBlock(blocks.StructBlock):
    """Title and Text Only"""
    title = blocks.CharBlock(required=True,help_text="add your title")
    text = blocks.TextBlock(required=True,help_text="add additional text")

    class Meta:
        icon='edit'
        label='Title & Text'
        # need explicit template path
        template = "streams/title_and_text_block.html"

class RichTextBlock(blocks.RichTextBlock):
    """Full RichTextBox with all the features"""

    class Meta:
        icon='doc-full'
        label='Full RichText'
        # need explicit template path
        template = "streams/richtext_block.html"

class CardBlock(blocks.StructBlock):
    """Cards with image, Text and button"""
    title = blocks.CharBlock(required=True,help_text="add your title")
    cards=blocks.ListBlock(blocks.StructBlock(
        [
            ("image", ImageChooserBlock(required=True)),
            ("title", blocks.CharBlock(required=True,max_length=40)),
            ("text", blocks.TextBlock(required=True,max_length=200)),
            ("button_page", blocks.PageChooserBlock(required=False)),
            ("button_url", blocks.URLBlock(required=False,help_text='If the above is selected that will be used first')),
        ]
    ))
    class Meta:
        icon='placeholder'
        label='staff cards'
        # need explicit template path
        template = "streams/card_block.html"

class MessageBlock(blocks.StructBlock):
    """Image Title and a Message for Directors"""
    title = blocks.CharBlock(required=True,help_text="add your title")
    message = blocks.CharBlock(required=True)
    image = ImageChooserBlock(required=True)
    class Meta:
            icon='placeholder'
            label='Director Message'
            # need explicit template path
            template = "streams/message_block.html"

