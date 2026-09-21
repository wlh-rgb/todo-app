import json
import os

FILE = "tasks.json"

def save_tasks(tasks):
    try:
        with open(FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
        print("保存成功")
    except OSError as e:
        print(f"保存失败：{e}")

def load_tasks():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️ 数据文件损坏，已重置为空列表")
        return []