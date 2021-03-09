import os

import nox


@nox.session(venv_backend="none")
def ansible_lint(session):
    session.run("ansible-lint")


@nox.session(venv_backend="none")
@nox.parametrize("playbook", sorted(os.listdir("playbooks")))
def ansible_syntax(session, playbook):
    session.run("ansible-playbook", "--syntax-check", f"playbooks/{playbook}")


@nox.session(venv_backend="none")
def yamllint(session):
    session.run("yamllint", ".")
