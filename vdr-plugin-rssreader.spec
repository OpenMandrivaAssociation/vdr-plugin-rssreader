
%define plugin	rssreader
%define name	vdr-plugin-%plugin
%define version	1.6.4
%define rel	2

Summary:	VDR plugin: RSS Reader for OSD
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPLv2+
URL:		https://www.saunalahti.fi/~rahrenbe/vdr/rssreader/
Source:		http://www.saunalahti.fi/~rahrenbe/vdr/rssreader/files/vdr-%plugin-%version.tgz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	expat-devel
BuildRequires:	curl-devel
Requires:	vdr-abi = %vdr_abi

%description
The RSS Reader plugin provides a simple OSD menu based user interface
for reading user-defined RSS streams.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -D -m644 rssreader/rssreader.conf %{buildroot}%{_vdr_plugin_cfgdir}/%plugin/rssreader.conf

%clean
rm -rf %{buildroot}

%post
# Move config file when migrating from 1.6.0
if [ -e %{_vdr_plugin_cfgdir}/rssreader.conf ] && [ "$1" = "2" ] && 
	/bin/rpm -V --nodeps --noscript -f %{_vdr_plugin_cfgdir}/rssreader.conf | grep -q '^..5.*%{_vdr_plugin_cfgdir}/rssreader.conf'; then
	mv -v %{_vdr_plugin_cfgdir}/%plugin/rssreader.conf %{_vdr_plugin_cfgdir}/%plugin/rssreader.conf.rpmnew
	mv -v %{_vdr_plugin_cfgdir}/rssreader.conf %{_vdr_plugin_cfgdir}/%plugin/rssreader.conf
fi
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%dir %{_vdr_plugin_cfgdir}/%plugin
%config(noreplace) %{_vdr_plugin_cfgdir}/%plugin/rssreader.conf


