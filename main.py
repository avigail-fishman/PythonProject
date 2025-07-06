from TextFileAnalyzer import TextFileAnalyzer
from JSONFileAnalyzer import JSONFileAnalyzer
import os
import json

def main():
    files_to_analyze = input("הכנס נתיב קובץ: ").split(',')
    search_word = input("הכנס מילה לחיפוש ").strip() or None
    # רשימה זו תכיל את התוצאות של הניתוח של כל קובץ
    results = []
    # מעבר על כל נתיבי הקובץ שהוכנס ומסירים רווחים מיותרים
    for file_path in files_to_analyze:
        file_path = file_path.strip()
        # בודקים את סוג הקובץ לפי הסיומת שלו, בשביל שנדע איזה מחלקה צריך להשתמש בשבילו
        try:
            if file_path.endswith('.txt'):
                analyzer = TextFileAnalyzer(file_path, search_word)
            elif file_path.endswith('.json'):
                analyzer = JSONFileAnalyzer(file_path, search_word)
            else:
                print(f"אין תמיכה בסוג קובץ כזה: {file_path}")
                continue
            # טוענים את הקובץ
            analyzer.load_file()
            # מבצעים עליו ניתוח
            analysis = analyzer.analyze()
            # מוסיפים את שם הקובץ עצמו לתוך התוצאה
            analysis["file"] = file_path
            # מוסיפים את התוצאה לרשימה
            results.append(analysis)
            # יוצרים שם אישי לכל קובץ - לתוצאה שלו ושומרים את התוצאה שלו ע"י הפונקציה שקיימת במחלקת הבסיס
            output_filename = f"{os.path.splitext(os.path.basename(file_path))[0]}_analysis.json"
            analyzer.save_results_to_json(analysis, output_filename)
        # אם יש שגיאה - התוכנית לא נופלת , היא מדפיסה הודעה וממשיכה הלאה
        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")
    # ממיינים את התוצאה לפי שם הקובץ
    results.sort(key=lambda x: x["file"].lower())
    # מדפיסים את התוצאות למסך בפורמט JSON
    print(json.dumps(results, indent=4, ensure_ascii=False))
    # שומרים את כל התוצאות בקובץ אחד
    with open("summary_analysis.json", "w", encoding="utf-8") as summary_file:
        json.dump(results, summary_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()
