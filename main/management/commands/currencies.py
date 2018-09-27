from django.core.management.base import BaseCommand
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
from main.models import Currency,Value


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        r = requests.get("http://www.tcmb.gov.tr/kurlar/today.xml")
        r.content
        soup = BeautifulSoup(r.content, "html.parser")

        currencies = soup.tarih_date.find_all("currency")
        #import ipdb;ipdb.set_trace()
        for currency in currencies:
            obj,created = Currency.objects.get_or_create(
                code=currency.attrs.get('currencycode'),
                name=currency.find('isim').text
            )

            Value.objects.create(
                currency=obj,
                unit=currency.find('unit').text,
                buying=currency.find('forexbuying').text,
                selling=currency.find('forexselling').text if currency.find('forexselling').text else None,
                announced_at=currency.find('announced_at').text if currency.select('announced_at') else None,
            )

