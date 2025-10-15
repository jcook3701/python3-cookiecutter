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
    tmp_dir = os.path.join(docs_dir, "_tmp_docs")

    os.makedirs(tmp_dir, exist_ok=True)
    
    # Use Cookiecutter context
    context = os.environ.get('COOKIECUTTER_CONTEXT')
    if context:
        import json
        ctx = json.loads(context)
    else:
        # fallback if not found
        ctx = {}

    # ⚙️ These placeholders are rendered *before* this hook runs.
    extra_ctx = {
        "project_name": "{{ cookiecutter.project_name }}",
        "author": "{{ cookiecutter.author }}",
        "version": "{{ cookiecutter.version }}",
        "description": "{{ cookiecutter.description }}",
        "theme": "{{ cookiecutter.github_docs_theme }}",
        "ga_tracking": "{{ cookiecutter.ga_tracking }}",
        "github_username": "{{ cookiecutter.github_username }}",
        "linkedin_usercode": "{{ cookiecutter.linkedin_usercode }}",
        "twitter_username": "{{ cookiecutter.twitter_username }}",
        "buymeacoffee_username": "{{ cookiecutter.buymeacoffee_username }}",
    }

    print(f"📘 Generating GitHub Docs for {extra_ctx.get('project_name', '(unknown)')}...")
    
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
