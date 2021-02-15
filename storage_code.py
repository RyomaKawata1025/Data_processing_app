

"""Views.pyコード"""
"""
from django.views.generic import ListView,TemplateView
from django.views import View
from django.db.models import Q

import defusedxml.ElementTree as ET


class TestView(ListView):
    def get_queryset(self):
        q_word = self.request.GET.get('keyword')
        q_word2 = self.request.GET.get('keyword2')
        if q_word and q_word2:
            object_list = NIKKEI.objects.filter(date__range=[q_word, q_word2]).values()
        else:
            object_list = NIKKEI.objects.all()
        return object_list


class TestView(object):

    #template_name = "stock_price/test.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["foo"] = "bar"
        return context

class TestlistView(ListView, TestView):
    model = NIKKEI
    context_object_name = "object_list"

class TestView(ListView):
    #def get_queryset(self):
    def test_serch(self,request):
        if (request.method == 'POST'):
            form_start = StartDateForm(request.POST)
            form_end = EndDateForm(request.POST)
            search_date_start = request.POST['date_search_start']
            search_date_end = request.POST['date_search_end']
            result_data = NIKKEI.objects.filter(date__range=[search_date_start,search_date_end]).values()
            nikkei_processing = pd.DataFrame(result_data)
        else:
            form_start = StartDateForm()
            form_end = EndDateForm()
            data_test = USDJPY.objects.all().values()
            usdjpy_processing = pd.DataFrame(data_test)
        context = {
            'record': usdjpy_processing.to_html(),
            'form_start': form_start,
            'form_end': form_end,
        }
        return render(request, 'stock_price/nikkei_list.html', context)


def serchform(request):
    if (request.method == 'POST'):
        #form = SearchForm(request.POST)
        data_test = NIKKEI.objects.filter(date_range=["2020-0101" ,"2021-01-01"])
    else:
        data_test = NIKKEI.objects.all()

    context = {
        'data':data_test,
    }
    return render(request,'stock_price/nikkei.html',context)


# SVG化
def plt2svg():
    buf = io.BytesIO() #メモリ上でバイナリデータを扱うための機能
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

def index(request):
    return render(request, 'stock_price/index.html')

def nikkei(request):
    return render(request, 'stock_price/nikkei.html')

def sp500(request):
    return render(request, 'stock_price/sp500.html')

def usdjpy(request):
    return render(request, 'stock_price/usdjpn.html')

def bitcoin(request):
    return render(request, 'stock_price/bitcoin.html')

#日経225終値
def setPlt_nikkei():
    plt.figure(figsize=(10, 7)).add_subplot(1,1,1).set_xticks([0,9999])
    plt.plot(nikkei_close, color='#00d5ff')
    #plt.plot(sp500_height, color='black')
    #plt.set_xticks([0, 250, 500, 750, 1000])
    plt.title(r"$\bf{NIKKEI225}$", color='#3407ba')
    plt.xlabel("Date")
    plt.ylabel("Close")


def setPlt_sp500(request):
    return render(request, 'stock_price/usdjpn.html')

def setPlt_usdjpy(request):
    return render(request, 'stock_price/usdjpn.html')

def setPlt_comparison(request):
    return render(request, 'stock_price/usdjpn.html')

#SP500終値
def get_svg_sp500(request):
    setPlt_sp500()
    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')
    return response

# 日経225終値
def get_svg_nikkei(request):
    setPlt_nikkei()
    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')

    return response

# USD/JPY終値
def get_svg_usdjpy(request):
    setPlt_usdjpy()
    svg = plt2svg()  # SVG化

    plt.cla()  # グラフをリセット


    f = open('out2.svg', 'w')

    f.write(str(svg))


    f.close()

    response = HttpResponse(svg, content_type='image/svg+xml')

    return response


def get_svg_comparison(request):
    return render(request, 'stock_price/usdjpn.html')

def get_nikkei_processing(search_date_start=None, search_date_end=None):
    if search_date_start is None and search_date_end is None:
        result_data = NIKKEI.objects.all().values()
    else:
        result_data = NIKKEI.objects.filter(date__range=[search_date_start, search_date_end]).values()
    data_processing = pd.DataFrame(result_data)
    return data_processing

def plt2svg():
    buf = io.BytesIO() #メモリ上でバイナリデータを扱うための機能
    plt.savefig(buf, format='svg', bbox_inches='tight')
    s = buf.getvalue()
    buf.close()
    return s

#全共通終値
def setPlt_comparison():
    plt.figure(figsize=(10, 7)).add_subplot(1,1,1).set_xticks([0,9999])
    #plt.figure(figsize=(17, 9)).add_subplot(1,1,1).set_xticklabels(["a","b","c","d","e","f","g","h","i","j","k","l"])
    plt.plot(nikkei_close, color='#00d5ff')
    plt.plot(sp500_close, color='green')
    plt.plot(usdjpy_close, color='red')
    plt.plot(bitcoin_close, color='#FFFF00')
    plt.title(r"$\bf{USD/JPY}$", color='#3407ba')
    plt.xlabel("Date")
    plt.ylabel("Close")
    plt.savefig("static/tmp/common_image.png")

# 全共通終値
def get_svg_comparison1(request):
    setPlt_comparison()
    svg = plt2svg()  #SVG化
    plt.cla()  # グラフをリセット
    response = HttpResponse(svg, content_type='image/svg+xml')

    return response

"""

# usdjpy_date = usdjpy_date.strftime("%Y/%m/%d")


