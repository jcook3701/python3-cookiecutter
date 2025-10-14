# coding: utf-8
"""Python3 Cookiecutter Package

© All rights reserved. Jared Cook

See the LICENSE.TXT file for more details.

Author: Jared Cook
"""

from cookiecutter.utils import rmtree
from cookiecutter.main import cookiecutter
import os
import json

def main():
   # Detect CI (e.g. GitHub Actions, GitLab CI, etc.)
    if os.getenv("CI"):
        print("⚙️  Detected CI environment — skipping GitHub Docs generation.")
        return
    
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
        "author": ctx.get("author"),
        "version": ctx.get("version"),
        "description": ctx.get("description"),
        "theme": ctx.get("github_docs_theme"),
        "ga_tracking": ctx.get("ga_tracking"),
        "github_username": ctx.get("github_username"),
        "linkedin_usercode": ctx.get("linkedin_usercode"),
        "twitter_username": ctx.get("twitter_username"),
        "buymeacoffee_username": ctx.get("buymeacoffee_username")
    }

    print(f"📘 Generating GitHub Docs for {extra_ctx.get('project_name', '(unknown)')}...")

    try:
        cookiecutter(
            "https://github.com/jcook3701/github-docs-cookiecutter",
            no_input=True,
            extra_context=extra_ctx,
            output_dir=docs_dir
        )
    except Exception as e:
        print(f"⚠️  Skipping GitHub Docs generation: {e}")

if __name__ == "__main__":
    main()
