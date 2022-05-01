#!/usr/bin/python
import click
import routeros_api
from config import *

@click.group()
def cli():
    """Mikrotik LTE AT Commands Runner"""
    pass

@cli.command(name='run')
@click.option('--chat', '-c', required=True)
def run_command(chat):
    """Run Commands"""
    connection = routeros_api.RouterOsApiPool(ip, username=username, password=password, plaintext_login=True)
    api = connection.get_api()
    out = api.get_resource("/interface/lte").call("at-chat", {"number": lte, "input":chat})[0]['output']
    print(out)
    connection.disconnect()
    
if __name__ == '__main__':
    cli()