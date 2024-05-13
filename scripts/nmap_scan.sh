#!/bin/bash
# Gán đầu vào cho biến target
#-sC -A
target="$1"
nmap -F -T4  -sV   "$target" -oX /root/Desktop/final/scripts/output/nmap_out.xml  
cd scripts/nmap-formatter && go run . html /root/Desktop/final/scripts/output/nmap_out.xml > /root/Desktop/final/scripts/output/nmap_out.html
