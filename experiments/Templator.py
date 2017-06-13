from pywikiaccessor.wiki_accessor import WikiAccessor
from pywikiaccessor.wiki_file_index import WikiFileIndex
from pywikiaccessor.wiki_categories import CategoryIndex
from pywikiutils.wiki_headers import HeadersFileIndex
from pywikiaccessor.wiki_iterator import WikiIterator

import numpy as np
import pickle
import json
import codecs
from collections import Counter
from math import log

class TemplateBuilder(WikiIterator):

    def preProcess(self):
        pass

    def processDocument(self, docId):
        pass

    def clear(self):
        pass

    def postProcess(self):
        pass

    def processSave(self, articlesCount):
        pass