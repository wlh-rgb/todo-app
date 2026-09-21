# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
import storage
import task_manager

def main():
    tasks = storage.load_tasks()

    while True:
        print("\n===== 待办事项 =====")
        print("1. 添加任务")
        print("2. 查看任务")
        print("3. 标记完成")
        print("4. 删除任务")
        print("5. 修改任务")
        print("6. 任务统计")
        print("7. 退出")
        choice = input("请选择：")

        if choice == "1":
            task_manager.add_task(tasks)
        elif choice == "2":
            task_manager.list_tasks(tasks)
        elif choice == "3":
            task_manager.complete_task(tasks)
        elif choice == "4":
            task_manager.delete_task(tasks)
        elif choice == "5":
            task_manager.edit_task(tasks)
        elif choice == "6":
            task_manager.show_stats(tasks)
        elif choice == "7":
            storage.save_tasks(tasks)
            print("再见！")
            break
        else:
            print("无效选择，请重新输入")

if __name__ == "__main__":
    main()