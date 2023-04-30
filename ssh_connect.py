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
from netmiko import NetMikoTimeoutException
#from netmiko import AuthenticationException
from paramiko import SSHException
#from netmiko.ssh_exception import NetMikoTimeoutException
#from netmiko.ssh_exception import AuthenticationException
#from paramiko.ssh_exception import SSHException
from datetime import datetime
from getpass import getpass
import time
import sys
# to enable ANSI Support for Windows 10 in func_ansi
import ctypes
# to check the Operating System in func_os_check
import os
import platform
import ipaddress
import subprocess
# import flask
import os





# create a List with IP Addresses to go to
data = open("data.txt", "r")
list_of_data = []


#list_of_data = data.readlines()


# Prompt user for username and password
# ADM_username = input("Enter your ADM-User: ")
# ADM_passwd = getpass("Enter your password: ")


def get_credentials():
    # Prompt user for username and password
    ADM_username = input("Enter your username: ")
    ADM_passwd = getpass("Enter your password: ")

    # Check if username or password is empty
    if len(ADM_username) == 0 or len(ADM_passwd) == 0:
        print('\x1b[1;31;47m' + "Username or password cannot be empty"  + '\x1b[0m')
        #exit()
        func_os_check()
        func_select_stuff()

    return (ADM_username, ADM_passwd)

# Call the get_credentials() function to prompt the user for credentials
# ADM_username, ADM_passwd = get_credentials()


def get_device_info(list_of_data, ADM_username, ADM_passwd):
    # Define the device information
    # create device template for netmiko to connect
    Devices = {
        'device_type': 'cisco_ios',
        'ip': 'list_of_data',
        'username': ADM_username,
        'password': ADM_passwd,
        'secret': 'password',
        'read_timeout_override': 300,
    }

    return Devices


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
def func_mklist(delete_empty_lines=False):
    print('reading IP Address from File')
    with open('data.txt', 'r') as file:
        for line in file:
            if delete_empty_lines and not line.strip():
                continue  # Skip empty lines if the flag is set
            ip = line.strip()
            list_of_data.append(ip)
    print(f'Read {len(list_of_data)} IP addresses from file.')


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


def print_text_in_square(text):
    width = len(text) + 4  # Add 4 to account for the padding on each side

    print("#" * width)  # Print the top border

    for line in text.split("\n"):
        print("# {0:<{1}} #".format(line, len(line)))  # Print each line with padding

    print("#" * width)  # Print the bottom border


# Ping test - does jetzt 1 Ping not used

def func_ping():
    for ip in list_of_data:
        res01 = subprocess.call(['ping', '-c', '2', ip])
        #print(res)
        print('\x1b[6;30;42m' + "     DONE     " + ip + '\x1b[0m')



def func_sh_int_status():
    
    # Call the get_credentials() function to prompt the user for credentials
    ADM_username, ADM_passwd = get_credentials()
    # Call the get_device_info() function to define the device information
    Devices = get_device_info(list_of_data, ADM_username, ADM_passwd)


    print ('\x1b[1;31;47m' + "START Script SHOW INT STATUS Please do nothing" + '\x1b[0m')
    for ip in list_of_data:
        #
        # Devices['username'] = input("User name ")
        # Devices['password'] = getpass.getpass()
        Devices['ip'] = (ip)
        # Devices['secret'] = input("Enter enable password")
        # Establishing SSH connection

        ssh_connect = ConnectHandler(**Devices)

        # changing to enable mode
        # ssh_connect.enable()

        # for ip in list_of_data:
        res0 = ssh_connect.send_command('show int status | inc cted')
        # print (res0)
        print ('\x1b[6;30;42m' + "     DONE     " + '\x1b[0m')

        original_stdout = sys.stdout  # Save a reference to the original standard output
        with open('func_sh_int_status.txt', 'a+') as f:
            sys.stdout = f  # Change the standard output to the file we created.
            print(res0)
            sys.stdout = original_stdout  # Reset the standard output to its original value

        # ssh_connect.send_command('ip add 10.10.10.1 255.255.255.0')
        # ssh_connect.send_command('end')
        # ssh_connect.send_command('write')
        ssh_connect.disconnect()


