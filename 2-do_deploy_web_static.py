#!/usr/bin/python3
""" Ship front end bundle to our server """
import os.path
from fabric.api import local, env, put, run
from datetime import datetime


env.hosts = ['54.152.238.19']

def do_deploy(archive_path):
    """ Deploy sit to server index """

    if not os.path.exists(archive_path):
        return False
    try:
        archiveName = archive_path[9:]
        archiveNameWithoutExtension = archiveName[:-4]

        put(archive_path, '/tmp/' + archiveName)
        run('mkdir -p /data/web_static/releases/' + archiveNameWithoutExtension)
        run('tar -xzvf /tmp/' + archiveName + ' -C ' + '/data/web_static/releases/' + archiveNameWithoutExtension + ' --strip-components=1')
        run('rm -f /tmp/' + archiveName)
        run('rm -f /data/web_static/current')
        run('ln -sf /data/web_static/releases/' + archiveNameWithoutExtension + ' /data/web_static/current')
        return True
    except:
        return False
