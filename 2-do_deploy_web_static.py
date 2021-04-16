#!/usr/bin/python3
""" Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy. """
from fabric.api import local, hide, env, run, put
from datetime import datetime
import os
env.user = "ubuntu"
env.hosts = ["104.196.120.195", "34.74.6.247"]


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """ Deploy the archive and configure the web server """

    if not os.path.exists(archive_path):
        return(False)
    try:
        put(archive_path, "/tmp/")
        folder_path = "/data/web_static/releases/" + archive_path[9:-4]
        name_file = archive_path[9:]
        name_folder = archive_path[9:-4]
        date = archive_path[21:-4]
        releases = "/data/web_static/releases/"

        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(name_file, folder_path))
        run("rm /tmp/{}".format(name_file))
        run("mv {}{}/web_static/* {}{}/"
            .format(releases, name_folder, releases, name_folder))
        run("rm -rf {}{}/web_static".format(releases, name_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print("New version deployed!")

        return(True)
    except BaseException:
        return (False)
