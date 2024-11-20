from autogen import ConversableAgent

LLM_CONFIG = {
    "model": "mistral:latest",
    "client_host": "http://localhost:11434/",
    "api_type": "ollama",
    "seed": 42,
    "cache_seed": None,
    "repeat_penalty": 1.1,
    "stream": False,
    "native_tool_calls": False,
    "temp": 0.0,
    "use_docker": False,
}

system_prompt = """

You are an AI agent capable of solving coding tasks by writing, testing, and verifying code. Your primary goal is to produce correct and functional Python or shell script solutions. Follow these guidelines:
        1. When solving a task, provide Python code in a python code block or shell script in a sh code block. Assume all necessary dependencies have been installed using pip.
        2. If additional information is needed, generate and suggest code to gather the required details (e.g., reading files, fetching data, or checking system information).
        3. Test your solution by simulating verification steps and ensure the output meets the task requirements.
        4. Output your solution as a self-contained script in a code block, ready for execution.

When all steps above are done:
 - Write TERMINATE (it should always be UPPERCASE and outside of the code block notated with ```)
"""


def create_code_generator_agent() -> ConversableAgent:
    # Define the agent
    agent = ConversableAgent(
        name="Code Generator Agent",
        system_message=system_prompt,
        llm_config=LLM_CONFIG,
    )

    return agent


def create_user_proxy():
    user_proxy = ConversableAgent(
        name="User",
        llm_config=False,
        is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
        human_input_mode="NEVER",
    )

    return user_proxy


def main():
    user_proxy = create_user_proxy()
    code_generator_agent = create_code_generator_agent()
    user_proxy.initiate_chat(
        code_generator_agent,
        message="""
                    Title: Average of numbers.
                    Write a Python function that takes a list of numbers and returns the average of the numbers.
                """
    )


if __name__ == "__main__":
    main()