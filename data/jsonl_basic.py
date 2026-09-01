import json

programs = [
    {
        "school_name": "University A",
        "program_name": "Data Science",
        "ielts_min": 6.5
    },
    {
        "school_name": "University B",
        "program_name": "Business Analytics",
        "ielts_min": 7.0
    },
    {
        "school_name": "University C",
        "program_name": "Public Policy",
        "ielts_min": None
    }
]

output_path = r"D:\Codex项目\数据岗位冲刺\data\programs.jsonl"

with open(
    output_path,
    "w",
    encoding="utf-8"
) as file:
    for program in programs:
        file.write(
            json.dumps(
                program,
                ensure_ascii=False
            ) + "\n"
        )

print("JSONL 文件保存成功")

with open(
    output_path,
    "r",
    encoding="utf-8"
) as file:
    for line in file:
        program = json.loads(line)
        print(program)