# !/usr/bin/env python
#  -*- coding: UTF-8 -*-
"""
ONTOSPY
Copyright (c)  __Michele Pasin__ <http://www.michelepasin.org>.
All rights reserved.

"""

from __future__ import print_function

import sys
import os
import time
import optparse
import os.path
import shutil
import requests

try:
    import cPickle
except ImportError:
    import pickle as cPickle

try:
    import urllib2
except ImportError:
    import urllib as urllib2

# Fix Python 2.x.
try:
    input = raw_input
except NameError:
    pass

import click
# http://click.pocoo.org/5/python3/
click.disable_unicode_literals_warning = True

from . import *  # imports __init__
from .VERSION import *

from .core.actions import *
from .core.ontospy import Ontospy
from .core.manager import *
from .core.utils import *

SHELL_EXAMPLES = """
Quick Examples:

  > ontospy ~/Desktop/mymodel.rdf          # ==> inspect a local RDF file
  > ontospy -l                             # ==> list ontologies available in the local library
  > ontospy -s http://xmlns.com/foaf/spec/ # ==> download FOAF vocabulary and save it in library

More info: <ontospy.readthedocs.org>
------------
"""

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

##################
#
#  COMMAND LINE MAIN METHODS
#
##################
#
# 2018-08-23: trying to restructure the cli using command groups
# http://click.pocoo.org/6/commands/
# test with python -m ontospy.cli library


@click.group()
def main_cli():
    click.secho("OntoSpy " + VERSION, bold=True)
    # click.secho("Local library: '%s'" % get_home_location(), fg='white')
    click.secho("------------", fg='white')
    # verbose option would go here


@main_cli.command()
def library():
    click.echo(
        "Library: here we can add boostrap/cache/delete/list/save/reset/update"
    )
    # delete and reset could be unified (reset = delete + *)
    # by default it shows the library


@main_cli.command()
def shell():
    click.echo(
        "Shell: launche the shell. If an arg is provided loads it into it too")


@main_cli.command()
def analyze():
    click.echo(
        "Open: main command for inspecting stuff. HEre we can add --endpoint ")
    # add web option here too?


@main_cli.command(context_settings=CONTEXT_SETTINGS)
@click.argument('sources', nargs=-1)
@click.option(
    '--serialize', '-s', help='Serialize: from one serialization to another.')
@click.pass_context
def utils(ctx, sources=None, serialize="ttl"):
    """Desc here
    """
    click.echo("Utils group")
    if sources:
        action_transform(sources, serialize)
    else:
        click.echo(ctx.get_help())


if __name__ == '__main__':
    import sys
    try:
        main_cli(prog_name='ontospy')
        sys.exit(0)
    except KeyboardInterrupt as e:  # Ctrl-C
        raise e