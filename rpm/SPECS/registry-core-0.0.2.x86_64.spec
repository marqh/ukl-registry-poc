
Name:		registry-core
Version:	0.0.2
Release:	1
Summary:	ukgov linked data registry

License:	apache
URL:		https://github.com/UKGovLD/registry-core
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	java-1.7.0-openjdk
Requires:	nginx
Requires:	tomcat7


%description
ukgov linked data registry - core


%prep
%setup -q 


%install
rm -rf $RPM_BUILD_ROOT/*
install -D etc/sudoers.d/ukldSudoers.conf $RPM_BUILD_ROOT/etc/sudoers.d/ukldSudoers.conf
mkdir -p $RPM_BUILD_ROOT/opt/ldregistry/ui
mkdir -p $RPM_BUILD_ROOT/var/opt/ldregistry
mkdir -p $RPM_BUILD_ROOT/var/log/ldregistry
install -D var/lib/tomcat7/webapps/ROOT.war $RPM_BUILD_ROOT/var/lib/tomcat7/webapps/ROOT.war

%pre

alternatives --set java /usr/lib/jvm/jre-1.7.0-openjdk.x86_64/bin/java
service tomcat7 stop

%post

service tomcat7 start

%clean
rm -rf $RPM_BUILD_ROOT/*

%postun

if [ -d /opt/ldregistry]; then
rm -rf /opt/ldregistry
fi
if [ -d /var/opt/ldregistry]; then
rm -rf /var/opt/ldregistry
fi
if [ -d /var/log/ldregistry]; then
rm -rf /var/log/ldregistry
fi

%files
/etc/sudoers.d/ukldSudoers.conf
%defattr(775,root,tomcat,-)
/var/lib/tomcat7/webapps/ROOT.war
%dir /opt/ldregistry
%dir /opt/ldregistry/ui
%dir /var/opt/ldregistry
%dir /var/log/ldregistry


%changelog
* Wed Feb 19 2014 Mark Hedley <mark.hedley@metoffice.gov.uk> - 1.0-1
- initial

