# student_utils.py
def parse_student(line):
    line = line.strip()
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError(f"字段数量错误，得到{len(parts)}个字段")
    name_str, score_str = parts
    name_str = name_str.strip()
    score_str = score_str.strip()
    if not name_str:
        raise ValueError("姓名为空")
    try:
        score_int = int(score_str)
    except ValueError:
        raise ValueError(f"成绩无法转为整数：{score_str}")
    if not (0 <= score_int <= 100):
        raise ValueError(f"分数{score_int}超出0‑100范围")
    return {"name": name_str, "score": score_int}
