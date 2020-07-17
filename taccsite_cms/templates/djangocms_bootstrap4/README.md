# TACC CMS - Templates - DjangoCMS Bootstrap4 Plugins

[plugins-docs]: https://github.com/divio/djangocms-bootstrap4/blob/1.5.0/README.rst
[plugins-code]: https://github.com/divio/djangocms-bootstrap4/tree/1.5.0/djangocms_bootstrap4/contrib

This directory allows us to override _templates_ for these [plugins][plugins-docs].

## Usage

1. Copy templates from [the code of these plugins][plugins-code] to this directory. Example:
    - __from__ plugin source code
      `.../plugin_name/templates/plugin_name/template_name.html`
    - __to__   overwriting template
      `/taccsite_cms/templates/plugin_name/template_name.html`
2. Add a comment stating the version of the source template. Example:
    - __before__ `{% load i18n cms_tags %}`
    - __after__  `{# v1.5.0 #}{% load i18n cms_tags %}`

## Development

### Extend Plugin Styles

1. Decide what class to use:
    - _either_ use a plugin class
    - _or_ add a new class that uses the plugin class namespace
2. Add styles into an appropriate stylesheet at:
  `/taccsite_cms/static/site_cms/styles/_imports`

### Replace Plugin Styles

> __Notice__:
> Bootstrap plugin styles can __not__ be replaced in this manner.
> Please, overwrite Bootstrap styles, instead.

1. Copy stylesheets from plugin source code to `static/` directory. Example:
    - __from__ plugin source code
      `.../plugin_name/static/plugin_name/css/stylesheet_name.css`
    - __to__   overwriting stylesheet
      `/taccsite_cms/static/plugin_name/css/stylesheet_name.css`
2. Add a comment stating the version of the source stylesheet. Example:
    - __at top of file__ add `/* v1.5.0 */`
