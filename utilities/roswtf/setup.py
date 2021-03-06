#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.package import parse_package_for_distutils

d = parse_package_for_distutils()
d['packages'] = ['roswtf']
d['package_dir'] = {'': 'src'}
d['scripts'] = ['scripts/roswtf']
d['install_requires'] = ['genmsg', 'genpy', 'roslib', 'rospkg']

setup(**d)
