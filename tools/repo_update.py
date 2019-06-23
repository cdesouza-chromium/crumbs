#!/usr/bin/env python
# Copyright (c) 2019 Crumbs Project. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Syncs the repo with the latest chromium version.

This script tries to get to the origin/master version of the dependent deps and
files.
"""

import ast
import argparse
import os
import subprocess
import re
import sys

# The separator used by deps roll for each dependecy passed to it.
ROLL_DEPS_DEPENDNECY_SEPARATOR = ' '

def run_command(cmd):
  """Small utility function to run a command.

  Prints out the command before running.
  """
  print('>> RUNNING : <<\n %s' % (' '.join(cmd)))
  subprocess.check_call(cmd)


def process_project_deps(path, project):
  local_scope = {}
  global_scope = {'Var': lambda var_name: '{%s}' % var_name}

  eval(compile(open(path).read(), '<unknown>', 'exec'), global_scope, local_scope)

  deps_dict = {}
  deps_dict.update(local_scope.get('deps', {}))

  project_prefix = "{%s_git}" %project
  deps_to_update = []

  for dep, value in deps_dict.items() :
    if isinstance(value, basestring) and value.startswith(project_prefix):
      deps_to_update.append(dep)

  roll_dep_cmd = [
      'roll-dep',
      '--ignore-dirty-tree',
  ]

  roll_dep_cmd.extend(deps_to_update)
  run_command(roll_dep_cmd)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('projects', nargs='+', help='Project to update (e.g. chromium)')
    args = parser.parse_args()

    tool_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(tool_dir)
    deps_path = os.path.join(root_dir, 'DEPS');
    os.chdir(root_dir)

    for project in args.projects:
      process_project_deps(deps_path, project)

    return 0

if __name__ == '__main__':
  sys.exit(main())
