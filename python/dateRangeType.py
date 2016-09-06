#! /utils/dateRangeType.py

# from datetime import datetime
# from datetime import timedelta

def typeRange(year, month):
    if year and month:
        return "harian"
    elif year and not month:
        return "bulanan"
    elif not year and not month:
        return "tahunan"

def listView(typeRange):
    if typeRange == "harian":
        pass
    elif typeRange == "bulanan":
        pass
    elif typeRange == "tahunan":
        pass
