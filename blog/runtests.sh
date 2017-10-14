#!/usr/bin/env bash

cd ../
./upgrade.sh
cd blog
./manage.py test && ./pylint.sh
