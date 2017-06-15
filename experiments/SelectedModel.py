from pywikiaccessor import wiki_accessor
from pywikiaccessor.wiki_categories import CategoryIndex
from pywikiutils.wiki_headers import HeadersFileIndex
from experiments.science_patterns import POSListBuilder, СollocationBuilder

import json

class UserModel:
    directory = "C:\\[Study]\\Diploma\\wiki_indexes\\"
    nameOfModel = "temp"
    prefixModel = "slug"
    selectedCats = []
    selectedHeaders = []
    def __init__(self, name, prefix, categories, headers):
        self.nameOfModel = "temp"
        self.prefixModel = "slug"
        self.selectedCats = categories
        self.selectedHeaders = headers

    def config_maker(self):
        export = {}
        export[self.prefixModel] = self.selectedHeaders
        return export
        # with open(self.directory + 'TemplateConfig.json', 'w', encoding="utf8") as outfile:
        #     return json.dump(export, outfile)
        # with open('tree.json', 'w', encoding='utf8') as outfile:
        # return json.dumps(listOfCategories, ensure_ascii=False)

import pickle

if __name__ =="__main__":
    accessor = wiki_accessor.WikiAccessor("C:\\[Study]\\Diploma\\wiki_indexes\\")
    my_config = {"slug": ["4", "1252"]}
    um = UserModel("test", "qwe", {}, my_config)

    # with open("C:\\[Study]\\Diploma\\wiki_indexes\\DocumentHeaders.pcl" , 'rb') as f:
    #     temp = pickle.load(f)

    sb = POSListBuilder(accessor, "slug", my_config)
    sb.build()

    fb = СollocationBuilder(accessor, "slug", my_config)
    fb.build()

# directory = "C:\\[Study]\\Diploma\\wiki_indexes\\"
# accessor = wiki_accessor.WikiAccessor(directory)
# sb = POSListBuilder(accessor, "slug", config)
# sb.build()
# fb = СollocationBuilder(accessor, "slug", config)
# fb.build()