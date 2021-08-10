# Netmiko is open-source Python library that simplifies SSH management to network devices. This is a common and easy to use library as netmiko supporting multi vendor devices.You can read more about netmiko from here
# https://github.com/ktbyers/netmiko
# Following are the some of the vendor devices supported by Netmiko.
#
# Arista vEOS
# Cisco ASA
# Cisco IOS
# Cisco IOS-XR
# Cisco NX-OS
# Cisco SG300
# HP Comware7
#
# Cisco IOS-XE
# HP ProCurve
# Juniper Junos
# Linux
#
# How to install Netmiko
# Netmiko package not available by default. You should have netmiko library installed on your machine .Following are the steps to download and install netmiko in Python 3.6
#
# Step 1. Working internet connection and Python 3.6 installed on machine
#
# Step 2. On command prompt, type following command, this will automatically fetch netmiko from internet and install on your machine
#
# “python3.8 -m pip install netmiko”
#
#
from netmiko import ConnectHandler
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
from paramiko.ssh_exception import SSHException
import getpass
import sys
# to enable ANSI Support for Windows 10 in func_ansi
import ctypes
# to check the Operating System in func_os_check
import os
import platform
import ipaddress
import subprocess
# import flask


# create a List with IP Addresses to go to
data = open("data.txt", "r")

list_of_data = []

# create device template for netmiko to connect
Devices = {
    'device_type': 'cisco_ios',
    'ip': 'list_of_data',
    'username': 'username',
    'password': 'password',
    'secret': 'password'
}


# to enable ANSI Support for Windows 10
def func_os_check():
    os = platform.system()
    print (os)
    if os == 'Windows':
        func_ansi()
    else:
        pass

# enable ANSI on Win10


def func_ansi():
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)


# read the List of IP Addresses in data.txt
def func_mklist():

    for line in data:
        stripped_line = line.strip()
        # line_list = stripped_line.split()
        list_of_data.append(stripped_line)

# Ping test - does jetzt 1 Ping not used


def func_ping():
    for ip in list_of_data:
        res = subprocess.call(['ping', '-c', '2', ip])
        print(res)


def func_userdata():
    Devices['username'] = input("User name ")
    Devices['password'] = getpass.getpass()
    print ("Input saved for selction")


#
#
# def func_iplist(ipaddr):
#     for ip in ipaddress.IPv4Network('ipaddr'):
#         print(ip)
#
# # read Data
#
#
# def func_readiplist():
#     with open('data.txt', 'r') as file:
#         data = file.read()  # .replace('\n', '')
# #        print(data)
#         func_iplist(data)
#

#


