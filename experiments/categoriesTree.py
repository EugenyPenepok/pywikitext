from pywikiaccessor import wiki_accessor
from pywikiaccessor import wiki_categories
import json

class CateforiesTree:
    directory = "C:\\[Study]\\Diploma\\wiki_indexes\\"
    accessor = wiki_accessor.WikiAccessor(directory)
    bld = wiki_categories.CategoryIndex(accessor)
    def tree_maker(self, parentNodeId):
        newNode = {}
        nodeText = self.bld.getTitleById(parentNodeId)
        # nodeHref = '#' + translit(nodeText, 'ru', reversed=True)
        # for ch in ['\\', '`', '*', '>', '#', '+', '-', '.', '!', '$', '\'', ' ', '«', '»']:
        #     nodeHref = nodeHref.replace(ch, '')
        nodeHref = parentNodeId
        tags = []
        nodes = []
        newNode['text'] = nodeText
        newNode['href'] = nodeHref
        newNode['tags'] = tags
        subCats = self.bld.getSubCatAsSet(parentNodeId)
        if len(subCats):
            newNode['nodes'] = nodes
            for cat in subCats:
                if cat != parentNodeId:  # Enjoy Movies
                    childNode = self.tree_maker(cat)
                    newNode['nodes'].append(childNode)
        return newNode

    def tree_maker_from_doctype(self, docTypeDirectory):
        listOfCategories = []
        with open(docTypeDirectory + 'DocumentTypeConfig.json', encoding="utf8") as data_file:
            doctypes = json.load(data_file, encoding="utf-8")
            for doctype in doctypes:
                if (doctype.get('categories', None)):
                    for category in doctype['categories']:
                        catId = self.bld.getIdByTitle(category)
                        listOfCategories.append(self.tree_maker(catId))
        # with open('tree.json', 'w', encoding='utf8') as outfile:
        # return json.dumps(listOfCategories, ensure_ascii=False)
        return listOfCategories


# test = CateforiesTree()
# print(test.tree_maker(bld.getIdByTitle('Фильмы')))
# #print(test.tree_maker_from_doctype(directory))
# print("--end--")