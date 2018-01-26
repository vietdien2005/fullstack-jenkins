#!/bin/bash

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
	'phpbrew --version'
	'pdepend --version'
	'phpcbf --version'
	'phpcs --version'
)

for i in "${CMD[@]}"
do
	echo $i
	eval 'docker exec -it fullstack_jenkins' $i
	echo '======================================================'
done