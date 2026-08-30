# 留学数据岗位面试冲刺包

## 快速开始

```powershell
python -m pip install pandas beautifulsoup4 requests pytest
python -m pytest work/tests -q
python -c "import sqlite3; c=sqlite3.connect('work/data/interview.db'); c.executescript(open('work/sql/schema.sql').read()); print(c.execute(open('work/sql/questions.sql').read().split('-- 2.')[0]).fetchall())"
```

## 五天使用顺序

1. `work/sql/schema.sql` 与 `work/sql/questions.sql`：先理解表，再遮住答案手写。
2. `work/study_kit/cleaning.py`：阅读代码后，用 `work/data/programs.csv` 改写一遍。
3. `work/study_kit/scraper.py`：先练静态 HTML，不做复杂反爬。
4. 对照 `work/interview_notes.md` 练口述和群面。

## 面试底线

任何抽取结果都要保留来源链接、更新时间，并对缺失、重复、单位和日期做检查；GPT 生成的结果必须抽样回看原文。
