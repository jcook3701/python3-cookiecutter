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
import shutil

def main():
   # Detect CI (e.g. GitHub Actions, GitLab CI, etc.)
    if os.getenv("CI"):
        print("⚙️  Detected CI environment — skipping GitHub Docs generation.")
        return
    
    # current directory is the new generated Python project
    project_dir = os.getcwd()
    docs_dir = os.path.join(project_dir, "docs")
    jekyll_dir = os.path.join(docs_dir, "jekyll")

    # load the original context from cookiecutter.json (created automatically)
    context_file = os.path.join(project_dir, "cookiecutter.json")
    if os.path.exists(context_file):
        with open(context_file) as f:
            ctx = json.load(f)
    else:
        # fallback if not found
        ctx = {}

    # Use environment variables set by Cookiecutter
    extra_ctx = {
        "project_name": os.environ.get("COOKIECUTTER_PROJECT_NAME"),
        "author": os.environ.get("COOKIECUTTER_AUTHOR"),
        "version": os.environ.get("COOKIECUTTER_VERSION"),
        "description": os.environ.get("COOKIECUTTER_DESCRIPTION"),
        "theme": os.environ.get("COOKIECUTTER_GITHUB_DOCS_THEME"),
        "ga_tracking": os.environ.get("COOKIECUTTER_GA_TRACKING"),
        "github_username": os.environ.get("COOKIECUTTER_GITHUB_USERNAME"),
        "linkedin_usercode": os.environ.get("COOKIECUTTER_LINKEDIN_USERCODE"),
        "twitter_username": os.environ.get("COOKIECUTTER_TWITTER_USERNAME"),
        "buymeacoffee_username": os.environ.get("COOKIECUTTER_BUYMEACOFFEE_USERNAME"),
    }

    print(f"📘 Generating GitHub Docs for {extra_ctx.get('project_name', '(unknown)')}...")

    # Temporary output dir so Cookiecutter doesn't create a nested folder we don't want
    tmp_dir = os.path.join(docs_dir, "_tmp_docs")
    os.makedirs(tmp_dir, exist_ok=True)    
    
    try:
        cookiecutter(
            "https://github.com/jcook3701/github-docs-cookiecutter",
            no_input=True,
            extra_context=extra_ctx,
            output_dir=tmp_dir
        )
        
        # Move everything from the nested folder into ./docs/jekyll
        nested = os.path.join(tmp_dir, os.listdir(tmp_dir)[0])
        os.makedirs(jekyll_dir, exist_ok=True)
        for item in os.listdir(nested):
            shutil.move(os.path.join(nested, item), jekyll_dir)

        # Cleanup temporary folder
        shutil.rmtree(tmp_dir)

        print(f"✅ Docs generated in {jekyll_dir}")
        
    except Exception as e:
        print(f"⚠️  Skipping GitHub Docs generation: {e}")

if __name__ == "__main__":
    main()
