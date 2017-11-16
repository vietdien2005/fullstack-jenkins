#!/bin/bash

set -e

CMD=(
	'python --version'
	'pip --version'
	'pip show selenium'
	'pip show virtualenv'
	'pip show nose'
)

for i in "${CMD[@]}"
do
	echo $i
	eval 'docker exec -it fullstackjenkins_jenkins_1' $i 
	echo '======================================================'
done