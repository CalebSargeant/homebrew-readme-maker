# readme-maker

## Project Overview
`readme-maker` is a powerful tool designed to automate the generation of high-quality README files for code repositories. By leveraging the OpenAI API, it analyzes the structure and content of a repository, including its code, configurations, and dependencies, to produce a well-structured and informative README.md file. This project is particularly useful for developers looking to enhance their project's documentation without the manual effort typically required.

## Features
- **Automated README Generation**: Automatically creates a README.md file based on the contents of your repository.
- **Customizable Configuration**: Users can specify file types to include and patterns to ignore through a configuration file.
- **OpenAI Integration**: Utilizes the OpenAI API to ensure the generated documentation is clear, concise, and adheres to industry standards.
- **Error Handling**: Provides informative error messages for missing configurations or API keys, ensuring a smooth user experience.

## Installation and Setup
### Prerequisites
- Python 3.6 or higher
- An OpenAI API key (store it in `~/.openai`)

### Dependencies
- `requests`
- `pyyaml`

### Setup Steps
1. Install the required dependencies:
   ```bash
   pip install requests pyyaml
   ```
2. Create a configuration file named `config.yaml` in the project root with the following structure:
   ```yaml
   file_types:
     - "*.py"
     - "*.md"
   ```
3. Ensure your OpenAI API key is saved in `~/.openai`.

## Directory Structure
```
.
├── config.py            # Handles loading configuration and API key.
├── file_collector.py    # Collects files based on specified types and ignores patterns.
├── git_utils.py         # Utility functions for interacting with Git repositories.
├── LICENSE              # License information for the project.
├── prompt_builder.py     # Constructs the prompt for the OpenAI API.
├── readme.py            # Main script to generate the README.md file.
└── openai_client.py     # Manages interactions with the OpenAI API.
```

## Usage
To generate a README.md file, simply run the main script:
```bash
python readme.py
```
This command will analyze the repository, collect relevant file contents, and generate a README.md file in the project root.

## Configuration
The configuration for `readme-maker` is managed through the `config.yaml` file. Here’s a sample configuration:
```yaml
file_types:
  - "*.py"
  - "*.md"
```
You can customize the `file_types` list to include any file extensions relevant to your project.

## Troubleshooting and Known Issues
- **Missing Configuration File**: Ensure that `config.yaml` exists in the project root and is correctly formatted.
- **API Key Not Found**: Make sure your OpenAI API key is stored in `~/.openai`.
- **Not in a Git Repository**: The script must be run inside a Git repository. Ensure you are in the correct directory.

## Contributing
Contributions are welcome! Please adhere to the following guidelines:
- Follow the existing coding style and conventions.
- Submit pull requests for any changes or enhancements.
- Ensure that your code is well-documented and tested.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.