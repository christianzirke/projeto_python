import datetime
from pandas_datareader import data as pandata
from .models import CompanyStockValue

class CompanyUtils(object):
    @staticmethod
    def updateShares(company):
        stock = company.getActualStock()
        previous = None
        # Se a data do ultimo valor no banco for anterior ao dia de hoje, tenta buscar dados novos
        if not stock:
            start = datetime.datetime(2017, 1, 1)
            end = datetime.date.today()
        elif stock.date.date() < datetime.date.today():
            # Adiciona um dia ao dia do ultimo registro
            start = stock.date + datetime.timedelta(days=1)
            previous = stock

        end = datetime.date.today()
        share_data = pandata.DataReader(company.nasdaq, "google", start, end)
        share_data.reset_index(inplace=True,drop=False)

        for i in range(len(share_data)):
            start_date = share_data["Date"][i]
            open_date = datetime.datetime.combine(start_date, datetime.time(9, 30))
            close_date = datetime.datetime.combine(start_date, datetime.time(16))
            previous = CompanyStockValue.objects.create(company=company, value=share_data["Open"][i], date=open_date, previous=previous)
            previous = CompanyStockValue.objects.create(company=company, value=share_data["Close"][i], date=close_date, previous=previous)
