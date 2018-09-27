from django.shortcuts import render,HttpResponse
from .models import Currency,Value
from django.db.models import OuterRef, Subquery
from django.http import JsonResponse

def get_main(request):
    data = []
    obj =Value.objects.filter(currency =OuterRef("pk")).order_by("-announced_at")
    currencies = Currency.objects.all().annotate(
        new_forex_selling = Subquery(obj.values("selling")[:1]),
        new_unit = Subquery(obj.values("unit")[:1]),
        new_forex_buying = Subquery(obj.values("buying")[:1]),
    )
    for currency in currencies:
        data.append(
            {
                'name':currency.name,
                'code':currency.code,
                'selling':currency.new_forex_selling,
                'unit':currency.new_unit,
                'buying':currency.new_forex_buying,
            }
        )

    return JsonResponse(data, safe=False)









