from prefect.deployments import Deployment
from prefect.filesystems import GitHub
from prefect.infrastructure import DockerContainer

import flows


def create_storage():
    storage = GitHub(
        repository="https://github.com/EmilRex/multi-container-demo.git",
        reference="main",
    )
    storage.save("multi-container-demo-main", overwrite=True)


def create_deployment(flow, image_tag):
    deployment = Deployment.build_from_flow(
        flow=flow,
        name=f"main-{image_tag.replace('.', '-')}",
        work_queue_name="multi-container-demo",
        storage=GitHub.load("multi-container-demo-main"),
        infrastructure=DockerContainer(
            image=f"prefecthq/prefect:{image_tag}", auto_remove=True
        ),
    )
    deployment_id = deployment.apply()
    print(f"Created deployment with ID {deployment_id}")


if __name__ == "__main__":
    create_storage()
    create_deployment(flows.version, "2.8.5-python3.10")
    create_deployment(flows.version, "2.8.6-python3.10")
    create_deployment(flows.version, "2.8.7-python3.10")
    create_deployment(flows.parent, "2-latest")
