#!/bin/bash

set -ev

CMD=(
	'node -v'
	'npm -v'
	'yarn --version'
	'mocha --version'
	'gulp --version'
	'webpack --version'
	'jscs --version'
	'standard --version'
	'webpack-dev-server --version'
)

for i in "${CMD[@]}"
do
	echo $i
	eval 'docker exec -it fullstackjenkins_jenkins_1' $i 
	echo '======================================================'
done