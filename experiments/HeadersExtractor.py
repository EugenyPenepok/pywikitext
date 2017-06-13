from pywikiaccessor import wiki_accessor
from pywikiaccessor.wiki_categories import CategoryIndex
from pywikiutils.wiki_headers import HeadersFileIndex

class HeadersExtractor:
    directory = "C:\\[Study]\\Diploma\\wiki_indexes\\"
    accessor = wiki_accessor.WikiAccessor(directory)
    bld = CategoryIndex(accessor)
    hid = HeadersFileIndex(accessor)

    def getCategoryHeaders(self, categoryId):
        categoryPages = self.bld.getDirectPages(categoryId)
        headersSet = set()  # множество с id заголовков статей категории
        for page in categoryPages:
            for h in self.hid.headersByDoc(page):
                headersSet.add(h['header'])
        return headersSet
        # for header in headersSet:
        #     print(hid.headerText(header))
    def getHeadersForTree(self, categories):
        allheaders = set()
        for category in categories:
            allheaders.update(self.getCategoryHeaders(category))
        headersArray = []
        for h in allheaders:
            headersDict = {}
            headersDict['id'] = h
            headersDict['text'] = self.hid.headerText(h)
            headersArray.append(headersDict)
        return headersArray

    def getCategoryHeaders_better(self, categoryId):
        categoryPages = self.bld.getDirectPages(categoryId)
        headersDict = {}
        for page in categoryPages:
            for h in self.hid.headersByDoc(page):
                if headersDict.get(h['header'], False):
                    headersDict[h['header']].append(page)
                else:
                    headersDict[h['header']] = []
                    headersDict[h['header']].append(page)
        return headersDict

    def getHeadersForTree_better(self, categories):
        headersDict = {}
        for category in categories:
            categoryPages = self.bld.getDirectPages(category)
            for page in categoryPages:
                for h in self.hid.headersByDoc(page):
                    if headersDict.get(h['header'], False):
                        headersDict[h['header']].append(page)
                    else:
                        headersDict[h['header']] = []
                        headersDict[h['header']].append(page)
        headersArray = []
        for key, val in headersDict.items():
            headersDict = {}
            headersDict['id'] = key
            headersDict['text'] = self.hid.headerText(key)
            headersDict['amount'] = len(val)
            headersDict['docs'] = val
            headersArray.append(headersDict)
        return headersArray
#
#
#
# category1 = 'Деление'
# category2 = 'Спорт в Вильнюсе'
# category1Id = bld.getIdByTitle(category1)
# category2Id = bld.getIdByTitle(category2)
# categories = {category1Id, category2Id}
# test = HeadersExtractor()
#
# old_stuff = test.getHeadersForTree(categories)
# print(len(old_stuff))
# print(old_stuff)
# print('-----------')
# new_stuff = test.getHeadersForTree_better(categories)
# print(len(new_stuff))
# print(new_stuff)
