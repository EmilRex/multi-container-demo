# Multi Container Demo

This repo demonstrates how to run flows in different containers using a single parent flow. This pattern is useful when a single flow needs different versions of dependencies.

## Getting Started

The demo assumes you have Docker installed and running.

```bash
# Install Prefect and login to Cloud if you haven't already
pip install -U prefect
prefect cloud login

# Clone this repository
git clone git@github.com:EmilRex/multi-container-demo.git
cd multi-container-demo

# Create the storage block and deployments
python deploy.py

# Run the parent flow and start an agent to execute
prefect deployment run parent/main-2-latest
prefect agent start -q multi-container-demo
```
