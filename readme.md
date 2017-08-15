[![Build Status](https://travis-ci.org/vietdien2005/fullstack-jenkins.svg?branch=master)](https://travis-ci.org/vietdien2005/fullstack-jenkins)

![Demo Image](http://image-store.slidesharecdn.com/da8e74c0-98cd-408d-a3cc-783e45d3ca9f-original.png)

# Fullstack Jenkins

Simple Docker Jenkins Image for PHP 7.0, NodeJS projects & testing with Selenium Python

## Running

Command:

	docker-composer up -d

And go to http://localhost:8080 and login with: 

- Username: fullstack_jenkins
- Password: fullstack_jenkins
	
## Theme Jenkins 

- From [jenkins-material-theme](https://github.com/afonsof/jenkins-material-theme)

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
- phantomjs (PhantomJS)

## Included NodeJS tools

- yarn
- mocha
- gulp
- webpack
- jscs
- standard
- webpack-dev-server

## Plugins Jenkins

- pipeline-stage-tags-metadata
- structs
- handlebars
- junit
- resource-disposer
- pam-auth
- durable-task
- windows-slaves
- antisamy-markup-formatter
- github-branch-source
- pipeline-model-extensions
- javadoc
- maven-plugin
- mapdb-api
- branch-api
- pipeline-milestone-step
- external-monitor-job
- workflow-aggregator
- analysis-core
- matrix-project
- workflow-cps
- workflow-job
- docker-commons
- slack
- build-timeout
- script-security
- mercurial
- ant
- publish-over-ssh
- pipeline-github-lib
- momentjs
- workflow-api
- plain-credentials
- token-macro
- workflow-support
- bitbucket
- github-api
- credentials-binding
- workflow-durable-task-step
- ldap
- workflow-basic-steps
- ws-cleanup
- jquery-detached
- github
- pipeline-input-step
- ace-editor
- pipeline-rest-api
- git-client
- git
- pipeline-build-step
- ssh
- matrix-auth
- scm-api
- bouncycastle-api
- git-server
- gradle
- workflow-scm-step
- simple-theme-plugin
- credentials
- pipeline-stage-view
- workflow-multibranch
- workflow-step-api
- jsch
- timestamper
- display-url-api
- docker-workflow
- ssh-credentials
- ssh-slaves
- mailer
- icon-shim
- pipeline-graph-analysis
- thinBackup
- email-ext
- pipeline-model-declarative-agent
- pipeline-model-definition
- cloudbees-folder
- jackson2-api
- seleniumhq
- pipeline-model-api
- authentication-tokens
- workflow-cps-global-lib
- pipeline-stage-step
- run-condition
- conditional-buildstep
- docker-build-publish
- embeddable-build-status
- gitlab-plugin
- jobConfigHistory
- monitoring
- rebuild
- role-strategy
- saferestart

## Support
### Get the list of plugins from an existing server:

	JENKINS_HOST=username:password@host.com:port
	curl -sSL "http://$JENKINS_HOST/pluginManager/api/xml?depth=1&xpath=/*/*/shortName|/*/*/version&wrapper=plugins" | perl -pe 's/.*?<shortName>([\w-]+).*?<version>([^<]+)()(<\/\w+>)+/\1 \2\n/g'|sed 's/ /:/'
