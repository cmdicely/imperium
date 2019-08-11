#!/usr/bin/env python
# -*- coding: utf-8 -*
"""
Imperium's CLI
"""

__copyright__ = "Copyright 2019, Christopher M. Dicely"
__license__ = "GPL-2.0-only"
# This program is free software; you can redistribute it 
# and/or modify it under the terms of the GNU General Public License 
# as published by the Free Software Foundation; version 2.

import click

@click.group()
def cli():
    pass

@cli.command()
def new_game():
    click.echo("New game!")

if __name__ == "__main__":
    cli()
