#!/usr/bin/python3
""" Module for HBNB project """

from datetime import datetime
from fabric.api import local
from os.path import isdir

def do_pack():
    """ Generate a .tgz archive from the contents """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("version") == False:
            local("mkdir version")
        name = "version/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(name))
        return name
    except:
        return None
