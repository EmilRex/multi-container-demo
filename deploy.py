from prefect.deployments import Deployment
from prefect.filesystems import GitHub
from prefect.infrastructure import DockerContainer

import flows


def create_deployment(flow, image_tag):
    deployment = Deployment.build_from_flow(
        flow=flow,
        name=f"main-{image_tag.replace('.', '-')}",
        work_queue_name="multi-container-demo",
        storage=GitHub(
            repository="https://github.com/EmilRex/multi-container-demo.git",
            reference="main",
        ),
        infrastructure=DockerContainer(
            image=f"prefectHQ/prefect:{image_tag}",
        ),
    )
    deployment_id = deployment.apply()
    print(f"Created deployment with ID {deployment_id}")


if __name__ == "__main__":
    create_deployment(flows.version, "2.6.0")
    create_deployment(flows.version, "2.7.0")
    create_deployment(flows.version, "2.8.0")
    create_deployment(flows.parent, "2-latest")
