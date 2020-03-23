"""CLI interface."""

import click
from .clientPackage import ClientPackage, PythonPackage
from pathlib import Path

all_viable_clients = [PythonPackage]
name_to_client = {clazz.name: clazz for clazz in all_viable_clients}
client_instances = []


def do_client_function(function_name, *args, **kwargs):
    for client in client_instances:
        fun = getattr(client, function_name)
        fun(*args, **kwargs)


@click.group("onshape-clients")
@click.option(
    "-c",
    "--client",
    "clients",
    type=click.Choice(name_to_client.keys(), case_sensitive=False),
    multiple=True,
    help="Clients to perform this action with. Defaults to all. Specify many by: -c python -c java, etc...",
)
@click.option(
    "-r",
    "--repo",
    envvar="ONSHAPE_CLIENTS_REPO",
    help="Path to the onshape clients repo",
    default=Path.cwd().absolute(),
)
def entry(clients, repo):
    if len(clients) == 0:
        clients = name_to_client.keys()
    for client in clients:
        client_instances.append(name_to_client[client](repo=repo))


@entry.command()
@click.option(
    "-v",
    "--version",
    type=click.STRING,
    help="version to publish.",
    envvar="ONSHAPE_CLIENTS_PUBLISH_VERSION",
)
def publish(version):
    do_client_function("set_version", version)
    do_client_function("publish")


@entry.command()
def generate():
    pass


@entry.command()
@click.option(
    "-m", "--marker", type=click.Choice(["fast"]), help="Group of tests to test.",
)
def test(marker):
    do_client_function("test", marker)


@entry.command()
def install():
    do_client_function("install")
