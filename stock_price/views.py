import pandas as pd
import numpy as np
from django.shortcuts import render
from pandas import Series, DataFrame
import base64
import requests
from .models import *
from .forms import *
from config import settings
import pandas_datareader.data as web
import datetime

import matplotlib

matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
from django.http import HttpResponse

from datetime import datetime
from datetime import timedelta

import tempfile
import os

from fractions import Fraction
from datetime import datetime as dt

start = '1997-1-1'

nikkei_data = web.DataReader("^N225", "yahoo", start)
nikkei_data = nikkei_data.round(1)

sp500_data = web.DataReader("^GSPC", "yahoo", start)
sp500_data = sp500_data.round(1)

usdjpy_data = web.DataReader("JPY=X", "yahoo", start)
usdjpy_data = usdjpy_data.round(1)

bitcoin_data = web.DataReader("BTC-USD", "yahoo", start)
bitcoin_data = bitcoin_data.round(1)


def index(request):
    return render(request, 'stock_price/index.html')

for date, high, low, open, close, volume in zip(nikkei_data.index, nikkei_data['High'], nikkei_data['Low'], nikkei_data['Open'], nikkei_data['Close'], nikkei_data['Volume']):
    nikkei_model = NIKKEI.objects.update_or_create(date=date,high=high,low=low,open=open,close=close,volume=volume)

for date, high, low, open, close, volume in zip(sp500_data.index, sp500_data['High'], sp500_data['Low'], sp500_data['Open'], sp500_data['Close'], sp500_data['Volume']):
    sp500_model = SP500.objects.update_or_create(date=date,high=high,low=low,open=open,close=close,volume=volume)

for date, high, low, open, close, volume in zip(usdjpy_data.index, usdjpy_data['High'], usdjpy_data['Low'], usdjpy_data['Open'], usdjpy_data['Close'], usdjpy_data['Volume']):
    usdjpy_model = USDJPY.objects.update_or_create(date=date,high=high,low=low,open=open,close=close,volume=volume)

for date, high, low, open, close, volume in zip(bitcoin_data.index, bitcoin_data['High'], bitcoin_data['Low'], bitcoin_data['Open'], bitcoin_data['Close'], bitcoin_data['Volume']):
    bitcoin_model = BITCOIN.objects.update_or_create(date=date,high=high,low=low,open=open,close=close,volume=volume)

for date, sp500 in zip(sp500_data.index, sp500_data['Close']):
    common_model = COMMON.objects.update_or_create(date=date,sp500=sp500)

for date, bitcoin in zip(bitcoin_data.index, bitcoin_data['Close']):
    common_model = COMMON(date=date,bitcoin=bitcoin)
    common_model.save()

common_model = COMMON.objects.all().delete()

nikkei_dataframe = pd.DataFrame(list(NIKKEI.objects.all().values()))
nikkei_processing = pd.DataFrame(nikkei_dataframe)

sp500_dataframe = pd.DataFrame(list(SP500.objects.all().values()))
sp500_processing = pd.DataFrame(sp500_dataframe)

usdjpy_dataframe = pd.DataFrame(list(USDJPY.objects.all().values()))
usdjpy_processing = pd.DataFrame(usdjpy_dataframe)

bitcoin_dataframe = pd.DataFrame(list(BITCOIN.objects.all().values()))
bitcoin_processing = pd.DataFrame(bitcoin_dataframe)


#日経225
nikkei_close = nikkei_processing["close"]
nikkei_close = nikkei_close.values.tolist()
nikkei_date = nikkei_processing.index
nikkei_date = nikkei_date.tolist()

#SP500
sp500_close = sp500_processing["close"]
sp500_close = sp500_close.values.tolist()
sp500_date = sp500_processing.index
sp500_date = sp500_date.tolist()

#USD/JPY
usdjpy_close = usdjpy_processing["close"]
usdjpy_close = usdjpy_close.values.tolist()
usdjpy_date = usdjpy_processing.index
usdjpy_date = usdjpy_date.tolist()

#bit-coin
bitcoin_close = bitcoin_processing["close"]
bitcoin_close = bitcoin_close.values.tolist()
bitcoin_date = bitcoin_processing.index
bitcoin_date = bitcoin_date.tolist()


