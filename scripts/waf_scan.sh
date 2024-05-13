#!/bin/bash
target="$1"
wafw00f ${target}  -f text -o scripts/output/waf_out.txt  > /dev/null 2>&1
