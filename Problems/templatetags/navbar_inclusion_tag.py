from django import template
from Problems.models import ProblemSet
from django.core.urlresolvers import resolve, Resolver404

register = template.Library()

@register.inclusion_tag('Problems/navbar_inclusion_tag.html', takes_context = True)
def navbar_inclusion_tag(context):
    ps = ProblemSet.objects.all()
    return {'problem_sets': ps, 'request': context.request }

@register.simple_tag
def check_active(request, view_name):
    if not request:
        return ''
    try:
        if view_name in resolve(request.path_info).url_name:
            return 'active'
        else:
            return ''
    except Resolver404:
        return ''

@register.filter
def num2diff(value):
    # Takes a number {1,2,3,4} and returns {easy,med,hard,imp}
    if value == 1:
        return "Easy"
    elif value == 2:
        return "Medium"
    elif value == 3:
        return "Hard"
    elif value == 4:
        return "Bonus"
    else:
        return ""
