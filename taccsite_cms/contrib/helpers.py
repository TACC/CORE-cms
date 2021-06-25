from datetime import date



# SEE: https://github.com/django-cms/djangocms-bootstrap4/blob/master/djangocms_bootstrap4/helpers.py
def concat_classnames(classes):
    """Concatenates a list of classes (without failing on None)"""
    # SEE: https://stackoverflow.com/a/20271297/11817077
    return ' '.join(_class for _class in classes if _class)



# SEE: https://newbedev.com/how-to-insert-multiple-elements-into-a-list
def insert_at_position(position, list, list_to_insert):
    """Insert list at position within another list"""
    return list[:position] + list_to_insert + list[position:]



# SEE: https://stackoverflow.com/a/32237949/11817077
def get_nearest(items, pivot):
    """Get nearest date (or other arithmatic value)"""
    return min(items, key=lambda x: abs(x - pivot))




# HELP: Can this logic be less verbose?
# HELP: Is the `preferred_time_period` parameter effectual?
def which_date_is_nearest_today(date_a, date_b, preferred_time_period):
    """
    Returns whether each date is today or nearest today, and whether nearest date is past or today or future.

    Only two dates are supported. You may prefer 'future' or 'past' date(s).

    If both dates are the same date, then both are reported as True.

    :param datetime date_a: a date "A" to compare
    :param datetime date_b: a date "B" to compare
    :param str preferred_time_period: whether to prefer 'future' or 'past' dates

    :returns:
        A tuple of tuples:
        (
            ``boolean`` of whether ``date_a`` is nearest,
            ``string`` of ``date_a`` time period ``past``/``today``/``future``
        ),
        (
            ``boolean`` of whether ``date_b`` is nearest,
            ``string`` of ``date_b`` time period ``past``/``today``/``future``
        ),
    :rtype: tuple
    """
    today = date.today()
    is_a = False
    is_b = False
    a_time_period = 'today'
    b_time_period = 'today'

    # Match preferred time

    if today in {date_a, date_b}:
        is_a = True
        is_b = True
        a_time_period = 'today'
        b_time_period = 'today'

    elif preferred_time_period == 'future':
        is_a = date_a and date_a >= today
        is_b = date_b and date_b >= today
        if is_a: a_time_period = 'future'
        if is_b: b_time_period = 'future'
        if not is_a and not is_b:
            is_a = date_a and date_a < today
            is_b = date_b and date_b < today
            if is_a: a_time_period = 'past'
            if is_b: b_time_period = 'past'

    elif preferred_time_period == 'past':
        is_a = date_a and date_a < today
        is_b = date_b and date_b < today
        if is_a: a_time_period = 'past'
        if is_b: b_time_period = 'past'
        if not is_a and not is_b:
            is_a = date_a and date_a >= today
            is_b = date_b and date_b >= today
            if is_a: a_time_period = 'future'
            if is_b: b_time_period = 'future'

    # Show nearest date
    if is_a and is_b and date_a != date_b:
        nearest_date = get_nearest((date_a, date_b), today)

        if date_a == nearest_date:
            is_b = False
        if date_b == nearest_date:
            is_a = False

    return ((is_a, a_time_period), (is_b, b_time_period))



# SEE: https://github.com/django-cms/django-cms/issues/5102#issuecomment-597150141

from django.shortcuts import render
from cms.plugin_base import CMSPluginBase

class CMSPluginBaseWithMaxChildren(CMSPluginBase):
    """
    Extension of `CMSPluginBase` that allows setting maximum amount of nested/child plugins. Usage:

    1. Extend this class (instead of `CMSPluginBase`)
    2. Set `max_children` to desired limit.
    """

    max_children = None

    def add_view(self,request, form_url='', extra_context=None):

        if self.max_children:
            # FAQ: Placeholders do not have a parent, only plugins do
            if self._cms_initial_attributes['parent']:
                num_allowed = len([v for v in self._cms_initial_attributes['parent'].get_children() if v.get_plugin_instance()[0] is not None])
            else:
                num_allowed = len([v for v in self.placeholder.get_plugins() if v.get_plugin_instance()[0] is not None and v.get_plugin_name() == self.name])

            if num_allowed >= self.max_children:
                return render(request , "path/to/your/max_reached_template.html", {
                    'max_children': self.max_children,
                })
        return super(CMSPluginBaseWithMaxChildren, self).add_view(request, form_url, extra_context)
