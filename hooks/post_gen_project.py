from cookiecutter.utils import rmtree
from cookiecutter.main import cookiecutter
import os
import json

def main():
    # current directory is the new generated Python project
    project_dir = os.getcwd()
    docs_dir = os.path.join(project_dir, "docs")

    # load the original context from cookiecutter.json (created automatically)
    context_file = os.path.join(project_dir, "cookiecutter.json")
    if os.path.exists(context_file):
        with open(context_file) as f:
            ctx = json.load(f)
    else:
        # fallback if not found
        ctx = {}

    # build the extra context for the Jekyll template
    extra_ctx = {
        "project_name": ctx.get("project_name"),
        "github_user": ctx.get("github_user"),
        "version": ctx.get("version"),
        "description": ctx.get("description"),
        "ga_tracking": ctx.get("ga_tracking"),
        "buy_me_a_coffee": ctx.get("buy_me_a_coffee"),
        "theme": ctx.get("github_docs_theme")
    }

    print(f"📘 Generating GitHub Docs for {extra_ctx['project_name']}...")

    cookiecutter(
        "https://github.com/jcook3701/github-docs-cookiecutter",
        no_input=True,
        extra_context=extra_ctx,
        output_dir=docs_dir
    )

if __name__ == "__main__":
    main()
