# Fullstack Jenkins

Simple Docker Jenkins Image for PHP 7.0, NodeJS projects & testing with Selenium Python

## Included PHP tools

- phpunit from <https://phar.phpunit.de/phpunit.phar>
- composer from <https://getcomposer.org/composer.phar>
- phpmd from <http://static.phpmd.org/php/latest/phpmd.phar>
- sami from <http://get.sensiolabs.org/sami.phar>
- phpcov from <https://phar.phpunit.de/phpcov.phar>
- phpcpd from <https://phar.phpunit.de/phpcpd.phar>
- phploc from <https://phar.phpunit.de/phploc.phar>
- phptok from <https://phar.phpunit.de/phptok.phar>
- box from <https://github.com/box-project/box2/releases/download/2.5.2/box-2.5.2.phar>
- phpbrew from <https://github.com/phpbrew/phpbrew/raw/master/phpbrew>

## Included Python tools

- selenium
- nose
- virtualenv

## Web Drivers

- chromedriver (Google Chrome)
- geckodriver (Mozilla Firefox)

## Included NodeJS tools

- yarn
- mocha
- bower
- gulp
- webpack
- jscs
- standard
- webpack-dev-server

## Support
### Get the list of plugins from an existing server:

	JENKINS_HOST=username:password@host.com:port
	curl -sSL "http://$JENKINS_HOST/pluginManager/api/xml?depth=1&xpath=/*/*/shortName|/*/*/version&wrapper=plugins" | perl -pe 's/.*?<shortName>([\w-]+).*?<version>([^<]+)()(<\/\w+>)+/\1 \2\n/g'|sed 's/ /:/'
