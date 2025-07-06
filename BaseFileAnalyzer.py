import os
import re
import json
import string
from abc import ABC, abstractmethod
from collections import Counter

class BaseFileAnalyzer(ABC):

    # קונסטראקטור
    def __init__(self, filepath, search_word=None):
        self.filepath = filepath
        self.search_word = search_word
        self.data = None
    # פונקציה לטעינת קובץ
    @abstractmethod
    def load_file(self):
        pass
    # פונקציה שמנתחת קובץ
    @abstractmethod
    def analyze(self):
        pass
    # פונקציה שמוצאת מיקומים של מילים מסוימות בטקסט
    @abstractmethod
    def search_word_positions(self):
        pass
    # שומרת את התוצאות שקיבלה לתוך קובץ JSON
    def save_results_to_json(self, results, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=4, ensure_ascii=False)