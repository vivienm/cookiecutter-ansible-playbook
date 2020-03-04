import os
import secrets
import string
import subprocess


def setup_vcs():
    if "{{ cookiecutter.vcs }}" == "git":
        subprocess.run(["git", "init"], check=True)
    else:
        os.remove(".gitignore")


BASE64_CHARS = (string.ascii_letters + string.digits + "+/").encode()


def setup_vault_pass():
    passphrase = bytes((secrets.choice(BASE64_CHARS) for _ in range(64)))
    subprocess.run(
        [
            "gpg",
            "-a",
            "-o",
            ".vault-pass.asc",
            "-e",
            "-s",
            "-r",
            "{{ cookiecutter.gpg_recipient }}",
        ],
        input=passphrase,
        check=True,
    )


if __name__ == "__main__":
    setup_vcs()
    setup_vault_pass()
