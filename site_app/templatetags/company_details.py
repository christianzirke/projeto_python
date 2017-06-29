from django import template
from googlefinance import getQuotes

register = template.Library()

@register.inclusion_tag('site_app/company_small_details.html')
def company_small_details(company):
    shares = getQuotes(company.nasdaq)
    for a in shares:
        print a;
        print;
    share = shares[0]
    print share
    return {
        "name": company.name,
        "actual_stock": share["LastTradePrice"],
        # "actual_stock": 0,
        # "stock_change": company.getActualStock().getPercentIncrement(),
        "stock_change": 0,
        "id": company.id,
        "logo": company.logo
    }
