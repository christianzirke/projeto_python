from django import template

register = template.Library()

@register.inclusion_tag('site_app/company_small_details.html')
def company_small_details(company):
    return {
        "name": company.name,
        # "actual_stock": company.getActualStock().value,
        "actual_stock": 0,
        # "stock_change": company.getActualStock().getPercentIncrement(),
        "stock_change": 0,
        "id": company.id,
        "logo": company.logo
    }
