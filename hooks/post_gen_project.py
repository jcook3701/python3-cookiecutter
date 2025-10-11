import os
import subprocess
from cookiecutter.main import cookiecutter

def main():
    project_dir = os.getcwd()
    docs_dir = os.path.join(project_dir, "docs")

    # Load the name from your context
    project_name = os.path.basename(project_dir)
    jekyll_template = "{{ cookiecutter.jekyll_docs_template_url }}"

    print(f"Generating Jekyll docs from {jekyll_template}...")

    cookiecutter(
        jekyll_template,
        no_input=True,
        extra_context={
            "project_name": project_name,
        },
        output_dir=docs_dir
    )

if __name__ == "__main__":
    main()
