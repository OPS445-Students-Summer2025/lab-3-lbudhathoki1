#!/usr/bin/env python3
'''Lab 3 Part 2 - free_space function'''
# Author ID: lbudhathoki

import subprocess

def free_space():
    # Run the 'df -h' command to get disk space info
    p = subprocess.Popen('df -h | grep "/$" | awk \'{print $4}\'', 
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    
    # Capture the output
    output, error = p.communicate()

    # Return the output in utf-8 and strip newline characters
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    # Display free space by calling the free_space function
    print(free_space())
