import os
import yaml

def load_config():
    config_file = os.path.join(os.path.dirname(__file__), "config.yaml")
    if not os.path.isfile(config_file):
        print(f"Configuration file not found: {config_file}")
        exit(1)

    with open(config_file, "r") as file:
        config = yaml.safe_load(file)
    file_types = config.get("file_types", [])

    gitignore_file = "../.gitignore"
    ignore_patterns = []
    if os.path.isfile(gitignore_file):
        with open(gitignore_file, "r") as gitignore:
            ignore_patterns = [line.strip() for line in gitignore if line.strip() and not line.startswith("#")]

    return file_types, ignore_patterns

def load_api_key():
    api_key_path = os.path.expanduser("~/.openai")
    if not os.path.isfile(api_key_path):
        print("API key not found. Please store your OpenAI API key in ~/.openai")
        exit(1)

    with open(api_key_path, "r") as file:
        return file.read().strip()