def func_sh_version():

    # Call the get_credentials() function to prompt the user for credentials
    ADM_username, ADM_passwd = get_credentials()
    # Call the get_device_info() function to define the device information
    Devices = get_device_info(list_of_data, ADM_username, ADM_passwd)


    print ('\x1b[1;31;47m' + "START Script SHOW VERSION Please do nothing" + '\x1b[0m')
    for ip in list_of_data:

        Devices['ip'] = (ip)
        # Devices['password'] = getpass.getpass()
        # Establishing SSH connection
        ssh_connect = ConnectHandler(**Devices)

        res0 = ssh_connect.send_command('show version')
        # print (res0)

        original_stdout = sys.stdout  # Save a reference to the original standard output
        with open('func_sh_version.txt', 'a+') as f:
            sys.stdout = f  # Change the standard output to the file we created.
            print(res0)
            sys.stdout = original_stdout  # Reset the standard output to its original value

        print ('\x1b[6;30;42m' + "     DONE     " + '\x1b[0m')
        ssh_connect.disconnect()

def func_sh_int_cdp_lldp_mactable():

    # Call the get_credentials() function to prompt the user for credentials
    ADM_username, ADM_passwd = get_credentials()
    # Call the get_device_info() function to define the device information
    Devices = get_device_info(list_of_data, ADM_username, ADM_passwd)


    print ('\x1b[1;31;47m' + "START Script SHOW VERSION Please do nothing" + '\x1b[0m')
    for ip in list_of_data:
        Devices['ip'] = (ip)
        # Devices['password'] = getpass.getpass()
        # Establishing SSH connection
        ssh_connect = ConnectHandler(**Devices)

        res01 = ssh_connect.send_command('show version')
        # print (res01)
        res02 = ssh_connect.send_command('show cdp neig detail')
        # print (res02)
        res03 = ssh_connect.send_command('show lldp neig detail')
        # print (res03)
        res04 = ssh_connect.send_command('show mac add')
        # print (res04)

        print ('\x1b[6;30;42m' + "               DONE               " + '\x1b[0m')

        original_stdout = sys.stdout  # Save a reference to the original standard output
        with open('func_sh_int_cdp_lldp_mactable.txt', 'a+') as f:
            sys.stdout = f  # Change the standard output to the file we created.
            print(res01, res02, res03, res04)
            sys.stdout = original_stdout  # Reset the standard output to its original value

        ssh_connect.disconnect()

