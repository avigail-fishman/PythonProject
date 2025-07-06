from BaseFileAnalyzer import BaseFileAnalyzer

class JSONFileAnalyzer(BaseFileAnalyzer):

    # פונקציה שבודקת אם הקובץ קיים, אם כן - קורא את הקובץ למשתנה
    def load_file(self):
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"File not found: {self.filepath}")

        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.data = json.load(f)

    # פונקציה שמנתחת את הקובץ
    def analyze(self):
        all_text = ""
        # מעבר על כל המילים בקובץ
        for item in self.data:
            # ממיר את כל הערכים של המילון הספציפי למחרוזת, ומחבר אותם למחרוזת אחת גדולה
            all_text += ' '.join(str(value) for value in item.values()) + " "
        # מסיר סימני פיסוק מהמחרוזת
        text = all_text.translate(str.maketrans('', '', string.punctuation))
        # ממיר לאותיות קטנות
        words = text.lower().split()
        # סופר את כמות המילים
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

        matches = []
        # עובר על כל מילה בקובץ JSON
        for i, item in enumerate(self.data):
            # עבור כל מילה בודק אם הערך הוא מחרוזת, ואם המילה שמחפשים מופיעה בתוכה
            for key, value in item.items():
                # אם כן - שומר את האינדקס, המיקום
                if isinstance(value, str) and re.search(rf'\b{re.escape(self.search_word)}\b', value, re.IGNORECASE):
                    matches.append({"index": i, "field": key})
        return matches