# 日経225 表・検索
def nikkei(request):
    search_date_start = '1997-1-1'
    search_date_end = '2021-1-1'

    if (request.method == 'POST'):
        form_start = StartDateForm(request.POST)
        form_end = EndDateForm(request.POST)
        search_date_start = request.POST['date_search_start']
        search_date_end = request.POST['date_search_end']
        result_data = NIKKEI.objects.filter(date__range=[search_date_start,search_date_end]).values()
        start_datetime = dt.strptime(search_date_start, '%Y-%m-%d')
        end_datetime = dt.strptime(search_date_end, '%Y-%m-%d')
    else:
        form_start = StartDateForm()
        form_end = EndDateForm()
        result_data = NIKKEI.objects.all().values()
        start_datetime = dt.strptime('1997-01-01', '%Y-%m-%d')
        end_datetime = dt.strptime('2021-01-01', '%Y-%m-%d')

    if start_datetime > end_datetime:
        count_data = 0

    else:
        nikkei_processing = pd.DataFrame(result_data)
        nikkei_close = nikkei_processing["close"]
        nikkei_close = nikkei_close.values.tolist()
        nikkei_date = nikkei_processing["date"]
        nikkei_date = nikkei_date.values.tolist()
        count_data = len(nikkei_close)

        if count_data < 15 :
            pass

        else:
            unit_1 = Fraction(1, 14)
            unit_2 = Fraction(2, 14)
            unit_3 = Fraction(3, 14)
            unit_4 = Fraction(4, 14)
            unit_5 = Fraction(5, 14)
            unit_6 = Fraction(6, 14)
            unit_7 = Fraction(7, 14)
            unit_8 = Fraction(8, 14)
            unit_9 = Fraction(9, 14)
            unit_10 = Fraction(10, 14)
            unit_11 = Fraction(11, 14)
            unit_12 = Fraction(12, 14)
            unit_13 = Fraction(13, 14)

            float1 = float(unit_1 * count_data)
            float2 = float(unit_2 * count_data)
            float3 = float(unit_3 * count_data)
            float4 = float(unit_4 * count_data)
            float5 = float(unit_5 * count_data)
            float6 = float(unit_6 * count_data)
            float7 = float(unit_7 * count_data)
            float8 = float(unit_8 * count_data)
            float9 = float(unit_9 * count_data)
            float10 = float(unit_10 * count_data)
            float11 = float(unit_11 * count_data)
            float12 = float(unit_12 * count_data)
            float13 = float(unit_13 * count_data)

            rounding1 = round(float1)
            rounding2 = round(float2)
            rounding3 = round(float3)
            rounding4 = round(float4)
            rounding5 = round(float5)
            rounding6 = round(float6)
            rounding7 = round(float7)
            rounding8 = round(float8)
            rounding9 = round(float9)
            rounding10 = round(float10)
            rounding11 = round(float11)
            rounding12 = round(float12)
            rounding13 = round(float13)

            date1 = nikkei_date[rounding1]
            date2 = nikkei_date[rounding2]
            date3 = nikkei_date[rounding3]
            date4 = nikkei_date[rounding4]
            date5 = nikkei_date[rounding5]
            date6 = nikkei_date[rounding6]
            date7 = nikkei_date[rounding7]
            date8 = nikkei_date[rounding8]
            date9 = nikkei_date[rounding9]
            date10 = nikkei_date[rounding10]
            date11 = nikkei_date[rounding11]
            date12 = nikkei_date[rounding12]
            date13 = nikkei_date[rounding13]

            plt.figure(figsize=(10, 7)).add_subplot(xticks=[0,
                                                            float1,
                                                            float2,
                                                            float3,
                                                            float4,
                                                            float5,
                                                            float6,
                                                            float7,
                                                            float8,
                                                            float9,
                                                            float10,
                                                            float11,
                                                            float12,
                                                            float13,
                                                            count_data],
                                                    xticklabels=[search_date_start,
                                                                 date1,
                                                                 date2,
                                                                 date3,
                                                                 date4,
                                                                 date5,
                                                                 date6,
                                                                 date7,
                                                                 date8,
                                                                 date9,
                                                                 date10,
                                                                 date11,
                                                                 date12,
                                                                 date13,
                                                                 search_date_end])
            plt.plot(nikkei_close, color='#00d5ff', label="NIKKEI")
            plt.xlim(0, count_data)
            plt.ylim(0, 35000)
            plt.subplots_adjust(bottom=0.2)
            plt.xticks(rotation=90)
            plt.grid(which="major", axis="x", color="#484848", alpha=0.8,
                    linestyle="--", linewidth=1)

            plt.grid(which="major", axis="y", color="#484848", alpha=0.8,
                    linestyle="--", linewidth=1)

            plt.xlabel("Date")
            plt.ylabel("Close")
            plt.savefig("static/tmp/nikkei_image.png")

    count_verification = count_data

    if count_verification < 15:
        msg = "日付範囲が短いのでグラフにデータを反映することができません"

    else:
        msg = ""

    context = {
        'msg': msg,
        'record':result_data,
        'form_start': form_start,
        'form_end': form_end,
        'start_date': search_date_start,
        'end_date': search_date_end,

    }

    return render(request,'stock_price/nikkei.html',context)

