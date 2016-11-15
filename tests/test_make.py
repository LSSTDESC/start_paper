#!/usr/bin/env python
"""
Test latex compilation script
"""
__author__ = "Alex Drlica-Wagner"

import os
import shutil
import logging
from subprocess import Popen, PIPE
import unittest

commands = [
    ['make'],
#    ['make','tex'],
#    ['make','apj'],
#    ['make','apjl'],
#    ['make','prl'],
#    ['make','prd'],
#    ['make','mnras'],
]

class TestMake(unittest.TestCase):

    def setUp(self):
        os.chdir("{{cookiecutter.folder_name}}")

    def tearDown(self):
        self.runcmd('make clean')
        os.chdir("..")

    def runcmd(self, cmd):
        print(cmd)
        p = Popen(cmd.split(),stdout=PIPE,stderr=PIPE)
        stdout,stderr = p.communicate()
        print(stdout)
        if p.returncode > 0:
            raise Exception(stderr)

# Can't be named 'test' or nose will find it
def create_func(args):
    def func(self):
        if isinstance(args,basestring): self.runcmd(args)
        else: self.runcmd(' '.join(args))
    return func

for args in commands:
    test_method = create_func(args)
    test_method.__name__ = 'test_%s' % ('_'.join(args))
    setattr (TestMake, test_method.__name__, test_method)
    # Need to delete the method or nose will find it
    del test_method

if __name__ == "__main__":
    unittest.main()
