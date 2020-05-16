# Uploads file to the server
#
import ftplib


def pufile(file, site, dir, user=(), *, verbose=True):
    if verbose:
        print(f'Uploading {file}')
    local = open(file, 'rb')
    remote = ftplib.FTP(site)
    remote.login(*user)
    remote.cwd(dir)
    remote.storbinary('STOR ' + file)
    remote.quit()
    local.close()
    if verbose:
        print('Upload done')


if __name__ == '__main__':
    site = ''  # put site here
    dir = ''  # dir here
    import sys, getpass
    pswd = getpass.getpass(site + ' pswd?')
    putfile(sys.argv[1], site, dir, user=('', pswd))
