#!/usr/bin/env python3

import configparser
import subprocess


class InstallDeployDependencies:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('deploy/config.cfg')

    def run(self):
        print('\n==== Install Deploy Dependencies ====\n')
        print('* APT packages')
        command = 'apt-get -qq update && apt-get -qq upgrade && apt-get -qq install build-essential git python3 python3-dev python3-pip python3-setuptools'
        apt_process = subprocess.Popen(command, shell=True)
        apt_process.wait()

        print('* pip3 packages')
        pip_process = subprocess.Popen('pip3 install -Uq gitpython wheel', shell=True)
        pip_process.wait()

if __name__ == '__main__':
    install = InstallDeployDependencies()
    install.run()