def func_techsupport():

    # Call the get_credentials() function to prompt the user for credentials
    ADM_username, ADM_passwd = get_credentials()
    # Call the get_device_info() function to define the device information
    Devices = get_device_info(list_of_data, ADM_username, ADM_passwd)

    print ('\x1b[1;31,47m' + "START Script TechSupport Please do nothing" + '\x1b[0m')
    for ip in list_of_data:
        Devices['ip'] = (ip)
        try:
            ssh_connect = ConnectHandler(**Devices)
            start_time = datetime.now()
            res01 = ssh_connect.send_command("show run | inc hostname")
            # print (res002)
            res02 = ssh_connect.send_command("show tech-support", read_timeout = 360 )

            # print (res01)
            # print (res02)
            # res03 = ssh_connect.send_command('show lldp neig detail')
            # print (res03)
            # res04 = ssh_connect.send_command('show mac add')
            # print (res04)
            end_time = datetime.now()
            print (f"\nExec time: {end_time - start_time}\n") 
            print ('\x1b[6;30;42m' + "               DONE               " + " with " + res01 + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('func_sh_techsupport.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print ('######## Start ' + res01 + ' ########')
                # print (res02)
                # print (res02)
                print ('######## End ' + res01 + ' ########')
                # print(res02, res01, res03, res04)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            ssh_connect.disconnect()
        except (AuthenticationException):
            print("Authetication failure: " + ip)
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Authetication failure: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (NetMikoTimeoutException):
            print("Time out from device: " + ip)
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Time out from device: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (EOFError):
            print("End of File reached: " + ip)
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("End of File reached: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (SSHException):
            print("Not able to SSH: Try with Telnet:  " + ip)
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Not able to SSH: Try with Telnet:  " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except Exception as unknown_error:
            print("other: " + unknown_error)
            continue
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("other: " + unknown_error)
                sys.stdout = original_stdout  # Reset the standard output to its original value
        finally:
                end_time = datetime.now()



def func_sh_inventory():

    # Call the get_credentials() function to prompt the user for credentials
    ADM_username, ADM_passwd = get_credentials()
    # Call the get_device_info() function to define the device information
    Devices = get_device_info(list_of_data, ADM_username, ADM_passwd)


    print ('\x1b[1;31;47m' + "START Script SHOW INVENTORY Please do nothing" + '\x1b[0m')
    for ip in list_of_data:
        Devices['ip'] = (ip)
        # Devices['password'] = getpass.getpass()
        # Establishing SSH connection
        try:
            ssh_connect = ConnectHandler(**Devices)

            res01 = ssh_connect.send_command('show inventory')
            # print (res01)
            res02 = ssh_connect.send_command('show run | inc hostname')
            # print (res02)
            # print (res01)
            # res03 = ssh_connect.send_command('show lldp neig detail')
            # print (res03)
            # res04 = ssh_connect.send_command('show mac add')
            # print (res04)
            print ('\x1b[6;30;42m' + "               DONE               " + '\x1b[0m')
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('func_sh_inventory.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                # print (res02)
                # print (res01)
                # print(res01, res02, res03, res04)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            ssh_connect.disconnect()
        except (AuthenticationException):
            print("Authetication failure: " + ip)
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Authetication failure: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (NetMikoTimeoutException):
            print("Time out from device: " + ip)
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Time out from device: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (EOFError):
            print("End of File reached: " + ip)
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("End of File reached: " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except (SSHException):
            print("Not able to SSH: Try with Telnet:  " + ip)
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("Not able to SSH: Try with Telnet:  " + ip)
                sys.stdout = original_stdout  # Reset the standard output to its original value
            continue
        except Exception as unknown_error:
            print("other: " + unknown_error)
            continue
            original_stdout = sys.stdout  # Save a reference to the original standard output
            with open('unreachable.txt', 'a+') as f:
                sys.stdout = f  # Change the standard output to the file we created.
                print("other: " + unknown_error)
                sys.stdout = original_stdout  # Reset the standard output to its original value


def func_sh_run_http():

    # Call the get_credentials() function to prompt the user for credentials
    ADM_username, ADM_passwd = get_credentials()
    # Call the get_device_info() function to define the device information
    Devices = get_device_info(list_of_data, ADM_username, ADM_passwd)

    print ('\x1b[1;31;47m' + "START Script SHOW INVENTORY Please do nothing" + '\x1b[0m')
    for ip in list_of_data:
         Devices['ip'] = (ip)
            # Devices['password'] = getpass.getpass()
            # Establishing SSH connection
         try:
             ssh_connect = ConnectHandler(**Devices)

             res01 = ssh_connect.send_command('show run | inc ip http server|secure|active')
             # print (res01)
             res02 = ssh_connect.send_command('show run | inc hostname')
             # print (res02)
             # print (res01)
             # res03 = ssh_connect.send_command('show lldp neig detail')
             # print (res03)
             # res04 = ssh_connect.send_command('show mac add')
             # print (res04)
             print ('\x1b[6;30;42m' + "               DONE               " + '\x1b[0m')
             original_stdout = sys.stdout  # Save a reference to the original standard output
             with open('func_sh_run_http.txt', 'a+') as f:
                 sys.stdout = f  # Change the standard output to the file we created.
                 # print (res02)
                 # print (res01)
                 # print(res01, res02, res03, res04)
                 sys.stdout = original_stdout  # Reset the standard output to its original value
             ssh_connect.disconnect()
         except (AuthenticationException):
             print("Authetication failure: " + ip)
             original_stdout = sys.stdout  # Save run |  reference to the original standard output
             with open('unreachable.txt', 'a+') as f:
                 sys.stdout = f  # Change the standard output to the file we created.
                 print("Authetication failure: " + ip)
                 sys.stdout = original_stdout  # Reset the standard output to its original value
             continue
         except (NetMikoTimeoutException):
             print("Time out from device: " + ip)
             original_stdout = sys.stdout  # Save a reference to the original standard output
             with open('unreachable.txt', 'a+') as f:
                 sys.stdout = f  # Change the standard output to the file we created.
                 print("Time out from device: " + ip)
                 sys.stdout = original_stdout  # Reset the standard output to its original value
             continue
         except (EOFError):
             print("End of File reached: " + ip)
             original_stdout = sys.stdout  # Save a reference to the original standard output
             with open('unreachable.txt', 'a+') as f:
                 sys.stdout = f  # Change the standard output to the file we created.
                 print("End of File reached: " + ip)
                 sys.stdout = original_stdout  # Reset the standard output to its original value
             continue
         except (SSHException):
             print("Not able to SSH: Try with Telnet:  " + ip)
             original_stdout = sys.stdout  # Save a reference to the original standard output
             with open('unreachable.txt', 'a+') as f:
                 sys.stdout = f  # Change the standard output to the file we created.
                 print("Not able to SSH: Try with Telnet:  " + ip)
                 sys.stdout = original_stdout  # Reset the standard output to its original value
             continue
         except Exception as unknown_error:
             print("other: " + unknown_error)
             continue
             original_stdout = sys.stdout  # Save a reference to the original standard output
             with open('unreachable.txt', 'a+') as f:
                 sys.stdout = f  # Change the standard output to the file we created.
                 print("other: " + unknown_error)
                 sys.stdout = original_stdout  # Reset the standard output to its original value




# Menu to select Options and Stuff


def func_select_stuff():
    print_text_in_square(" Cisco SSH Connect Script ")
    print ("\n\n press 1 for show int status\n\n press 2 for show version\n\n press 3 for LLDP CDP ARP\n\n press 4 for sh run http\n\n press 5 for show inventory\n\n press 6 for TechSupport \n\n press 7 to Ping Devices \n\n press q for Quit\n\n ")

    selection = input("Please Select:\n\n")
    if selection == '1':
        print ("\n\nshow int status\n\n")
        func_mklist(delete_empty_lines=True)
        func_sh_int_status()
        func_select_stuff()
    elif selection == '2':
        print ("\n\nshow version\n\n")
        func_mklist(delete_empty_lines=True)
        func_sh_version()
        func_select_stuff()
    elif selection == '3':
        print ("\n\nLLDP CDP ARP\n\n")
        func_mklist(delete_empty_lines=True)
        func_sh_int_cdp_lldp_mactable()
        func_select_stuff()
    elif selection == '4':
        print ("\n\nshow run http\n\n")
        func_mklist(delete_empty_lines=True)
        func_sh_run_http()
        func_select_stuff()
    elif selection == '5':
        print ("\n\nshow inv\n\n")
        func_mklist(delete_empty_lines=True)
        func_sh_inventory()
        func_select_stuff()
    elif selection == '6':
        print ("\n\nshow TechSupport\n\n")
        func_mklist(delete_empty_lines=True)
        func_techsupport()
        func_select_stuff()
    elif selection == '7':
        print ("\n\nPing Devices in List\n\n")
        func_mklist(delete_empty_lines=True)
        func_ping()
        func_select_stuff()
    elif selection == 'q':
        print ("\n\nBy by digga\n\n")
        quit()
    else:
        print ('\033[5m\033[1m\033[94m' + "\n\n Unknown Option Selected! Please type a Number from 1 to 7 !!!\n\n" + '\033[0m')
        time.sleep(3)
        func_select_stuff()


# Start the basic Functions
func_os_check()
func_select_stuff()
