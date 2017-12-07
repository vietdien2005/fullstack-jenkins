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
	eval 'docker exec -it fullstack_jenkins' $i 
	echo '======================================================'
done