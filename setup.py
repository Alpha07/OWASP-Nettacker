#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from setuptools import setup

setup(
    name='OWASP-Nettacker',
    version='0.0.1',
    packages=['lib', 'lib.icmp', 'lib.scan', 'lib.scan.dir', 'lib.scan.subdomain', 'lib.scan.tcp_connect_port',
              'lib.scan.viewdns_reverse_ip_lookup', 'lib.brute', 'lib.brute.ftp', 'lib.brute.ssh', 'lib.brute.smtp',
              'lib.graph', 'lib.graph.d3_tree_v1', 'lib.graph.d3_tree_v2', 'lib.graph.jit_circle_v1', 'lib.argparse',
              'lib.argparse.v2' if int(sys.version_info[0]) is 2 else 'lib.argparse.v3', 'lib.html_log', 'lib.language',
              'lib.socks_resolver', 'core'],
    url='https://github.com/viraintel/OWASP-Nettacker',
    license='Apache-2.0',
    author='Ali Razmjoo',
    author_email='ali.razmjoo@owasp.org',
    description='Automated Penetration Testing Framework - OWASP Nettacker project is created to'
                ' automate information gathering, vulnerability scanning and eventually generating'
                ' a report for networks, including services, bugs, vulnerabilities, misconfigurations,'
                ' and other information. This software will utilize TCP SYN, ACK, ICMP and many other'
                ' protocols in order to detect and bypass Firewall/IDS/IPS devices. By leveraging a'
                ' unique method in OWASP Nettacker for discovering protected services and devices such'
                ' as SCADA. It would make a competitive edge compared to other scanner making it one of'
                ' the bests.'
)