# SP500 表・検索
def sp500(request):
    search_date_start = '1997-1-1'
    search_date_end = '2021-1-1'

    if (request.method == 'POST'):
        form_start = StartDateForm(request.POST)
        form_end = EndDateForm(request.POST)
        search_date_start = request.POST['date_search_start']
        search_date_end = request.POST['date_search_end']
        result_data = SP500.objects.filter(date__range=[search_date_start,search_date_end]).values()
        start_datetime = dt.strptime(search_date_start, '%Y-%m-%d')
        end_datetime = dt.strptime(search_date_end, '%Y-%m-%d')
    else:
        form_start = StartDateForm()
        form_end = EndDateForm()
        result_data = SP500.objects.all().values()
        start_datetime = dt.strptime('1997-01-01', '%Y-%m-%d')
        end_datetime = dt.strptime('2021-01-01', '%Y-%m-%d')

    if start_datetime > end_datetime:
        count_data = 0

    else:
        sp500_processing = pd.DataFrame(result_data)
        sp500_close = sp500_processing["close"]
        sp500_close = sp500_close.values.tolist()
        sp500_date = sp500_processing["date"]
        sp500_date = sp500_date.values.tolist()
        count_data = len(sp500_close)

        if count_data < 15 :
            pass

        else:
            unit_1 = Fraction(1, 14)
            unit_2 = Fraction(2, 14)
            unit_3 = Fraction(3, 14)
            unit_4 = Fraction(4, 14)
            unit_5 = Fraction(5, 14)
            unit_6 = Fraction(6, 14)
            unit_7 = Fraction(7, 14)
            unit_8 = Fraction(8, 14)
            unit_9 = Fraction(9, 14)
            unit_10 = Fraction(10, 14)
            unit_11 = Fraction(11, 14)
            unit_12 = Fraction(12, 14)
            unit_13 = Fraction(13, 14)

            float1 = float(unit_1 * count_data)
            float2 = float(unit_2 * count_data)
            float3 = float(unit_3 * count_data)
            float4 = float(unit_4 * count_data)
            float5 = float(unit_5 * count_data)
            float6 = float(unit_6 * count_data)
            float7 = float(unit_7 * count_data)
            float8 = float(unit_8 * count_data)
            float9 = float(unit_9 * count_data)
            float10 = float(unit_10 * count_data)
            float11 = float(unit_11 * count_data)
            float12 = float(unit_12 * count_data)
            float13 = float(unit_13 * count_data)

            rounding1 = round(float1)
            rounding2 = round(float2)
            rounding3 = round(float3)
            rounding4 = round(float4)
            rounding5 = round(float5)
            rounding6 = round(float6)
            rounding7 = round(float7)
            rounding8 = round(float8)
            rounding9 = round(float9)
            rounding10 = round(float10)
            rounding11 = round(float11)
            rounding12 = round(float12)
            rounding13 = round(float13)

            date1 = sp500_date[rounding1]
            date2 = sp500_date[rounding2]
            date3 = sp500_date[rounding3]
            date4 = sp500_date[rounding4]
            date5 = sp500_date[rounding5]
            date6 = sp500_date[rounding6]
            date7 = sp500_date[rounding7]
            date8 = sp500_date[rounding8]
            date9 = sp500_date[rounding9]
            date10 = sp500_date[rounding10]
            date11 = sp500_date[rounding11]
            date12 = sp500_date[rounding12]
            date13 = sp500_date[rounding13]

            plt.figure(figsize=(10, 7)).add_subplot(xticks=[0,
                                                            float1,
                                                            float2,
                                                            float3,
                                                            float4,
                                                            float5,
                                                            float6,
                                                            float7,
                                                            float8,
                                                            float9,
                                                            float10,
                                                            float11,
                                                            float12,
                                                            float13,
                                                            count_data],
                                                    xticklabels=[search_date_start,
                                                                 date1,
                                                                 date2,
                                                                 date3,
                                                                 date4,
                                                                 date5,
                                                                 date6,
                                                                 date7,
                                                                 date8,
                                                                 date9,
                                                                 date10,
                                                                 date11,
                                                                 date12,
                                                                 date13,
                                                                 search_date_end])
            plt.plot(sp500_close, color='#00d5ff', label="SP500")
            plt.xlim(0, count_data)
            plt.ylim(0, 5000)
            plt.subplots_adjust(bottom=0.2)
            plt.xticks(rotation=90)
            plt.grid(which="major", axis="x", color="#484848", alpha=0.8,
                    linestyle="--", linewidth=1)

            plt.grid(which="major", axis="y", color="#484848", alpha=0.8,
                    linestyle="--", linewidth=1)

            plt.xlabel("Date")
            plt.ylabel("Close")
            plt.savefig("static/tmp/sp500_image.png")

    count_verification = count_data

    if count_verification < 15:
        msg = "日付範囲が短いのでグラフにデータを反映することができません"

    else:
        msg = ""

    context = {
        'msg': msg,
        'record':result_data,
        'form_start': form_start,
        'form_end': form_end,
        'start_date': search_date_start,
        'end_date': search_date_end,

    }

    return render(request,'stock_price/sp500.html',context)

