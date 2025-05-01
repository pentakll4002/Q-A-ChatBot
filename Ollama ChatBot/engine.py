def get_engine(name):
    engines = {
        "gemma": "gemma3:1b",
        "deepseek": "deepseek-r1",
        "ollama": "llama3.2",
        "moondream": "moondream"
    }
    return engines.get(name, "deepseek-r1")