def func_sh_int_status():
    # Getting the user credential

    print ('\x1b[1;31;47m' + "START Script SHOW INT STATUS Please do nothing" + '\x1b[0m')
    for ip in list_of_data:
        #
        # Devices['username'] = input("User name ")
        # Devices['password'] = getpass.getpass()
        Devices['ip'] = (ip)
        # Devices['secret'] = input("Enter enable password")
        # Establishing SSH connection
        try:
            ssh_connect = ConnectHandler(**Devices)

            # changing to enable mode
            # ssh_connect.enable()

            # for ip in list_of_data:
            res0 = ssh_connect.send_command('show int status | inc cted')
            print (res0)
            print ('\x1b[6;30;42m' + "               DONE               " + '\x1b[0m')

            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('func_sh_int_status.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print(res0)
                sys.stdout = original_stdout  # Reset the standard output to its original value

            # ssh_connect.send_command('ip add 10.10.10.1 255.255.255.0')
            # ssh_connect.send_command('end')
            # ssh_connect.send_command('write')
            ssh_connect.disconnect()
        except (AuthenticationException):
            print('\x1b[6;30;41m' + "       Authetication failure: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Authetication failure: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (NetMikoTimeoutException):
            print('\x1b[6;30;41m' + "       Time out from device: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Time out from device: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (EOFError):
            print('\x1b[6;30;41m' + "       End of File reached: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("End of File reached: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (SSHException):
            print('\x1b[6;30;41m' + "       Not able to SSH: Try with Telnet:  " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Not able to SSH: Try with Telnet:  " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except Exception as unknown_error:
            print('\x1b[6;30;41m' + "       other: " + unknown_error + '\x1b[0m')
            continue
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("other: " + unknown_error)
                sys.stdout = original_stdout  # Reset the standard output to its original value


def func_sh_version():

    print ('\x1b[1;31;47m' + "START Script SHOW VERSION Please do nothing" + '\x1b[0m')
    for ip in list_of_data:

        Devices['ip'] = (ip)
        # Devices['password'] = getpass.getpass()
        # Establishing SSH connection
        try:
            ssh_connect = ConnectHandler(**Devices)

            res0 = ssh_connect.send_command('show version')
            print (res0)

            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('func_sh_version.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print(res0)
                sys.stdout = original_stdout  # Reset the standard output to its original value

            print ('\x1b[6;30;42m' + "               DONE               " + '\x1b[0m')
            ssh_connect.disconnect()
        except (AuthenticationException):
            print('\x1b[6;30;41m' + "       Authetication failure: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Authetication failure: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (NetMikoTimeoutException):
            print('\x1b[6;30;41m' + "       Time out from device: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Time out from device: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (EOFError):
            print('\x1b[6;30;41m' + "       End of File reached: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("End of File reached: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (SSHException):
            print('\x1b[6;30;41m' + "       Not able to SSH: Try with Telnet:  " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Not able to SSH: Try with Telnet:  " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except Exception as unknown_error:
            print('\x1b[6;30;41m' + "       other: " + unknown_error + '\x1b[0m')
            continue
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("other: " + unknown_error)
                sys.stdout = original_stdout  # Reset the standard output to its original value


def func_sh_int_cdp_lldp_mactable():

    print ('\x1b[1;31;47m' + "START Script SHOW VERSION Please do nothing" + '\x1b[0m')
    for ip in list_of_data:
        Devices['ip'] = (ip)
        # Devices['password'] = getpass.getpass()
        # Establishing SSH connection
        try:
            ssh_connect = ConnectHandler(**Devices)

            res01 = ssh_connect.send_command('show version')
            print (res01)
            res02 = ssh_connect.send_command('show cdp neig detail')
            print (res02)
            res03 = ssh_connect.send_command('show lldp neig detail')
            print (res03)
            res04 = ssh_connect.send_command('show mac add')
            print (res04)

            print ('\x1b[6;30;42m' + "               DONE               " + '\x1b[0m')

            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('func_sh_int_cdp_lldp_mactable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print(res01, res02, res03, res04)
                sys.stdout = original_stdout  # Reset the standard output to its original value

            ssh_connect.disconnect()
        except (AuthenticationException):
            print('\x1b[6;30;41m' + "       Authetication failure: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Authetication failure: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (NetMikoTimeoutException):
            print('\x1b[6;30;41m' + "       Time out from device: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Time out from device: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (EOFError):
            print('\x1b[6;30;41m' + "       End of File reached: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("End of File reached: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (SSHException):
            print('\x1b[6;30;41m' + "       Not able to SSH: Try with Telnet:  " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Not able to SSH: Try with Telnet:  " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except Exception as unknown_error:
            print('\x1b[6;30;41m' + "       other: " + unknown_error + '\x1b[0m')
            continue
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("other: " + unknown_error)
                sys.stdout = original_stdout  # Reset the standard output to its original value


def func_sh_inventory():
    print ('\x1b[1;31;47m' + "START Script SHOW INVENTORY Please do nothing" + '\x1b[0m')
    for ip in list_of_data:
        Devices['ip'] = (ip)
        # Devices['password'] = getpass.getpass()
        # Establishing SSH connection
        try:
            ssh_connect = ConnectHandler(**Devices)

            res01 = ssh_connect.send_command('show inventory')
            #print (res01)
            res02 = ssh_connect.send_command('show run | inc hostname')
            print (res02)
            print (res01)
            # res03 = ssh_connect.send_command('show lldp neig detail')
            # print (res03)
            # res04 = ssh_connect.send_command('show mac add')
            # print (res04)
            print ('\x1b[6;30;42m' + "               DONE               " + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('func_sh_inventory.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print (res02)
                print (res01)
                # print(res01, res02, res03, res04)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            ssh_connect.disconnect()
        except (AuthenticationException):
            print('\x1b[6;30;41m' + "       Authetication failure: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Authetication failure: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (NetMikoTimeoutException):
            print('\x1b[6;30;41m' + "       Time out from device: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Time out from device: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (EOFError):
            print('\x1b[6;30;41m' + "       End of File reached: " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("End of File reached: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (SSHException):
            print('\x1b[6;30;41m' + "       Not able to SSH: Try with Telnet:  " + ip + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Not able to SSH: Try with Telnet:  " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except Exception as unknown_error:
            print('\x1b[6;30;41m' + "       other: " + unknown_error + '\x1b[0m')
            continue
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("other: " + unknown_error)
                sys.stdout = original_stdout  # Reset the standard output to its original value

# Menu to select Options and Stuff


def func_select_stuff():

    print ("\n\n W T F \n\n press 1 for show int status\n\n press 2 for show version\n\n press 3 for LLDP CDP ARP\n\n press 4 for sh inventory\n\n press 5 for ping test\n\n press q for Quit\n\n ")

    selection = input("Please Select:\n\n")
    if selection == '1':
        print ("\n\nshow int status\n\n")
        func_mklist()
        func_sh_int_status()
        func_select_stuff()
    elif selection == '2':
        print ("\n\nshow version\n\n")
        func_mklist()
        func_sh_version()
        func_select_stuff()
    elif selection == '3':
        print ("\n\nLLDP CDP ARP\n\n")
        func_mklist()
        func_sh_int_cdp_lldp_mactable()
        func_select_stuff()
    elif selection == '4':
        print ("\n\nshow inventory\n\n")
        func_mklist()
        func_sh_inventory()
        func_select_stuff()
    elif selection == '5':
        print ("\n\nping\n\n")
        func_mklist()
        func_ping()
        func_select_stuff()
    elif selection == 'q':
        print ("\n\nBy by digga\n\n")
        quit()
    else:
        print ("\n\n Unknown Option Selected!\n\n")


# Start the basic Functions
func_os_check()
func_userdata()
func_select_stuff()