# USD/JPY 表・検索
def usdjpy(request):
    search_date_start = '1997-1-1'
    search_date_end = '2021-1-1'

    if (request.method == 'POST'):
        form_start = StartDateForm(request.POST)
        form_end = EndDateForm(request.POST)
        search_date_start = request.POST['date_search_start']
        search_date_end = request.POST['date_search_end']
        result_data = USDJPY.objects.filter(date__range=[search_date_start,search_date_end]).values()
        start_datetime = dt.strptime(search_date_start, '%Y-%m-%d')
        end_datetime = dt.strptime(search_date_end, '%Y-%m-%d')
    else:
        form_start = StartDateForm()
        form_end = EndDateForm()
        result_data = USDJPY.objects.all().values()
        start_datetime = dt.strptime('1997-01-01', '%Y-%m-%d')
        end_datetime = dt.strptime('2021-01-01', '%Y-%m-%d')

    if start_datetime > end_datetime:
        count_data = 0

    else:
        usdjpy_processing = pd.DataFrame(result_data)
        usdjpy_close = usdjpy_processing["close"]
        usdjpy_close = usdjpy_close.values.tolist()
        usdjpy_date = usdjpy_processing["date"]
        usdjpy_date = usdjpy_date.values.tolist()
        count_data = len(usdjpy_close)

        if count_data < 15 :
            pass

        else:
            unit_1 = Fraction(1, 14)
            unit_2 = Fraction(2, 14)
            unit_3 = Fraction(3, 14)
            unit_4 = Fraction(4, 14)
            unit_5 = Fraction(5, 14)
            unit_6 = Fraction(6, 14)
            unit_7 = Fraction(7, 14)
            unit_8 = Fraction(8, 14)
            unit_9 = Fraction(9, 14)
            unit_10 = Fraction(10, 14)
            unit_11 = Fraction(11, 14)
            unit_12 = Fraction(12, 14)
            unit_13 = Fraction(13, 14)

            float1 = float(unit_1 * count_data)
            float2 = float(unit_2 * count_data)
            float3 = float(unit_3 * count_data)
            float4 = float(unit_4 * count_data)
            float5 = float(unit_5 * count_data)
            float6 = float(unit_6 * count_data)
            float7 = float(unit_7 * count_data)
            float8 = float(unit_8 * count_data)
            float9 = float(unit_9 * count_data)
            float10 = float(unit_10 * count_data)
            float11 = float(unit_11 * count_data)
            float12 = float(unit_12 * count_data)
            float13 = float(unit_13 * count_data)

            rounding1 = round(float1)
            rounding2 = round(float2)
            rounding3 = round(float3)
            rounding4 = round(float4)
            rounding5 = round(float5)
            rounding6 = round(float6)
            rounding7 = round(float7)
            rounding8 = round(float8)
            rounding9 = round(float9)
            rounding10 = round(float10)
            rounding11 = round(float11)
            rounding12 = round(float12)
            rounding13 = round(float13)

            date1 = usdjpy_date[rounding1]
            date2 = usdjpy_date[rounding2]
            date3 = usdjpy_date[rounding3]
            date4 = usdjpy_date[rounding4]
            date5 = usdjpy_date[rounding5]
            date6 = usdjpy_date[rounding6]
            date7 = usdjpy_date[rounding7]
            date8 = usdjpy_date[rounding8]
            date9 = usdjpy_date[rounding9]
            date10 = usdjpy_date[rounding10]
            date11 = usdjpy_date[rounding11]
            date12 = usdjpy_date[rounding12]
            date13 = usdjpy_date[rounding13]

            plt.figure(figsize=(10, 7)).add_subplot(xticks=[0,
                                                            float1,
                                                            float2,
                                                            float3,
                                                            float4,
                                                            float5,
                                                            float6,
                                                            float7,
                                                            float8,
                                                            float9,
                                                            float10,
                                                            float11,
                                                            float12,
                                                            float13,
                                                            count_data],
                                                    xticklabels=[search_date_start,
                                                                 date1,
                                                                 date2,
                                                                 date3,
                                                                 date4,
                                                                 date5,
                                                                 date6,
                                                                 date7,
                                                                 date8,
                                                                 date9,
                                                                 date10,
                                                                 date11,
                                                                 date12,
                                                                 date13,
                                                                 search_date_end])
            plt.plot(usdjpy_close, color='#00d5ff', label="USD/JPY")
            plt.xlim(0, count_data)
            plt.ylim(0, 200)
            plt.subplots_adjust(bottom=0.2)
            plt.xticks(rotation=90)
            plt.grid(which="major", axis="x", color="#484848", alpha=0.8,
                    linestyle="--", linewidth=1)

            plt.grid(which="major", axis="y", color="#484848", alpha=0.8,
                    linestyle="--", linewidth=1)

            plt.xlabel("Date")
            plt.ylabel("Close")
            plt.savefig("static/tmp/usdjpy_image.png")

    count_verification = count_data

    if count_verification < 15:
        msg = "日付範囲が短いのでグラフにデータを反映することができません"

    else:
        msg = ""

    context = {
        'msg': msg,
        'record':result_data,
        'form_start': form_start,
        'form_end': form_end,
        'start_date': search_date_start,
        'end_date': search_date_end,

    }

    return render(request,'stock_price/usdjpy.html',context)


