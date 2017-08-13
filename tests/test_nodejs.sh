#!/bin/bash

CMD=(
	'node -v'
	'npm -v'
	'yarn -v'
	'mocha -v'
	'bower -v'
	'gulp -v'
	'webpack -v'
	'jscs -v'
	'standard -v'
	'webpack-dev-server -v'
)

for i in "${CMD[@]}"
do
	eval 'docker exec -it fullstackjenkins_jenkins_1' $i 
	echo ''
	echo '======================================================'
done