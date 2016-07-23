from django.forms import ChoiceField
from django.utils.translation import ugettext as _

from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailcore.blocks import (
    StructBlock, StreamBlock, CharBlock,
    RichTextBlock, TextBlock, FieldBlock
)


class ImageFormatBlock(FieldBlock):
    """
    The Image stream field accepts an ``alignment`` parameter that adds
    a class to the resulting image. This allows editors to place the image
    in different ways, according to the built-in CSS style.
    """
    FORMAT_CHOICES = (
        ('image-left', _('Wrap left')),
        ('image-right', _('Wrap right')),
        ('image-middle', _('Place in the center')),
        ('image-full', _('Full width')),
    )

    field = ChoiceField(choices=FORMAT_CHOICES)


class ImageBlock(StructBlock):
    """
    The ``aligned_image`` block, used to add an image into the ``BlogPage``
    """
    image = ImageChooserBlock()
    alignment = ImageFormatBlock()
    caption = RichTextBlock(required=False)


class PullQuoteBlock(StructBlock):
    """
    A block that adds a quote with the proper attribution
    """
    quote = TextBlock(label=_("Quote title"))
    attribution = CharBlock()


class VideoBlock(StructBlock):
    """
    A block that adds an embedded block for
    """
    video_link = EmbedBlock()


class BodyStreamBlock(StreamBlock):
    """
    Defines a ``StreamBlock`` with a dynamic behavior when writing the body of new pages.
    It includes:
        - h2 and h3 titles
        - a paragraph
        - an image that could be aligned on the left, on the right, in the center
          or with a full width
        - a quote with attributions
        - an embedded iframe for videos
    """
    h2 = CharBlock(icon="title")
    h3 = CharBlock(icon="title")
    paragraph = RichTextBlock(icon="pilcrow")
    image = ImageBlock(label=_("Aligned image"), icon="image")
    video = VideoBlock(label=_("Embedded video"), icon="media")
    pullquote = PullQuoteBlock(label=_("Quote"), icon="openquote")
