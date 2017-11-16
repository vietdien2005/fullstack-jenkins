#!/bin/bash

set -e

CMD=(
	'php -v',
	'composer --version'
	'phpunit --version'
	'phpmd --version'
	'sami --version'
	'phpcov --version'
	'phpcpd --version'
	'phploc --version'
	'phptok --version'
	'phpdox -v'
	'box --version'
	'phpbrew --version'
)

for i in "${CMD[@]}"
do
	echo $i
	eval 'docker exec -it fullstackjenkins_jenkins_1' $i
	echo '======================================================'
done