from transliterate import translit
from pywikiaccessor import wiki_accessor
from pywikiaccessor import wiki_categories
from pywikiaccessor.document_type import DocumentTypeConfig
import json

directory = "C:\\[Study]\\Diploma\\wiki_indexes\\"
accessor = wiki_accessor.WikiAccessor(directory)

bld = wiki_categories.CategoryIndex(accessor)

catTitle = 'Арифметика'
catId = bld.getIdByTitle(catTitle)

def tree_maker(parentNodeId):
    newNode = {}
    nodeText = bld.getTitleById(parentNodeId)
    nodeHref = '#' + translit(nodeText, 'ru', reversed=True)
    tags = []
    nodes = []
    newNode['text'] = nodeText
    newNode['href'] = nodeHref
    newNode['tags'] = tags
    newNode['nodes'] = nodes
    subCats = bld.getSubCatAsSet(parentNodeId)
    if len(subCats):
        for cat in subCats:
            childNode = tree_maker(cat)
            newNode['nodes'].append(childNode)
    return newNode

def tree_maker_from_doctype(directory):
    with open(directory + 'DocumentTypeConfig.json', encoding="utf8") as data_file:
        doctypes = json.load(data_file, encoding="utf-8")
        for doctype in doctypes:
            if (doctype.get('categories', None)):
                for category in doctype['categories']:
                    print(category)
    


# print(tree_maker(catId))
print(tree_maker_from_doctype(directory))

print("end")