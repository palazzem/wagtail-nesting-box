from django.contrib.contenttypes.models import ContentType

from model_mommy.recipe import Recipe, seq, foreign_key

from wagtail_box.blog.models import Blog, Post


content_type = Recipe(ContentType,
    app_label='blog',
)

blog = Recipe(Blog,
    content_type=foreign_key(content_type),
    title=seq('Blog '),
    slug=seq('blog-'),
)

post = Recipe(Post,
    content_type=foreign_key(content_type),
    title=seq('Post '),
    slug=seq('post-'),
    body=[],
)
