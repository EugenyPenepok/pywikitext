from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from experiments.categoriesTree import CateforiesTree
from experiments.HeadersExtractor import HeadersExtractor
import json
import re

choosenCats = []
headersForCats = []
# Исправить
directory = "C:\\[Study]\\Diploma\\wiki_indexes\\"

def index(request):
    if request.method == 'GET':
        catTree = CateforiesTree()
        json_data = catTree.tree_maker_from_doctype(directory)
        context = {'json_data': json_data}
        return render(request, 'index.html', context)

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
        headersForCats = he.getHeadersForTree(choosenCats)
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
