FROM jenkins/jenkins:lts-alpine

MAINTAINER Dam Viet "vietdien2005@gmail.com"

USER root

# Add Repos
ADD https://php.codecasts.rocks/php-alpine.rsa.pub /etc/apk/keys/php-alpine.rsa.pub
RUN echo "@php http://php.codecasts.rocks/v3.5/php-7.0" >> /etc/apk/repositories

# Basic tools
RUN apk update --no-cache && apk upgrade

RUN apk add --update --no-cache sudo git doxygen vim python python-dev ca-certificates dialog gcc musl-dev libffi-dev \
	zip unzip curl autoconf automake re2c tzdata libxml2 libxml2-dev bison openssl gettext libmcrypt-dev xvfb python \
	python-dev py-pip build-base

# Install Php 7.0
RUN apk add --update --no-cache \
    php7@php \
    php7-apcu@php	\
    php7-bcmath@php \
    php7-bz2@php \
    php7-calendar@php \
    php7-common@php \
    php7-ctype@php \
    php7-curl@php \
    php7-dba@php \
    php7-dev@php \
    php7-dom@php \
    php7-embed@php \
    php7-enchant@php \
    php7-exif@php \
    php7-ftp@php \
    php7-gd@php \
    php7-gettext@php \
    php7-gmp@php \
    php7-iconv@php \
    php7-imagick@php \
    php7-imap@php \
    php7-intl@php \
    php7-json@php \
    php7-ldap@php \
    php7-libsodium@php \
    php7-litespeed@php \
    php7-mbstring@php \
    php7-mcrypt@php \
    php7-memcached@php \
    php7-mongodb@php \
    php7-mysqli@php \
    php7-mysqlnd@php \
    php7-odbc@php \
    php7-opcache@php \
    php7-openssl@php \
    php7-pcntl@php \
    php7-pdo@php \
    php7-pdo_dblib@php \
    php7-pdo_mysql@php \
    php7-pdo_pgsql@php \
    php7-pdo_sqlite@php \
    php7-pear@php \
    php7-pgsql@php \
    php7-phar@php \
    php7-phpdbg@php \
    php7-posix@php \
    php7-pspell@php \
    php7-redis@php \
    php7-session@php \
    php7-shmop@php \
    php7-soap@php \
    php7-sockets@php \
    php7-sqlite3@php \
    php7-sysvmsg@php \
    php7-sysvsem@php \
    php7-sysvshm@php \
    php7-tidy@php \
    php7-wddx@php \
    php7-xdebug@php \
    php7-xml@php \
    php7-xmlrpc@php \
    php7-xsl@php \
    php7-zip@php \
    php7-zlib@php

RUN ln -s /usr/bin/php7 /usr/bin/php

# Install php tools
RUN mkdir -p /usr/local/bin \
	&& wget -q -O /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar && chmod +x /usr/local/bin/phpunit \
	&& wget -q -O /usr/local/bin/composer https://getcomposer.org/composer.phar && chmod +x /usr/local/bin/composer \
	&& wget -q -O /usr/local/bin/phpmd http://static.phpmd.org/php/latest/phpmd.phar && chmod +x /usr/local/bin/phpmd \
	&& wget -q -O /usr/local/bin/sami http://get.sensiolabs.org/sami.phar && chmod +x /usr/local/bin/sami \
	&& wget -q -O /usr/local/bin/phpcov https://phar.phpunit.de/phpcov.phar && chmod +x /usr/local/bin/phpcov \
	&& wget -q -O /usr/local/bin/phpcpd https://phar.phpunit.de/phpcpd.phar && chmod +x /usr/local/bin/phpcpd \
	&& wget -q -O /usr/local/bin/phploc https://phar.phpunit.de/phploc.phar && chmod +x /usr/local/bin/phploc \
	&& wget -q -O /usr/local/bin/phptok https://phar.phpunit.de/phptok.phar && chmod +x /usr/local/bin/phptok \
	&& wget -q -O /usr/local/bin/phpdox https://github.com/theseer/phpdox/releases/download/0.10.1/phpdox-0.10.1.phar && chmod +x /usr/local/bin/phpdox \
	&& wget -q -O /usr/local/bin/box https://github.com/box-project/box2/releases/download/2.7.5/box-2.7.5.phar && chmod +x /usr/local/bin/box \
	&& wget -q -O /usr/local/bin/phpbrew https://github.com/phpbrew/phpbrew/raw/master/phpbrew && chmod +x /usr/local/bin/phpbrew

# Update Timezone. Hello, I'm from Ho Chi Minh, Vietnam
RUN cp /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime \
	&& echo "Asia/Ho_Chi_Minh" > /etc/timezone \
	&& apk del tzdata

# Install environment testing with selenium
RUN pip install --upgrade pip \
	&& pip install selenium==3.3.1 virtualenv nose

# Install NodeJS & Packages Global
RUN apk add --update --no-cache nodejs \
	&& npm install --global yarn \
	&& yarn global add n mocha gulp webpack jscs standard webpack-dev-server

# Setup Config Jenkins
COPY ./config/config.xml /usr/share/jenkins/ref/config.xml
COPY ./config/jenkins.model.JenkinsLocationConfiguration.xml /usr/share/jenkins/ref/jenkins.model.JenkinsLocationConfiguration.xml
COPY ./config/nodeMonitors.xml /usr/share/jenkins/ref/nodeMonitors.xml
COPY ./config/org.codefirst.SimpleThemeDecorator.xml /usr/share/jenkins/ref/org.codefirst.SimpleThemeDecorator.xml
COPY ./config/thinBackup.xml /usr/share/jenkins/ref/thinBackup.xml
COPY ./config/users /usr/share/jenkins/ref/users

# Clean packages 
RUN rm -rf /var/cache/apk/*

# Install plugin Jenkins
USER jenkins
COPY ./config/plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/plugins.txt | tr '\n' ' ')

# Upgrade Jenkins latest
RUN wget -q http://updates.jenkins-ci.org/latest/jenkins.war -O /usr/share/jenkins/jenkins.war

# Setup version Jenkins
RUN echo $(java -jar /usr/share/jenkins/jenkins.war --version) > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state
