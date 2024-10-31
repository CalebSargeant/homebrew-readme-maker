from config import load_config, load_api_key
from git_utils import get_repo_name
from file_collector import collect_files_content
from prompt_builder import construct_prompt
from openai_client import call_openai_api

def main():
    file_types, ignore_patterns = load_config()
    repo_name = get_repo_name()
    api_key = load_api_key()
    files_content = collect_files_content(file_types, ignore_patterns)
    prompt = construct_prompt(repo_name, files_content)
    readme_content = call_openai_api(prompt, api_key)

    # Write to README.md
    with open("../README.md", "w") as file:
        file.write(readme_content)
    print("README.md generated successfully.")

if __name__ == "__main__":
    main()