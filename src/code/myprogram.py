import click

from pathlib import Path
import os.path


def regular_function():
    results = []
    if os.path.exists("path1"):
        results.append("Exist")
    if not os.path.exists("/tmp"):
        results.append("Does not exist")
    return results


@click.command()
def command_foo_os():
    results = []
    if os.path.exists("path1"):
        results.append("Exist")
    if not os.path.exists("/tmp"):
        results.append("Does not exist")
    click.echo(results)
    return results


@click.command()
def command_foo_pathlib():
    results = []
    if Path.exists("path1"):
        results.append("Exist")
    if not Path.exists("/tmp"):
        results.append("Does not exist")
    click.echo(results)
    return results
