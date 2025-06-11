class Task:

    def __init__(self, description, agent, data=None):
        self.description = description
        self.agent = agent
        self.data = data or {}
        self.status = 'pending'
