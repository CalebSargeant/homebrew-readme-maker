def construct_prompt(repo_name, files_content):
    return f"""
    The repository '{repo_name}' contains code, configurations, and dependencies. Generate a high-quality, structured README.md file to provide clear, concise, and comprehensive documentation for this project. The README should be written to a high industry standard, with unique clarity and efficiency. Skip the detail on how to clone a repo. Your exact output is the exact contents of the README.md file; therefore, you must begin the README by writing "# {repo_name}" as the title, not "``` markdown".

    Include the following sections, formatted and explained clearly:
    - **Project Overview**: Describe the purpose and primary functionality of this project in a way that highlights its unique aspects or use cases.
    - **Features**: Briefly list core features or functionalities that make this project stand out.
    - **Installation and Setup**: Include any prerequisites, dependencies, and setup steps specific to this project. Avoid generic Git clone instructions but ensure any essential project-specific setup steps are covered.
    - **Directory Structure**: Summarise the main directories and files with a brief explanation of each component’s role in the project.
    - **Usage**: Provide clear instructions or examples for running the project, key commands, or common workflows users may need to know.
    - **Configuration**: Outline any configurations or settings that can be customised, particularly those controlled by configuration files, with sample configurations if appropriate.
    - **Troubleshooting and Known Issues**: Note any common issues, setup mistakes, or potential conflicts and recommend solutions.
    - **Contributing**: Briefly mention any guidelines for contributors, such as coding standards or pull request preferences.
    - **License**: Specify the license and include a link if a license file exists.

    Here are some file summaries to use for generating this README:\n\n{files_content}
    """