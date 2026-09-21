def add_task(tasks):
    title = input("请输入任务内容：")
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    print(f"已添加：{title}")

def list_tasks(tasks):
    if not tasks:
        print("暂无任务")
        return
    for task in tasks:
        status = "✔" if task["done"] else "✘"
        print(f'{task["id"]}. [{status}] {task["title"]}')

def complete_task(tasks):
    list_tasks(tasks)
    try:
        task_id = int(input("请输入要完成的任务编号："))
    except ValueError:
        print("请输入数字")
        return
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print("已标记完成")
            return
    print("没找到这个任务")

def delete_task(tasks):
    list_tasks(tasks)
    try:
        task_id = int(input("请输入要删除的任务编号："))
    except ValueError:
        print("请输入数字")
        return
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("已删除")
            return
    print("没找到这个任务")

def edit_task(tasks):
    list_tasks(tasks)
    try:
        task_id = int(input("请输入要修改的任务编号："))
    except ValueError:
        print("请输入数字")
        return
    for task in tasks:
        if task["id"] == task_id:
            new_title = input("请输入新的任务内容：")
            task["title"] = new_title
            print("已修改")
            return
    print("没找到这个任务")

def show_stats(tasks):
    if not tasks:
        print("暂无任务")
        return
    total = len(tasks)
    done_count = 0
    for task in tasks:
        if task["done"]:
            done_count += 1
    undone_count = total - done_count
    print(f"总数:{total}, 已完成:{done_count}, 未完成:{undone_count}")