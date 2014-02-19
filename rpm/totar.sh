#!/bin/bash

mkdir registry-core-0.0.2
mkdir -p registry-core-0.0.2/var/lib/tomcat7/webapps/
mkdir -p registry-core-0.0.2/etc/sudoers.d/

wget --no-check-certificate https://exvmidebldprod01:8443/jenkins/job/ukl-registry-develop-SNAPSHOT/lastSuccessfulBuild/artifact/target/registry-core-0.0.2.war 

mv registry-core-0.0.2.war registry-core-0.0.2/var/lib/tomcat7/webapps/ROOT.war

echo -e '## enable tomcat sudo access to run proxy dynamic reconfigure script\nDefaults:tomcat !requiretty\nDefaults:ec2-user !requiretty\ntomcat     ALL=NOPASSWD: /opt/ldregistry/proxy-conf.sh\nec2-user     ALL=NOPASSWD: /opt/ldregistry/proxy-conf.sh' > registry-core-0.0.2/etc/sudoers.d/ukldSudoers.conf

tar -cvf registry-core-0.0.2.tar.gz registry-core-0.0.2

rm -rf registry-core-0.0.2

mv registry-core-0.0.2.tar.gz ~/rpmbuild/SOURCES/