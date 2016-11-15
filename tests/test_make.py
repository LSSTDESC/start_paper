#!/usr/bin/env python
"""
Test latex compilation script
"""
__author__ = "Alex Drlica-Wagner"

import os
from subprocess import Popen, PIPE
import unittest

srcdir="./{{cookiecutter.folder_name}}"

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
        os.chdir(srcdir)

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

    @classmethod
    def create_method(cls, args):
        def test_method(self):
            if isinstance(args,basestring): self.runcmd(args)
            else: self.runcmd(' '.join(args))
        test_method.__name__ = 'test_%s'%('_'.join(args))
        return test_method

    @classmethod
    def create_methods(cls, args):
        for arg in args:
            test_method = TestMake.create_method(arg)
            setattr(cls, test_method.__name__, test_method)

TestMake.create_methods(commands)

if __name__ == "__main__":
    unittest.main()
