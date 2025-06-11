from .agent_base import AgentBase


class ManagerAgent(AgentBase):

    def run(self):
        while self.context.backlog:
            task = self.context.backlog.pop(0)
            print(
                f"ManagerAgent: Assigning task '{task.description}' to "
                f"{task.agent}"
            )


            # In a real system, would dispatch to the correct agent

