from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from experiments.categoriesTree import CateforiesTree
from experiments.HeadersExtractor import HeadersExtractor
import json

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
        cats = json.loads(request.POST['categories'])
        he = HeadersExtractor();
        print(he.getHeadersForTree(cats))
        return redirect('index')