# BitCoin 表・検索
def bitcoin(request):
    search_date_start = '1997-1-1'
    search_date_end = '2021-1-1'

    if (request.method == 'POST'):
        form_start = StartDateForm(request.POST)
        form_end = EndDateForm(request.POST)
        search_date_start = request.POST['date_search_start']
        search_date_end = request.POST['date_search_end']
        result_data = BITCOIN.objects.filter(date__range=[search_date_start,search_date_end]).values()
        start_datetime = dt.strptime(search_date_start, '%Y-%m-%d')
        end_datetime = dt.strptime(search_date_end, '%Y-%m-%d')
    else:
        form_start = StartDateForm()
        form_end = EndDateForm()
        result_data = BITCOIN.objects.all().values()
        start_datetime = dt.strptime('1997-01-01', '%Y-%m-%d')
        end_datetime = dt.strptime('2021-01-01', '%Y-%m-%d')

    if start_datetime > end_datetime:
        count_data = 0

    else:
        bitcoin_processing = pd.DataFrame(result_data)
        bitcoin_close = bitcoin_processing["close"]
        bitcoin_close = bitcoin_close.values.tolist()
        bitcoin_date = bitcoin_processing["date"]
        bitcoin_date = bitcoin_date.values.tolist()
        count_data = len(bitcoin_close)

        if count_data < 15 :
            pass

        else:
            unit_1 = Fraction(1, 14)
            unit_2 = Fraction(2, 14)
            unit_3 = Fraction(3, 14)
            unit_4 = Fraction(4, 14)
            unit_5 = Fraction(5, 14)
            unit_6 = Fraction(6, 14)
            unit_7 = Fraction(7, 14)
            unit_8 = Fraction(8, 14)
            unit_9 = Fraction(9, 14)
            unit_10 = Fraction(10, 14)
            unit_11 = Fraction(11, 14)
            unit_12 = Fraction(12, 14)
            unit_13 = Fraction(13, 14)

            float1 = float(unit_1 * count_data)
            float2 = float(unit_2 * count_data)
            float3 = float(unit_3 * count_data)
            float4 = float(unit_4 * count_data)
            float5 = float(unit_5 * count_data)
            float6 = float(unit_6 * count_data)
            float7 = float(unit_7 * count_data)
            float8 = float(unit_8 * count_data)
            float9 = float(unit_9 * count_data)
            float10 = float(unit_10 * count_data)
            float11 = float(unit_11 * count_data)
            float12 = float(unit_12 * count_data)
            float13 = float(unit_13 * count_data)

            rounding1 = round(float1)
            rounding2 = round(float2)
            rounding3 = round(float3)
            rounding4 = round(float4)
            rounding5 = round(float5)
            rounding6 = round(float6)
            rounding7 = round(float7)
            rounding8 = round(float8)
            rounding9 = round(float9)
            rounding10 = round(float10)
            rounding11 = round(float11)
            rounding12 = round(float12)
            rounding13 = round(float13)

            date1 = bitcoin_date[rounding1]
            date2 = bitcoin_date[rounding2]
            date3 = bitcoin_date[rounding3]
            date4 = bitcoin_date[rounding4]
            date5 = bitcoin_date[rounding5]
            date6 = bitcoin_date[rounding6]
            date7 = bitcoin_date[rounding7]
            date8 = bitcoin_date[rounding8]
            date9 = bitcoin_date[rounding9]
            date10 = bitcoin_date[rounding10]
            date11 = bitcoin_date[rounding11]
            date12 = bitcoin_date[rounding12]
            date13 = bitcoin_date[rounding13]

            plt.figure(figsize=(10, 7)).add_subplot(xticks=[0,
                                                            float1,
                                                            float2,
                                                            float3,
                                                            float4,
                                                            float5,
                                                            float6,
                                                            float7,
                                                            float8,
                                                            float9,
                                                            float10,
                                                            float11,
                                                            float12,
                                                            float13,
                                                            count_data],
                                                    xticklabels=[search_date_start,
                                                                 date1,
                                                                 date2,
                                                                 date3,
                                                                 date4,
                                                                 date5,
                                                                 date6,
                                                                 date7,
                                                                 date8,
                                                                 date9,
                                                                 date10,
                                                                 date11,
                                                                 date12,
                                                                 date13,
                                                                 search_date_end])
            plt.plot(bitcoin_close, color='#00d5ff', label="BitCoin")
            plt.xlim(0, count_data)
            plt.ylim(0, 42000)
            plt.subplots_adjust(bottom=0.2)
            plt.xticks(rotation=90)
            plt.grid(which="major", axis="x", color="#484848", alpha=0.8,
                    linestyle="--", linewidth=1)

            plt.grid(which="major", axis="y", color="#484848", alpha=0.8,
                    linestyle="--", linewidth=1)

            plt.xlabel("Date")
            plt.ylabel("Close")
            plt.savefig("static/tmp/bitcoin_image.png")

    count_verification = count_data

    if count_verification < 15:
        msg = "日付範囲が短いのでグラフにデータを反映することができません"

    else:
        msg = ""

    context = {
        'msg': msg,
        'record':result_data,
        'form_start': form_start,
        'form_end': form_end,
        'start_date': search_date_start,
        'end_date': search_date_end,

    }

    return render(request,'stock_price/bitcoin.html',context)

