# A script to download a file from ftp server
#
import os
import sys
from ftplib import FTP
from getpass import getpass


nonpassive = False
filename = ''  # put filename here
dirname = ''  # put dirname here
sitename = ''  # and sitename here
userinfo = ('', getpass('Pswd?'))  # put userinfo

if len(sys.argv) > 1:
    filename = sys.argv[1]

print('Connecting...')
connection = FTP(sitename)
connection.login(*userinfo)
connection.cwd(dirname)
if nonpassive:
    connection.set_pasv(False)

print('Downloading')
localfile = open(filename, 'wb')
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
connection.quit()
localfile.close()
