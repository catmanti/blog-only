"""Custom StreamField blocks for our apps"""
from wagtail.core import blocks

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