from django import template

register = template.Library()

@register.filter(name='number_of_challenges')
def number_of_challenges(category):
    return category.challenges.all().count()


@register.filter(name='related_count')
def related_count(obj, related_field):
    return getattr(obj, related_field).all().count()