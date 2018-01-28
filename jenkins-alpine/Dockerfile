FROM jenkins/jenkins:lts-alpine

MAINTAINER Dam Viet "vietdien2005@gmail.com"

ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
    org.label-schema.name="Fullstack Jenkins" \
    org.label-schema.description="Simple Docker Jenkins Image for PHP 7.0" \
    org.label-schema.url="https://github.com/vietdien2005/fullstack-jenkins" \
    org.label-schema.vcs-ref=$VCS_REF \
    org.label-schema.vcs-url="https://github.com/vietdien2005/fullstack-jenkins" \
    org.label-schema.version=$VERSION \
    org.label-schema.schema-version="1.0"

USER root

# Basic tools
RUN apk update --no-cache && apk upgrade

RUN apk add --update --no-cache sudo git doxygen vim python python-dev ca-certificates dialog gcc musl-dev libffi-dev \
	zip unzip curl autoconf automake re2c tzdata libxml2 libxml2-dev bison openssl gettext libmcrypt-dev xvfb python \
	python-dev py-pip build-base

RUN apk --no-cache add --virtual build-deps

# Install Php 7.0
RUN apk add --update --no-cache \
        php7 \
        php7-memcached \
        php7-common \
        php7-sysvsem \
        php7-sysvshm \
        php7-tidy \
        php7-tokenizer \
        php7-wddx \
        php7-xml \
        php7-xmlreader \
        php7-xmlrpc \
        php7-xmlwriter \
        php7-xsl \
        php7-zip \
        php7-zlib \
        php7-phar \
        php7-posix \
        php7-pspell \
        php7-recode \
        php7-session \
        php7-shmop \
        php7-simplexml \
        php7-soap \
        php7-sockets \
        php7-sqlite3 \
        php7-sysvmsg \
        php7-mysqlnd \
        php7-odbc \
        php7-opcache \
        php7-openssl \
        php7-pcntl \
        php7-pdo \
        php7-pdo_dblib \
        php7-pdo_mysql \
        php7-pdo_odbc \
        php7-pdo_pgsql \
        php7-pdo_sqlite \
        php7-pgsql \
        php7-ftp \
        php7-gd \
        php7-gettext \
        php7-gmp \
        php7-iconv \
        php7-imap \
        php7-intl \
        php7-json \
        php7-ldap \
        php7-mbstring \
        php7-mcrypt \
        php7-mysqli \
        php7-bcmath \
        php7-bz2 \
        php7-calendar \
        php7-ctype \
        php7-curl \
        php7-dba \
        php7-dom \
        php7-enchant \
        php7-exif \
        php7-fileinfo \
        php7-pear \
        php7-apache2 \
        php7-cgi \
        php7-dev \
        php7-doc \
        php7-embed \
        php7-fpm \
        php7-litespeed \
        php7-phpdbg \
        php7-imagick \
        php7-imagick-dev \
        php7-ssh2 \
        php7-xdebug \
        php7-amqp \
        php7-mailparse \
        php7-oauth \
        php7-pear-mail_mime \
        php7-pear-mdb2_driver_pgsql \
        php7-pear-net_idna2 \
        php7-zmq \
        php7-pear-auth_sasl \
        php7-pear-mdb2_driver_mysql \
        php7-apcu \
        php7-pear-auth_sasl2 \
        php7-redis \
        php7-pear-net_smtp \
        php7-pear-net_smtp-doc \
        php7-pear-net_socket

# Install php tools
RUN mkdir -p /usr/local/bin
RUN wget -q -O /usr/local/bin/phpunit https://phar.phpunit.de/phpunit.phar && chmod +x /usr/local/bin/phpunit
RUN wget -q -O /usr/local/bin/phpcov https://phar.phpunit.de/phpcov.phar && chmod +x /usr/local/bin/phpcov
RUN wget -q -O /usr/local/bin/phpcpd https://phar.phpunit.de/phpcpd.phar && chmod +x /usr/local/bin/phpcpd
RUN wget -q -O /usr/local/bin/phploc https://phar.phpunit.de/phploc.phar && chmod +x /usr/local/bin/phploc
RUN wget -q -O /usr/local/bin/phptok https://phar.phpunit.de/phptok.phar && chmod +x /usr/local/bin/phptok
RUN wget -q -O /usr/local/bin/composer https://getcomposer.org/composer.phar && chmod +x /usr/local/bin/composer
RUN wget -q -O /usr/local/bin/phpmd http://static.phpmd.org/php/latest/phpmd.phar && chmod +x /usr/local/bin/phpmd
RUN wget -q -O /usr/local/bin/sami http://get.sensiolabs.org/sami.phar && chmod +x /usr/local/bin/sami
RUN wget -q -O /usr/local/bin/phpcbf https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar && chmod +x /usr/local/bin/phpcbf
RUN wget -q -O /usr/local/bin/phpcs https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar && chmod +x /usr/local/bin/phpcs
RUN wget -q -O /usr/local/bin/phpdox http://phpdox.de/releases/phpdox.phar && chmod +x /usr/local/bin/phpdox
RUN wget -q -O /usr/local/bin/pdepend http://static.pdepend.org/php/latest/pdepend.phar && chmod +x /usr/local/bin/pdepend
RUN wget -q -O /usr/local/bin/phpbrew https://github.com/phpbrew/phpbrew/raw/master/phpbrew && chmod +x /usr/local/bin/phpbrew

# Update Timezone. Hello, I'm from Ho Chi Minh, Vietnam
RUN cp /usr/share/zoneinfo/Asia/Ho_Chi_Minh /etc/localtime \
	&& echo "Asia/Ho_Chi_Minh" > /etc/timezone \
	&& apk del tzdata

# Install environment testing with selenium
RUN pip install --upgrade pip \
	&& pip install selenium==3.3.1 virtualenv nose

# Upgrade Jenkins latest
RUN wget -q http://mirrors.jenkins.io/war-stable/latest/jenkins.war -O /usr/share/jenkins/jenkins.war

# Setup Config Jenkins
COPY ./config/config.xml /usr/share/jenkins/ref/config.xml
COPY ./config/jenkins.model.JenkinsLocationConfiguration.xml /usr/share/jenkins/ref/jenkins.model.JenkinsLocationConfiguration.xml
COPY ./config/nodeMonitors.xml /usr/share/jenkins/ref/nodeMonitors.xml
COPY ./config/org.codefirst.SimpleThemeDecorator.xml /usr/share/jenkins/ref/org.codefirst.SimpleThemeDecorator.xml
COPY ./config/thinBackup.xml /usr/share/jenkins/ref/thinBackup.xml
COPY ./config/users /usr/share/jenkins/ref/users
COPY ./config/jobs /usr/share/jenkins/ref/jobs

# Clean packages 
RUN rm -rf /var/cache/apk/*

# Install plugin Jenkins
USER jenkins
COPY ./config/plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/plugins.txt | tr '\n' ' ')

# Setup version Jenkins
RUN echo $(java -jar /usr/share/jenkins/jenkins.war --version) > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state
