# Code Generator Agent

This is boilerplate code for a code generator agent.

## Setup

Install the Python dependencies.

```bash
pip install -r requirements.txt
```

Configure the LLM_CONFIG to match your preferred model 
Docs: https://ollama.com/library/mistral  

The LLM_CONFIG could be configured in the following way:
```python
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
```

## Run the agent

Navigate to the code_generator_agent/agent
```bash
cd code_generator_agent/agent/
```

Run the agent:
```bash
python -m code_generator_agent.py
```

## Requirements

- Python 3.10+ (3.12 preferred)
- autogen
- ollama
- fix-busted-json




