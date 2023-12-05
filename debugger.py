#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from ryu.cmd import manager


def main():
    sys.argv.append('/home/vwmin/Desktop/ryu-multicast/gui_topology/gui_topology.py')
    sys.argv.append('--verbose')
    sys.argv.append('--enable-debugger')
    manager.main()


if __name__ == '__main__':
    main()
