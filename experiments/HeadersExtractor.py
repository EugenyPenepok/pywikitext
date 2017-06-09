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
        headersSet = set()  # множество с заголовками статей категории
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
        return allheaders
