from django import template
from ..utils import CompanyUtils

register = template.Library()

@register.inclusion_tag('site_app/company_small_details.html')
def company_small_details(company):
    actual_stock = CompanyUtils.getActualStock([company.nasdaq])
    previous = company.getActualStock().value
    print actual_stock
    print previous
    print
    return {
        "name": company.name,
        # em array ele puxa da NASDAQ, soh o valor ele puxa da NYSE. pq????????
        "actual_stock": actual_stock,
        "stock_change": CompanyUtils.getPercentIncrement(actual_stock, previous),
        "id": company.id,
        "logo": company.logo
    }
