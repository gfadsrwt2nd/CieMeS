#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This is a part of CieMeS, check the LICENSE file for more information
# Rex4 - Cantix Crew

import os
import ciemesdb.basic as ciemes

def start(version):
    if version != '0':
        vuln_file = os.getcwd() + '/deepscans/joom/database/corevul.txt' # shoutouts to joomscan
        if os.path.isfile(vuln_file):
            vuln_detection = '1' # version detection successful and vuln db loaded as well
            vuln_count = 0
            joom_vulns = []
            f = open(vuln_file, 'r')
            vuln_db = f.read()
            vulns = vuln_db.split('\n')
            for vuln in vulns:
                if version in vuln:
                    ciemes.warning('Joomla core vulnerability detected')
                    vuln_count += 1
                    vul = vuln.split('|')
                    # print(vul[1])
                    joom_vulns.append(vul[1])
            return [vuln_detection, vuln_count, joom_vulns]
        else:
            vuln_detection = '3' # version was detected but vulnerability database not found
            vuln_count = 0
            joom_vulns = []
            return [vuln_detection, vuln_count, joom_vulns]

    else:
        vuln_detection = '2' # detection failed due to no version info
        vuln_count = 0
        joom_vulns = []
        return [vuln_detection, vuln_count, joom_vulns]
