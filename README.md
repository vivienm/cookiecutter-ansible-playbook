# Ansible playbook template

An opinionated Cookiecutter template for Ansible playbooks.

## Features

* Secret management with [Ansible Vault](https://docs.ansible.com/ansible/latest/user_guide/vault.html) and [GnuPG](https://gnupg.org/).
* Linting with [Ansible Lint](https://ansible-lint.readthedocs.io/) and [yamllint](https://yamllint.readthedocs.io/).
* Testing with [Nox](https://nox.thea.codes/en/stable/).

## Quickstart

Install the latest [Cookiecutter](https://cookiecutter.readthedocs.io/) if you haven't installed it yet.
You can refer to installation instructions [here](https://cookiecutter.readthedocs.io/en/latest/installation.html), or use [pipx](https://pipxproject.github.io/pipx/):

```console
$ pipx install cookiecutter
```

To generate an Ansibple playbook project, run:

```console
$ cookiecutter . -o ~/projects/
```

## Configuration

* `project_name`: The project name, used as toplevel directory name.
* `inventory_hostname`: The inventory name of the first host.
* `ansible_host`: The SSH hostname of the first host.
* `role_name`: The name of the first role.
* `gpg_recipients`: A comma-separated list of GnuPG recipients for the Vault secret passphrase.
* `version_control`: Whether to initialize a new Git repository for the project.
