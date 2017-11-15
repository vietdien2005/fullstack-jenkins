FROM jenkins:latest

MAINTAINER Dam Viet "vietdien2005@gmail.com"

ENV DEBIAN_FRONTEND noninteractive

USER root

# Add Basic Source List Debian Jessie
RUN echo "deb-src http://httpredir.debian.org/debian jessie main" >> /etc/apt/sources.list
RUN echo "deb-src http://httpredir.debian.org/debian jessie-updates main" >> /etc/apt/sources.list
RUN echo "deb-src http://security.debian.org jessie/updates main" >> /etc/apt/sources.list

# Basic tools
RUN apt-get update && apt-get -y install sudo git ant ant-contrib doxygen sqlite3 wget vim python python-dev ca-certificates \
    dialog gcc musl-dev libffi-dev python-pip zip unzip iputils-ping curl apt-transport-https \
    autoconf automake build-essential \
    libxslt1-dev re2c libxml2 libxml2-dev  \
    bison libbz2-dev libreadline-dev \
    libfreetype6 libfreetype6-dev libjpeg-dev libgd-dev libgd3 libxpm4 \
    libssl-dev openssl \
    gettext libgettextpo-dev libgettextpo0 \
    libicu-dev \
    libmhash2 libmhash-dev \
    libmcrypt4 libmcrypt-dev \
    libpcre3-dev libpcre++-dev libgconf-2-4 xvfb libxi6

# Install Php 7.0
RUN apt-get update && apt-get -y install php7.0 php7.0-cli php7.0-cgi php7.0-common php7.0-curl php7.0-dba php7.0-dev \
    php7.0-fpm php7.0-gd php7.0-gmp php7.0-imap php7.0-intl php7.0-json php7.0-mbstring php7.0-mcrypt php7.0-mysql \
    php7.0-odbc php7.0-opcache php7.0-pgsql php7.0-pspell php7.0-readline php7.0-recode php7.0-sqlite3 php7.0-tidy \
    php7.0-xml php7.0-xmlrpc php7.0-xsl php7.0-zip 

# Install php tools
RUN  mkdir -p /usr/bin \
	&& wget -q -O /usr/bin/phpunit https://phar.phpunit.de/phpunit.phar && chmod +x /usr/bin/phpunit \
	&& wget -q -O /usr/bin/composer https://getcomposer.org/composer.phar && chmod +x /usr/bin/composer \
	&& wget -q -O /usr/bin/phpmd http://static.phpmd.org/php/latest/phpmd.phar && chmod +x /usr/bin/phpmd \
	&& wget -q -O /usr/bin/sami http://get.sensiolabs.org/sami.phar && chmod +x /usr/bin/sami \
	&& wget -q -O /usr/bin/phpcov https://phar.phpunit.de/phpcov.phar && chmod +x /usr/bin/phpcov \
	&& wget -q -O /usr/bin/phpcpd https://phar.phpunit.de/phpcpd.phar && chmod +x /usr/bin/phpcpd \
	&& wget -q -O /usr/bin/phploc https://phar.phpunit.de/phploc.phar && chmod +x /usr/bin/phploc \
	&& wget -q -O /usr/bin/phptok https://phar.phpunit.de/phptok.phar && chmod +x /usr/bin/phptok \
	&& wget -q -O /usr/bin/phpdox https://github.com/theseer/phpdox/releases/download/0.10.1/phpdox-0.10.1.phar && chmod +x /usr/bin/phpdox \
	&& wget -q -O /usr/bin/box https://github.com/box-project/box2/releases/download/2.7.5/box-2.7.5.phar && chmod +x /usr/bin/box \
	&& wget -q -O /usr/bin/phpbrew https://github.com/phpbrew/phpbrew/raw/master/phpbrew && chmod +x /usr/bin/phpbrew

# Update Timezone. Hello, I'm from Ho Chi Minh, Vietnam
RUN echo "Asia/Ho_Chi_Minh" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

# Install environment testing with selenium
RUN pip install selenium==3.3.1 virtualenv nose

# Install NodeJS & Packages Global
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \
	apt-get update && \
	apt-get install nodejs && \
	npm install -g n && \
	n latest

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \
	echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list && \
	apt-get update && \
	apt-get install yarn && \
	yarn global add mocha gulp webpack jscs standard webpack-dev-server

# Clean packages 
RUN apt-get -q clean -y \
	&& apt-get -q autoclean -y \
	&& apt-get -q autoremove -y \
	&& rm -rf /var/lib/{apt,dpkg,cache,log}/ \
	&& rm -rf /var/lib/apt/lists/*

# Setup Jenkins
COPY config/config.xml /usr/share/jenkins/ref/config.xml
COPY config/jenkins.model.JenkinsLocationConfiguration.xml /usr/share/jenkins/ref/jenkins.model.JenkinsLocationConfiguration.xml
COPY config/nodeMonitors.xml /usr/share/jenkins/ref/nodeMonitors.xml
COPY config/org.codefirst.SimpleThemeDecorator.xml /usr/share/jenkins/ref/org.codefirst.SimpleThemeDecorator.xml
COPY config/thinBackup.xml /usr/share/jenkins/ref/thinBackup.xml
COPY config/users /usr/share/jenkins/ref/users

# Install plugin Jenkins
USER jenkins
COPY config/plugins.txt /usr/share/jenkins/plugins.txt
RUN /usr/local/bin/install-plugins.sh $(cat /usr/share/jenkins/plugins.txt | tr '\n' ' ')

RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state

CMD java ${JVM_OPTS} \
	-Djenkins.install.runSetupWizard=false \
	-jar /usr/share/jenkins/jenkins.war \
	${JENKINS_OPTS}