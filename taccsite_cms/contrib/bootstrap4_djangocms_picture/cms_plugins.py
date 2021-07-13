# Re-register unregistered PicturePlugin without uninstalling Bootstrap4's
# FAQ: A Bootstrap picture has superfluous options that are not always desirable
# TODO: Drop try/except & load non-standard plugin set for migrated legacy sites
# FAQ: If we can import both plugins, then re-register PicturePlugin
#      (because Bootstrap4Picture unregistered PicturePlugin)
try:
    from cms.plugin_pool import plugin_pool
    from djangocms_picture.cms_plugins import PicturePlugin
    from djangocms_bootstrap4.contrib.bootstrap4_picture.cms_plugins import Bootstrap4PicturePlugin

    # SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/master/djangocms_bootstrap4/contrib/bootstrap4_picture/cms_plugins.py#L54
    plugin_pool.register_plugin(PicturePlugin)
# CAVEAT: If plugins exist but import statement is inaccurate... silent failure
except ImportError:
    pass
