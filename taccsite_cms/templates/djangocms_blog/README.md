# TACC CMS - Templates - Plugins - DjangoCMS Blog

By default, the templates in this directory[^1] are used by _both_ the `djangocms_blog` app _and_ its plugins (that CMS users can use to add blog content to pages) in the `plugins/` directory.

More than one set of `plugins/` may exist, by _both_ adding a child directory within the `plugins/` directory _and_ updating the `BLOG_PLUGIN_TEMPLATE_FOLDERS` setting (in `settings.py`).

To learn more, read the docs:

- [Templates](https://djangocms-blog.readthedocs.io/en/latest/features/templates.html)
- [Settings](https://djangocms-blog.readthedocs.io/en/latest/settings.html)

[^1]: The origin of the templates is [`nephila/djangocms-blog`:`/djangocms_blog/templates/djangocms_blog`](https://github.com/nephila/djangocms-blog/tree/1.1.1/djangocms_blog/templates/djangocms_blog).