
%define plugin	rssreader
%define name	vdr-plugin-%plugin
%define version	1.6.0
%define rel	2

Summary:	VDR plugin: RSS Reader for OSD
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.saunalahti.fi/~rahrenbe/vdr/rssreader/
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

install -D -m644 example/rssreader.conf %{buildroot}%{_vdr_plugin_cfgdir}/rssreader.conf

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%config(noreplace) %{_vdr_plugin_cfgdir}/rssreader.conf


