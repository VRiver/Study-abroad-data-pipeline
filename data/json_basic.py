import json

program = {
    "school_name": "University of Example",
    "country": "United States",
    "program_name": "MSc Data Science",
    "degree": "Master",
    "ielts_min": 6.5,
    "tuition_amount": None,
    "source_url": "https://example.edu/program"
}

output_path = r"D:\Codex项目\数据岗位冲刺\data\program.json"

with open(
    output_path,
    "w",
    encoding="utf-8"
) as file:
    json.dump(
        program,
        file,
        ensure_ascii=False,
        indent=4
    )

with open(
    output_path,
    "r",
    encoding="utf-8"
) as file:
    loaded_program = json.load(file)

print("读取后的项目数据：")
print(loaded_program)
print("项目名称：", loaded_program["program_name"])
print("学费：", loaded_program["tuition_amount"])