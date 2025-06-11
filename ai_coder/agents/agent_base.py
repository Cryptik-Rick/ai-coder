class AgentBase:
    def __init__(self, context):
        self.context = context

    def run(self, task):
        raise NotImplementedError
