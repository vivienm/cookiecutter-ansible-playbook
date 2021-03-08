import os
import secrets
import string
import subprocess


def setup_vcs() -> None:
    if "{{ cookiecutter.version_control }}" == "git":
        subprocess.run(["git", "init"], check=True)
    else:
        os.remove(".gitignore")


BASE64_CHARS = (string.ascii_letters + string.digits + "+/").encode()


def setup_vault_pass() -> None:
    passphrase = bytes((secrets.choice(BASE64_CHARS) for _ in range(64)))
    subprocess.run(
        [
            "gpg",
            "--sign",
            "--encrypt",
            "--armor",
            *(
                "--recipient={}".format(recipient.strip())
                for recipient in "{{ cookiecutter.gpg_recipients }}".split(",")
            ),
            "--output=.vault_pass.asc",
        ],
        input=passphrase,
        check=True,
    )


def main() -> None:
    setup_vcs()
    setup_vault_pass()


if __name__ == "__main__":
    main()
