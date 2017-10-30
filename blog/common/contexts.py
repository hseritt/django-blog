"""A context module for common app.
"""

from blog.settings import THEME
from common.models import (
    PageElement, SiteLink, RecommendedLink, SocialMediaLink
)
from posts.models import Category


def get_common_view_context():
    """Returns view context for common app views.
    """
    tag_line = PageElement.objects.get(name='Tag Line', is_visible=True)
    footer_text = PageElement.objects.get(name='Footer Text', is_visible=True)

    category_list = Category.objects.filter(
        display=True, post__is_published=True
    ).distinct().order_by('name')
    site_link_list = SiteLink.objects.filter(is_visible=True)
    recommended_link_list = RecommendedLink.objects.filter(is_visible=True)
    social_media_link_list = SocialMediaLink.objects.filter(is_visible=True)

    common_view_context = {
        'category_list': category_list,
        'footer_text': footer_text,
        'recommended_link_list': recommended_link_list,
        'site_link_list': site_link_list,
        'social_media_link_list': social_media_link_list,
        'tag_line': tag_line,
        'theme': THEME,
    }

    return common_view_context
