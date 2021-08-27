#!/usr/bin/python3
"""Write a Fabric script (based on the file 1-pack_web_static.py)"""
import os
from fabric.api import put, run, env
from datetime import datetime


def do_deploy(archive_path):
    '''distributes an archive to your web servers, using the function do_deploy
    '''