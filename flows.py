import subprocess

from prefect import flow, task, get_run_logger
from prefect.deployments import run_deployment


@flow
def version():
    """Capture 'prefect version' in logs"""
    p = subprocess.run(["prefect", "version"], capture_output=True, encoding="ascii")
    logger = get_run_logger()
    for line in p.stdout.strip().splitlines():
        logger.info(line)


@task
def run_deployment_task(deployment_name):
    """Run the deployment in a task for async execution"""
    run_deployment(
        name=f"version/{deployment_name}",
    )


@flow
def parent():
    """Run three deployments in different docker containers"""
    deployment_names = [
        "main-2-8-5-python3-10",
        "main-2-8-6-python3-10",
        "main-2-8-7-python3-10",
    ]
    for deployment_name in deployment_names:
        run_deployment_task.submit(
            deployment_name,
        )


if __name__ == "__main__":
    parent()
