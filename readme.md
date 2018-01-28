[![Build Status](https://travis-ci.org/vietdien2005/fullstack-jenkins.svg?branch=master)](https://travis-ci.org/vietdien2005/fullstack-jenkins) [![](https://images.microbadger.com/badges/image/vietdien2005/fullstack_jenkins_alpine.svg)](https://microbadger.com/images/vietdien2005/fullstack_jenkins_alpine "Get your own image badge on microbadger.com") [![](https://images.microbadger.com/badges/version/vietdien2005/fullstack_jenkins_alpine.svg)](https://microbadger.com/images/vietdien2005/fullstack_jenkins_alpine "Get your own version badge on microbadger.com")

![Demo Image](http://image-store.slidesharecdn.com/da8e74c0-98cd-408d-a3cc-783e45d3ca9f-original.png)

# Fullstack Jenkins

Simple Docker Jenkins Image for PHP 7.0

## Running

Command:

	docker-composer up -d

And go to http://localhost:8888 and login with:

- Username: fullstack_jenkins
- Password: fullstack_jenkins

## Template Jobs

- Template PHP Code Coverage from <http://jenkins-php.org/index.html>

## Theme Jenkins 

- From [jenkins-material-theme](https://github.com/afonsof/jenkins-material-theme)

## Included PHP tools

- phpunit from <https://phar.phpunit.de>
- phpcov from <https://phar.phpunit.de>
- phpcpd from <https://phar.phpunit.de>
- phploc from <https://phar.phpunit.de>
- phptok from <https://phar.phpunit.de>
- composer from <https://getcomposer.org>
- phpmd from <https://phpmd.org>
- sami from <https://sensiolabs.com>
- phpcbf from <https://squizlabs.github.io/PHP_CodeSniffer/analysis>
- phpcs from <https://squizlabs.github.io/PHP_CodeSniffer/analysis>
- phpdox from <http://phpdox.de>
- pdepend from <https://pdepend.org>
- phpbrew from <https://phpbrew.github.io/phpbrew>

## Included Python tools

- selenium
- nose
- virtualenv

## Plugins Jenkins

- blueocean-display-url
- ldap
- pipeline-stage-tags-metadata
- apache-httpcomponents-client-4-api
- blueocean
- notification
- sse-gateway
- workflow-aggregator
- warnings
- dry
- jdepend
- structs
- ace-editor
- jackson2-api
- jquery-detached
- git-server
- ant
- role-strategy
- pipeline-model-declarative-agent
- resource-disposer
- matrix-project
- conditional-buildstep
- momentjs
- credentials-binding
- ssh-credentials
- pipeline-model-api
- ssh
- pipeline-model-extensions
- publish-over-ssh
- gradle
- command-launcher
- bitbucket
- run-condition
- jsch
- build-timeout
- workflow-step-api
- docker-commons
- cloverphp
- blueocean-core-js
- timestamper
- pipeline-github-lib
- ws-cleanup
- antisamy-markup-formatter
- gitlab-plugin
- branch-api
- variant
- email-ext
- blueocean-bitbucket-pipeline
- durable-task
- mapdb-api
- testingbot
- git-client
- saferestart
- blueocean-autofavorite
- pipeline-model-definition
- junit
- display-url-api
- git
- pipeline-milestone-step
- analysis-core
- handlebars
- blueocean-rest-impl
- blueocean-dashboard
- cloudbees-folder
- github-api
- workflow-support
- external-monitor-job
- blueocean-config
- workflow-durable-task-step
- maven-plugin
- cloudbees-bitbucket-branch-source
- blueocean-commons
- workflow-scm-step
- config-file-provider
- publish-over
- mailer
- pipeline-input-step
- xunit
- pipeline-stage-view
- favorite
- matrix-auth
- blueocean-jwt
- simple-theme-plugin
- pipeline-build-step
- workflow-multibranch
- credentials
- script-security
- plot
- pipeline-rest-api
- nodejs
- workflow-basic-steps
- checkstyle
- crap4j
- embeddable-build-status
- workflow-cps
- jira
- violations
- workflow-cps-global-lib
- blueocean-rest
- plain-credentials
- workflow-job
- blueocean-github-pipeline
- discard-old-build
- authentication-tokens
- git-changelog
- blueocean-jira
- github-branch-source
- mercurial
- blueocean-git-pipeline
- docker-workflow
- blueocean-personalization
- thinBackup
- gravatar
- javadoc
- internetmeme
- scm-api
- blueocean-web
- pipeline-graph-analysis
- jenkins-design-language
- jobConfigHistory
- pmd
- token-macro
- workflow-api
- blueocean-i18n
- blueocean-pipeline-api-impl
- docker-build-publish
- icon-shim
- rebuild
- blueocean-events
- github
- htmlpublisher
- show-build-parameters
- pipeline-stage-step
- pubsub-light
- blueocean-pipeline-scm-api
- blueocean-pipeline-editor
- handy-uri-templates-2-api
- ssh-slaves

## Support
### Get the list of plugins from an existing server:

	JENKINS_HOST=username:password@host.com:port
	curl -sSL "http://$JENKINS_HOST/pluginManager/api/xml?depth=1&xpath=/*/*/shortName|/*/*/version&wrapper=plugins" | perl -pe 's/.*?<shortName>([\w-]+).*?<version>([^<]+)()(<\/\w+>)+/\1 \2\n/g'|sed 's/ /:/'

## Donate

[![Donate with Bitcoin](https://en.cryptobadges.io/badge/big/1Cvk2WP8rfhhcKLBgxxK1e6bo5ffRYhQm1)](https://en.cryptobadges.io/donate/1Cvk2WP8rfhhcKLBgxxK1e6bo5ffRYhQm1)

[![Donate with Ethereum](https://en.cryptobadges.io/badge/big/0x0D0A378451a1D32082d08981d9DD9d8cD1773539)](https://en.cryptobadges.io/donate/0x0D0A378451a1D32082d08981d9DD9d8cD1773539)
