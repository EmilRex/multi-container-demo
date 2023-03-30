import subprocess

from prefect import flow, get_run_logger


@flow
def version():
    """Capture 'prefect version' in logs"""
    p = subprocess.run(["prefect", "version"], capture_output=True, encoding="ascii")
    logger = get_run_logger()
    for line in p.stdout.strip().splitlines():
        logger.info(line)


if __name__ == "__main__":
    version()
