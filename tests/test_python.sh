#!/bin/bash

CMD=(
	'python --version'
	'pip --version'
	'pip show selenium'
	'pip show virtualenv'
	'pip show nose'
	'geckodriver --version'
	'chromedriver --version'
)

for i in "${CMD[@]}"
do
	eval 'docker exec -it fullstackjenkins_jenkins_1' $i 
	echo ''
	echo '======================================================'
done