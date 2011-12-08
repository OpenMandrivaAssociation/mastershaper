%define name mastershaper
%define version 0.44
%define prerelease  c
%define release %mkrel 6
%define _webdir /var/www

%define _requires_exceptions pear(jpgraph/jpgraph_bar.php)\\|pear(jpgraph/jpgraph_line.php)\\|pear(jpgraph/jpgraph.php)\\|pear(jpgraph/jpgraph_pie3d.php)\\|pear(jpgraph/jpgraph_pie.php)

Summary: Network traffic shaper which provides an Web Interface for Quality of Servcie
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}_%{version}.tar.bz2
Source1: master_shaper_quick_setup
Source2: mastershaper.init
Patch0: mastershaper_shaper_stat.patch
Patch1: mastershaper_tc_collector.patch
License: GPL
Group: System/Configuration/Networking
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://shaper.netshadow.at/
Requires: apache, php-pear, php-jpgraph, php-pear-Net_IPv4, php-gd, php-mysql, apache-mod_php, mysql, php-layersmenu
Buildarch: noarch

%description
The MasterShaper is an network traffic shaper which provides an Web Interface
for Quality of Servcie (QoS) functions of newer Linux 2.4- & 2.6-Kernel-Series
external link.
It targets to let users learn and use traffic shaping mechanism. This should 
be possible for everyone who has no deeper knowledge of Linux and the difficult
syntax of the tc commands from the iproute2external link package.

It provides an Web Interface which lets you define bandwidth pipes and filter
(IP, MAC, ports, protocols, ipp2pexternal link, layer7-filterexternal link..).
Also it draws some graphs about the current bandwidth usage and distribution.
There is no more need for any shell access or privileged users.

%prep
%setup -q -n MasterShaper-%{version}
%patch0 -p0
%patch1 -p0

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_webdir}/shaper/
mkdir -p $RPM_BUILD_ROOT%{_prefix}/share/doc/%name/
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_initrddir}
#cp %{SOURCE1} $RPM_BUILD_ROOT%{_prefix}/share/doc/%name/master_shaper_quick_setup
cp -v %{SOURCE1} %{_builddir}/MasterShaper-%version/master_shaper_quick_setup
cp %{SOURCE2} $RPM_BUILD_ROOT%{_initrddir}/mastershaper
mv -v htdocs/tc_collector.pl $RPM_BUILD_ROOT%{_bindir}
cp -a htdocs/* $RPM_BUILD_ROOT%{_webdir}/shaper/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_post_service mastershaper

%preun
%_preun_service mastershaper

%files
%defattr(-,root,root)
%doc docs/ INSTALL LICENSE README tools/ master_shaper_quick_setup
%attr(755,root,root) %{_initrddir}/mastershaper
%attr(644,root,root) %{_webdir}/shaper/*.php
%attr(644,root,root) %{_webdir}/shaper/*.css
%attr(644,root,root) %{_webdir}/shaper/images/*
%attr(644,root,root) %{_webdir}/shaper/setup/*
%attr(644,root,root) %{_webdir}/shaper/icons/*
%attr(644,root,root) %{_webdir}/shaper/*.js
%attr(644,root,root) %{_webdir}/shaper/favicon.ico
%attr(644,root,root) %{_webdir}/shaper/icons.dat
%attr(644,root,root) %{_webdir}/shaper/ms_menu.txt
%attr(755,root,root) %{_webdir}/shaper/shaper_loader.sh
%attr(755,root,root) %{_bindir}/tc_collector.pl

