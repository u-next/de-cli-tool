import click
from utils.run_shell import run_shell


@click.command()
@click.argument("env")
@click.option(
    "--filter",
    default="",
    help="Filter services by name. Only services containing this string will be listed.",
)
def show_external_ip(env, filter):
    """
    List the external IP addresses of the services in the dev/prod GKE cluster \n
    Example: \n
        show-external-ip dev \n
        show-external-ip prod --filter kafka \n
    """
    if env not in ["dev", "prod"]:
        click.echo("Invalid environment. Please choose either 'dev' or 'prod'.")
        return

    cluster_name = f"de-{env}-gke-cluster"
    run_shell(
        f"gcloud container clusters get-credentials {cluster_name} --zone asia-northeast1-a --project un-de-sawmill"
    )

    if filter:
        kubectl_command = (
            "kubectl get svc -A -o json | "
            'jq -r \'["Namespace", "Name", "ExternalIP", "Ports"], '
            f'(.items[] | select(.spec.type=="LoadBalancer" and (.metadata.name | test("{filter}"; "i"))) | '
            "[.metadata.namespace, .metadata.name, "
            '(.status.loadBalancer.ingress[0].ip // "None"), '
            '(.spec.ports | map(.name + ":" + (.port | tostring)) | join(", "))]) | @tsv\' | '
            "column -t"
        )
    else:
        kubectl_command = (
            "kubectl get svc -A -o json | "
            'jq -r \'["Namespace", "Name", "ExternalIP", "Ports"], '
            '(.items[] | select(.spec.type=="LoadBalancer") | '
            "[.metadata.namespace, .metadata.name, "
            '(.status.loadBalancer.ingress[0].ip // "None"), '
            '(.spec.ports | map(.name + ":" + (.port | tostring)) | join(", "))]) | @tsv\' | '
            "column -t"
        )
    run_shell(kubectl_command)
