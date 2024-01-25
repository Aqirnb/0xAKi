class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"任务已添加: {task}")

    def view_tasks(self):
        if self.tasks:
            print("任务列表：")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("没有任务")

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f"任务已移除: {removed_task}")
        else:
            print("无效的任务索引")

# 使用示例
task_manager = TaskManager()

task_manager.add_task("完成项目报告")
task_manager.add_task("学习新技术")
task_manager.view_tasks()

task_manager.remove_task(1)
task_manager.view_tasks()
