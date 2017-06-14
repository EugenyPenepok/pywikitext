from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from experiments.categoriesTree import CateforiesTree
from experiments.HeadersExtractor import HeadersExtractor
from experiments.SelectedModel import UserModel
from pywikiaccessor import wiki_accessor
from experiments.science_patterns import POSListBuilder, СollocationBuilder

import json
import re

choosenCats = []
headersForCats = []
# Исправить
directory = "C:\\[Study]\\Diploma\\wiki_indexes\\"

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

def get_categories(request):
    if request.method == 'GET':
        catTree = CateforiesTree()
        json_data = catTree.tree_maker_from_doctype(directory)
        return JsonResponse(json_data, safe=False)

def post_tree_categories(request):
    if request.method == 'POST':
        global choosenCats
        global headersForCats
        # Получение отмеченных категорий
        choosenCats = json.loads(request.POST['categories'])
        # Сохранение всех заголовков для категорий
        he = HeadersExtractor();
        headersForCats = he.getHeadersForTree_better(choosenCats)
        return redirect('index')

def post_selected_headers(request):
    if request.method == 'POST':
        choosenHeaders = json.loads(request.POST['headers'])
        # um = UserModel("test","qwe", choosenCats, choosenHeaders)
        # print(um.config_maker())
        return redirect('index')

def get_headers(request):
    if request.method == 'GET' :
        if 'q' in request.GET:
            pattern = request.GET['q'].lower()
            result = []
            for header in headersForCats:
                if re.search(pattern, header['text']):
                    result.append(header)
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse(headersForCats, safe=False)