def get_svg_comparison(request):
    search_date_start = '1997-1-1'
    search_date_end = '2021-2-1'

    if (request.method == 'POST'):
        form_start = StartDateForm(request.POST)
        form_end = EndDateForm(request.POST)
        search_date_start = request.POST['date_search_start']
        search_date_end = request.POST['date_search_end']
        result_data_nikkei = NIKKEI.objects.filter(date__range=[search_date_start, search_date_end]).values()
        result_data_sp500 = SP500.objects.filter(date__range=[search_date_start, search_date_end]).values()
        result_data_usdjpy = USDJPY.objects.filter(date__range=[search_date_start, search_date_end]).values()
        result_data_bitcoin = BITCOIN.objects.filter(date__range=[search_date_start,search_date_end]).values()
        nikkei_processing = pd.DataFrame(result_data_nikkei)
        sp500_processing = pd.DataFrame(result_data_sp500)
        usdjpy_processing = pd.DataFrame(result_data_usdjpy)
        bitcoin_processing = pd.DataFrame(result_data_bitcoin)
    else:
        form_start = StartDateForm()
        form_end = EndDateForm()
        result_data_nikkei = NIKKEI.objects.all().values()
        result_data_sp500 = SP500.objects.all().values()
        result_data_usdjpy = USDJPY.objects.all().values()
        result_data_bitcoin = BITCOIN.objects.all().values()
        nikkei_processing = pd.DataFrame(result_data_nikkei)
        sp500_processing = pd.DataFrame(result_data_sp500)
        usdjpy_processing = pd.DataFrame(result_data_usdjpy)
        bitcoin_processing = pd.DataFrame(result_data_bitcoin)

    nikkei_close = nikkei_processing["close"]
    nikkei_close = nikkei_close.values.tolist()
    sp500_close = sp500_processing["close"]
    sp500_close = sp500_close.values.tolist()
    usdjpy_close = usdjpy_processing["close"]
    usdjpy_close = usdjpy_close.values.tolist()
    bitcoin_close = bitcoin_processing["close"]
    bitcoin_close = bitcoin_close.values.tolist()
    #count_data = len(bitcoin_close)

    nikkei_count = len(nikkei_close)
    sp500_count = len(sp500_close)
    usdjpy_count = len(usdjpy_close)
    bitcoin_count = len(bitcoin_close)

    ax1 = plt.figure(figsize=(5, 4)).add_subplot(111,xticks=[0, nikkei_count], xticklabels=[search_date_start, search_date_end])
    ax2 = plt.figure(figsize=(5, 4)).add_subplot(111, xticks=[0, sp500_count], xticklabels=[search_date_start, search_date_end])
    ax3 = plt.figure(figsize=(5, 4)).add_subplot(111, xticks=[0, usdjpy_count],xticklabels=[search_date_start, search_date_end])
    ax4 = plt.figure(figsize=(5, 4)).add_subplot(111, xticks=[0, bitcoin_count],xticklabels=[search_date_start, search_date_end])
    ax1.plot(nikkei_close, color='#00d5ff', label="NIKKEI")
    ax2.plot(sp500_close, color='green', label="SP500")
    ax3.plot(usdjpy_close, color='red', label="USD/JPY")
    ax4.plot(bitcoin_close, color='#FFFF00', label="BitCoin")
    ax1.set_title("NIKKEI")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Close")
    ax1.legend()
    ax2.set_title("SP500")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Close")
    ax2.legend()
    ax3.set_title("USD/JPY")
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Close")
    ax3.legend()
    ax4.set_title("BitCoin")
    ax4.set_xlabel("Date")
    ax4.set_ylabel("Close")
    ax4.legend()
    ax1.get_figure().savefig("static/tmp/common_image_nikkei.png")
    ax2.get_figure().savefig("static/tmp/common_image_sp500.png")
    ax3.get_figure().savefig("static/tmp/common_image_usdjpy.png")
    ax4.get_figure().savefig("static/tmp/common_image_bitcoin.png")

    context = {
        #'record': bitcoin_processing.to_html(),
        'form_start': form_start,
        'form_end': form_end,
        'start_date': search_date_start,
        'end_date': search_date_end,
    }

    return render(request, 'stock_price/common.html', context)
