#!/usr/bin/env bash
# A script to upgrade pip and npm packages used in the the django-blog project.

REQFILE="requirements.txt"
JSDIR="blog/static/js"

# Upgrade pip packages.
pip install --upgrade -r $REQFILE
pip freeze > $REQFILE

# Upgrade npm packages.
cd $JSDIR
npm update
