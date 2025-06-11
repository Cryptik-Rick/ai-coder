

def main():
    parser = argparse.ArgumentParser(
        description="AI Coder Project Orchestrator"
    )
    parser.add_argument(
        "description", help="Project description for the agents"
    )
    args = parser.parse_args()

    # Initialize context and agents
    context = ProjectContext()
    agents = {
        "manager": ManagerAgent(context),
        "prompt": PromptAgent(context),
        "codegen": CodeGenAgent(context),
        "test": TestAgent(context),
        "integrator": IntegratorAgent(context),
        "dialogue": DialogueAgent(context),
    }

    # Add initial tasks to backlog
    context.add_task(
        Task(
            description=f"Scaffold project for: {args.description}",
            agent="manager"
        )
    )

    # Simple agent loop (MVP: manager only delegates, others are placeholders)
    while context.backlog:
        task = context.backlog.pop(0)
        agent = agents.get(task.agent)
        if agent:
            print(f"[SYSTEM] Running {task.agent} on: {task.description}")
            if task.agent == "manager":
                # Manager creates subtasks for other agents
                context.add_task(Task("Refine prompt for project", "prompt"))
                context.add_task(Task("Generate code for CLI echo app", "codegen"))
                context.add_task(Task("Generate test for CLI echo app", "test"))
                context.add_task(Task("Integrate code and tests", "integrator"))
            else:
                agent.run(task)
        else:
            print(f"[ERROR] No agent found for: {task.agent}")


if __name__ == "__main__":
    main()
