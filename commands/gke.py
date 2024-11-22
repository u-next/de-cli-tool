import click
from utils.run_shell import run_shell


@click.command()
@click.argument("env")
def show_external_ip(env):
    """
    List the external IP addresses of the services in the dev/prod GKE cluster \n
    Example: \n
        show_external_ip dev \n
        show_external_ip prod \n
    """
    if env not in ["dev", "prod"]:
        click.echo("Invalid environment. Please choose either 'dev' or 'prod'.")
        return
    else:
        cluster_name = f"de-{env}-gke-cluster"
        run_shell(
            f"gcloud container clusters get-credentials {cluster_name} --zone asia-northeast1-a --project un-de-sawmill"
        )
        run_shell("kubectl get svc -A -o json | jq -r '[\"Namespace\", \"Name\", \"ExternalIP\", \"Ports\"], (.items[] | select(.spec.type==\"LoadBalancer\") | [.metadata.namespace, .metadata.name, (.status.loadBalancer.ingress[0].ip // \"None\"), (.spec.ports | map(.name + \":\" + (.port | tostring)) | join(\", \"))]) | @tsv' | column -t")
