class ProjectContext:
    def __init__(self):
        self.files = {}
        self.tests = {}
        self.backlog = []
        self.state = {}

    def add_file(self, name, content):
        self.files[name] = content

    def add_test(self, name, content):
        self.tests[name] = content

    def add_task(self, task):
        self.backlog.append(task)
