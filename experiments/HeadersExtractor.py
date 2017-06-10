from pywikiaccessor import wiki_accessor
from pywikiaccessor.wiki_categories import CategoryIndex
from pywikiaccessor.title_index import TitleIndex
from pywikiutils.wiki_headers import HeadersFileIndex

directory = "C:\\[Study]\\Diploma\\wiki_indexes\\"
accessor = wiki_accessor.WikiAccessor(directory)
titleIndex = TitleIndex(accessor)
bld = CategoryIndex(accessor)
hid = HeadersFileIndex(accessor)

class HeadersExtractor:
    def getCategoryHeaders(self, categoryId):
        categoryPages = bld.getDirectPages(categoryId)
        headersSet = set()  # множество с id заголовков статей категории
        for page in categoryPages:
            for h in hid.headersByDoc(page):
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
            headersDict['text'] = hid.headerText(h)
            headersArray.append(headersDict)
        return headersArray

# category = 'Барнаул'
# categoryId = titleIndex.getTitleById(category)
# test = HeadersExtractor()
#
# for header in test.getCategoryHeaders(categoryId):
#     if header['id'] == 144:  # история (присутствует в заголовках)
#         print(hid.getDocSection(articleId, header['id']))
