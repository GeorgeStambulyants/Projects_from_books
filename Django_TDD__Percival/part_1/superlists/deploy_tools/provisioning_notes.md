Provisioning a new site
=======================

## Required packeges

    * nginx
    * Python 3.7
    * virtualenv + pip
    * Git

eg, on Ubuntu:

    sudo apt install nginx git python3.7 python3.7-venv python3-venv

## Nginx Virtual Host config

    * see gunicorn-systemd.template.service
    * replace SITENAME with, e.g, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
        ├── database
        ├── source
        ├── static
        └── virtualenv
