# Static Articles

## Intention

Support static addition of news articles that originate from a Core news site.

A [dynamic solution that pulls form the Core news site](https://github.com/TACC/Core-CMS/issues/69) is preferable.

But this is not available due to constrainst of architecture, time, or ability.

## Architectural Decisions

## Add Image via Child Plugin Instead of Via Fields

Ideally, the image fields are in the plugin, not a child plugin.

Wesley failed to achieve that functionality:
1. Build model so it extends `AbstractPicture` from `djangocms-picture`.
2. Tweak model to sweep bugs under the rug.
3. Quit when he was unable to resolve the error,
    `TaccsiteStaticNewsArticlePreview has no field named 'cmsplugin_ptr_id'`
    upon saving a plugin instance.
4. Learn that he [should not try to reduce `AbstractPicture`](https://stackoverflow.com/a/3674714/11817077).

This is the relevant code he abandoned:
```python
from djangocms_picture.models import AbstractPicture

# To allow user to not set image
# FAQ: Emptying the clean() method avoids picture validation
# SEE: https://github.com/django-cms/djangocms-picture/blob/3.0.0/djangocms_picture/models.py#L278
def skip_image_validation():
    pass

class TaccsiteStaticNewsArticlePreview(AbstractPicture):
    #
    # …
    #

    # Remove error-prone attribute from parent class
    # FAQ: Avoid error when running `makemigrations`:
    #      "You are trying to add a non-nullable field 'cmsplugin_ptr' […]"
    # SEE: https://github.com/django-cms/djangocms-picture/blob/3.0.0/djangocms_picture/models.py#L212
    # SEE: https://github.com/django-cms/djangocms-picture/blob/3.0.0/djangocms_picture/models.py#L234
    cmsplugin_ptr = None

    class Meta:
        abstract = False

    def clean(self):
        skip_image_validation()
```