from django import template

register = template.Library()

@register.inclusion_tag('site_app/company_small_details.html')
def company_small_details(company):
    print(company)
    return {
        "name": company.name,
        "actual_stock": company.getActualStock().value,
        "stock_change": company.getActualStock().getPercentIncrement(),
        "id": company.id
    }
