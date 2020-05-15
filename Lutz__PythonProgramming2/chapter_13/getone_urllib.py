import os
import getpass
from urllib.request import urlopen


filename = ''  # put filename here
password = getpass.getpass('Pswd?')

remoteaddr = ''  # put address here
print(f'Downloading {remoteaddr}')

remotefile = urlopen(remoteaddr)
localfile = open(filename, 'wb')
localfile = write(remotefile.read())
localfile.close()
remotefile.close()
