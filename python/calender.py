#! /utils/calender.py
import json, pprint

def get_month(month):
    if month == "01":
        value = "January"
    elif month == "02":
        value = "February"
    elif month == "03":
        value = "March"
    elif month == "04":
        value = "April"
    elif month == "05":
        value = "May"
    elif month == "06":
        value = "June"
    elif month == "07":
        value = "July"
    elif month == "08":
        value = "August"
    elif month == "09":
        value = "September"
    elif month == "10":
        value = "October"
    elif month == "11":
        value = "November"
    elif month == "12":
        value = "December"
    else:
        value = "Invalid Month"

    return value

def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

def days(month,leap_year):
    if month == "01":
        value = 31
    elif month == "02":
        if leap_year == True:
            value = 29
        else:
            value = 28
    elif month == "03":
        value = 31
    elif month == "04":
        value = 30
    elif month == "05":
        value = 31
    elif month == "06":
        value = 30
    elif month == "07":
        value = 31
    elif month == "08":
        value = 31
    elif month == "09":
        value = 30
    elif month == "10":
        value = 31
    elif month == "11":
        value = 30
    elif month == "12":
        value = 31
    else:
        value = 0

    return value

def get_day(year, month):
    rows = {}
    leap_status = leap_year(year)
    user_month  = "%s" % month
    get_days    = days(user_month, leap_status)
    rows['data']=[]
    for day in range(0, get_days):
        hari    = day + 1
        tanggal = '%02d' % hari
        rows['data'].append({
				"tanggal": tanggal,
			})
    # bulan       = get_month(user_month)
    # rows['bulan']   = bulan
    # rows['tahun']   = year
    # pprint.pprint(json.dumps(rows))
    return json.dumps(rows)
