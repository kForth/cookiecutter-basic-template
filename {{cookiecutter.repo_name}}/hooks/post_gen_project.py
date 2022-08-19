{% raw -%}
import logging

logger = logging.getLogger(__name__)

if "{{ cookiecutter.initialize_git_repo | lower }}".strip().startswith("y"):
    import subprocess

    logger.debug("Initializing Git Repo")
    subprocess.call(["git", "init", "-b", "{{ cookiecutter.repo_branch }}"])
    subprocess.call(["git", "remote", "add", "origin", "{{ cookiecutter.repo_url }}"])

if "{{ cookiecutter.license | lower }}".strip() != "agplv3":
    logger.warning("\n".join([
        "",
        "WARNING: Your selected license is different than the default 'AGPLv3'.",
        "Be sure to update your README and LICENSE files accordingly"
    ]))
{%- endraw %}
