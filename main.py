import requests
import subprocess
import logging
import colorlog
from pathlib import Path
import urllib3


def test_repo(data):
    try:
        log.warning("Testing repo")
        token = exec_cmd(f"moken UNNCHANC", True)
        for repo, branch, node, url in data:
            if url:
                link = url + token
                response = requests.get(link, verify=False)
                log.info(repo)
                log.debug(link)
                log.info("PASS") if response.status_code == 200 else log.error("FAIL")
    except Exception as e:
        log.debug("Error occurring test repo")
        raise e


def manage_repo(repo, branch, node, folder):
    try:
        path = folder / repo
        source = path / "dist" / repo
        dest = folder / "phxinvweb" / "public" / repo
        url = "https://git.matador.ais.co.th/vhlinventory/"
        # Clone
        if not path.exists():
            exec_cmd(f"git clone {url}{repo} --single-branch -b {branch} {path}")
        # Setup
        status = exec_cmd(f"cd {path} && git pull")
        if not ("Already up to date" in status and (path / "node_modules").is_dir()):
            exec_cmd(f"cd {path} && npm install")

        if repo not in ["phxinvweb", "phxinvapp"]:
            # Build
            if not ("Already up to date" in status and source.exists()):
                if source.exists():
                    exec_cmd(f"rd /s /q {source}")
                exec_cmd(f"cd {path} && npm run ps:build")
            # Copy
            if dest.exists():
                exec_cmd(f"rd /s /q {dest}")
            exec_cmd(f"xcopy /e /h /c /i {source} {dest}")
    except Exception as e:
        log.debug("Error occurring manage repo")
        raise e


def read_file(file):
    with open(file, "r") as f:
        data = [line.strip().split("|") for line in f]
        return data


def exec_cmd(command, hide = False):
    try:
        log.info(f"> {command}")
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        data = stdout.decode().strip()

        if process.returncode != 0:
            raise Exception(stderr.decode().strip())
        if "Access is denied" in data:
            raise Exception("Access is denied")
        if "File(s) copied" in data:
            lines = data.split("\n")
            data = lines[-1]

        if not hide: 
            log.debug(data)
        return data
    except Exception as e:
        log.debug("Error occurring execute command")
        raise e


def init_log():
    # Disable warnings about insecure requests
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # Hide logging for 'requests' and 'urllib3'
    logging.getLogger('requests').setLevel(logging.WARNING)
    logging.getLogger('urllib3').setLevel(logging.WARNING)

    handler = colorlog.StreamHandler()
    formatter = colorlog.ColoredFormatter(
        "%(asctime)s %(log_color)s%(levelname)s: %(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    logger = colorlog.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger


def main():
    try:
        folder = Path("_keep")
        folder.mkdir(parents=True, exist_ok=True)
        data = read_file("repo.csv")

        print(f"0 = Skip to Test")
        for index, item in enumerate(data):
            print(f"{index+1} = {item[0]}")

        range_input = input("Enter range (e.g., 1:3) or '0' ")
        if range_input != '0':
            start, end = map(int, range_input.split(':'))

            if not 0 < start <= end <= len(data):
                raise Exception("Invalid range input")

            for repo, branch, node, url in data[start - 1:end]:
                log.warning(f"{repo} is starting")
                exec_cmd(f"nvm use {node}")
                manage_repo(repo, branch, node, folder)

        exec_cmd("nvm use 16.15.0")
        text = input("Prepared for testing? (Y/n) ")
        if text.lower() not in ["y", ""]:
            raise KeyboardInterrupt
        test_repo(data)
        input("Press Enter to exit...")

    except KeyboardInterrupt:
        log.critical("Terminated by user")
        input("Press Enter to exit...")
    except Exception as e:
        log.error(str(e))
        input("Press Enter to exit...")


if __name__ == "__main__":
    log = init_log()
    main()
