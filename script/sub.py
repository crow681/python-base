#!/usr/bin/env python3.9
# -*- coding: utf-8 -*-
# @Time    : 2022/8/14 20:57
# @Author  : wangjun
# @File    : sub.py

import subprocess

def invoke(cmd):
    try:
        cmd = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out = cmd.stdout.read().decode('GBK')
        return out
    except:
        raise


out = invoke(cmd='pip list')
print(out)
