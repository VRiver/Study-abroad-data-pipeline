-- 1. 各国家项目数量
SELECT s.country, COUNT(*) AS program_count FROM schools s JOIN programs p USING (school_id) GROUP BY s.country ORDER BY program_count DESC;
-- 2. 没有语言要求的项目
SELECT p.program, s.school FROM programs p JOIN schools s USING (school_id) LEFT JOIN requirements r USING (program_id) WHERE r.ielts_min IS NULL;
-- 3. 各国家平均学费
SELECT s.country, AVG(p.tuition_usd) AS avg_tuition FROM schools s JOIN programs p USING (school_id) GROUP BY s.country;
-- 4. 每个国家最贵项目（窗口函数）
WITH ranked AS (SELECT s.country, p.program, p.tuition_usd, RANK() OVER (PARTITION BY s.country ORDER BY p.tuition_usd DESC) AS rnk FROM programs p JOIN schools s USING (school_id)) SELECT * FROM ranked WHERE rnk = 1;
-- 5. 识别重复项目（业务键）
SELECT school_id, program, degree, COUNT(*) AS duplicate_count FROM programs GROUP BY school_id, program, degree HAVING COUNT(*) > 1;
