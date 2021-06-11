#!/usr/bin/python3
""" Ship front end bundle to our server """
import os.path
from fabric.api import local, env, put, run


env.hosts = ['54.152.238.19']

def deploy():
    """ Convenient compiled function that deploys """
    archive = do_pack()
    if archive is None:
        return False
    status = do_deploy(archive)
    return status


def do_deploy(archive_path):
    """ Deploy sit to server index """
    
    if not os.path.exists(archive_path):
        return False
    try:
        archiveName = archive_path[9:]
        archiveNameWithoutExtension = archiveName[:-4]

        put(archive_path, '/tmp/' + archiveName)
        run('mkdir -p /data/web_static/releases/' + archiveNameWithoutExtension)
        run('tar -xzvf /tmp' + archiveName + ' -C ' + '/data/web_static/releases/' + archiveNameWithoutExtension + ' --strip-components=1')
        run('rm -f /tmp/' + archiveName)
        run('rm -f /data/web_static/current')
        run('ln -sf /data/web_static/releases/' + archiveNameWithoutExtension + ' /data/web_static/current')
        local('rm -r ' + archive_path)
        local('rm /data/web_static/current')
        return True
    except:
        return False

def do_pack():
    """ Pack up the front end """
    now = datetime.now()

    tarArchiveName = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
    tarArchivePath = "versions/" + tarArchiveName

    local("mkdir -p versions")
    local("tar -czvf " + tarArchivePath + " web_static")        
