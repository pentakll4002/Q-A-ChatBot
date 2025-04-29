def get_engine(name):
    engines = {
        "ollama": "gemma3:1b",
        "deepseek": "deepseek-r1",
    }
    return engines.get(name, "deepseek-r1")