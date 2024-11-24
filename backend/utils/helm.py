import subprocess
import yaml

def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        raise Exception(result.stderr.strip())
    return result.stdout.strip()

def get_charts(repo_url):
    run_command(["helm", "repo", "add", "temp-repo", repo_url])
    output = run_command(["helm", "search", "repo", "temp-repo", "-o", "json"])
    run_command(["helm", "repo", "remove", "temp-repo"])
    return yaml.safe_load(output)

def get_chart_values(repo_url, chart_name, version):
    run_command(["helm", "repo", "add", "temp-repo", repo_url])
    output = run_command(["helm", "show", "values", f"temp-repo/{chart_name}", "--version", version])
    run_command(["helm", "repo", "remove", "temp-repo"])
    return yaml.safe_load(output)

def generate_helmrelease(chart_data):
    helmrelease = {
        "apiVersion": "helm.toolkit.fluxcd.io/v2beta1",
        "kind": "HelmRelease",
        "metadata": {"name": chart_data["name"], "namespace": chart_data["namespace"]},
        "spec": {
            "chart": {
                "spec": {
                    "chart": chart_data["chart"],
                    "sourceRef": {"kind": "HelmRepository", "name": chart_data["repo"]},
                    "version": chart_data["version"],
                }
            },
            "values": chart_data["values"],
        },
    }
    return yaml.dump(helmrelease)
