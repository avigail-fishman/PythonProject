import os
import re
import string
from collections import Counter

from BaseFileAnalyzer import BaseFileAnalyzer

class TextFileAnalyzer(BaseFileAnalyzer):

    # פונקציה שבודקת אם הקובץ קיים, אם כן - קורא את הקובץ למשתנה
    def load_file(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found: {self.filepath}")

        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.data = f.read()
    # פונקציה שמנתחת את הקובץ
    def analyze(self):
        # מסיר סימני פיסוק
        text = self.data.translate(str.maketrans('', '', string.punctuation))
        # ממיר לאותיות קטנות ומפריד מילים
        words = text.lower().split()
        # סופר את המילים
        word_count = len(words)
        # סופר כמה פעמים כל מילה מופיעה
        word_freq = Counter(words)
        # מוצא את חמשת המילים הכי נפוצות
        most_common = word_freq.most_common(5)
        return {
            "total_words": word_count,
            "unique_words": dict(word_freq),
            "most_common": most_common,
            "search_word_positions": self.search_word_positions()
        }
    # פונקציה שמוצאת מיקומים של מילים מסוימות בטקסט
    def search_word_positions(self):
        if not self.search_word:
            return []
        positions = [m.start() for m in re.finditer(rf'\b{re.escape(self.search_word)}\b', self.data, re.IGNORECASE)]
        return positions