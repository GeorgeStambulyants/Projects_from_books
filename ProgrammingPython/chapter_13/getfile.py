from ftplib import FTP
from os.path import exists


def getfile(file, site, dir, user=(), *, verbose=True, refetch=False):
    if exists(file) and not refetch:
        if verbose:
            print(f'{file} is already fetched')
    else:
        if verbose:
            print(f'Downloading {file}')
            local = open(file, 'wb')
            try:
                remote = FTP(site)
                remote.login(*user)
                remote.cwd(dir)
                remote.retrbinary('RETR' + file, local.write, 1024)
                remote.quit()
            finally:
                local.close()
            if verbose:
                print('Downloading done')


if __name__ == '__main__':
    from getpass import getpass
    file = ''  # put filename here
    dir = ''  # dir here
    site = ''  # site here
    user = ('', getpass('Pswd'))  # user info here
    getfile(file, site, dir, user)
