#!/usr/bin/env bash

pylint 	--rcfile=pylintrc \
		--ignore-patterns=migrations \
		--load-plugins pylint_django \
		analytics blog common messaging posts scripts \
	   
