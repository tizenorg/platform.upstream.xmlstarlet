Name:           xmlstarlet
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel >= 2.6.27
BuildRequires:  libxslt-devel >= 1.1.9
BuildRequires:  pkgconfig
#BuildRequires:  sgml-skel
Summary:        Command Line Tool to Process XML Documents
License:        MIT
Group:          Productivity/Publishing/XML
Version:        1.4.1
Release:        0
Source:         http://prdownloads.sourceforge.net/xmlstar/xmlstarlet-%{version}.tar.gz
#Source1:        %{name}-rpmlintrc
#Patch2:         %{name}-xml_depyx.c.diff
#BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            http://sourceforge.net/projects/xmlstar/
requires: libxml2

%description
XMLStarlet (xml) is a command line XML toolkit which can be used to
transform, query, validate, and edit XML documents and files using
simple set of shell commands in similar way it is done for plain text
files using 'grep', 'sed', 'awk', 'tr', 'diff', or 'patch'.

%prep
%setup -q
#%patch2

%build
export CFLAGS="$RPM_OPT_FLAGS -W -Wall"
%configure \
    --disable-static-libs

%__make %{?_smp_mflags}

%check
%__make tests

%install
%makeinstall
#ln -s %{buildroot}/usr/bin/xml %{buildroot}/usr/bin/xmlstarlet

#install -d _docs
#%__mv "%{buildroot}%{_datadir}/doc"/* _docs/
#%__rm -rf "%{buildroot}%{_datadir}/doc"
rm -rf %{buildroot}/usr/share

%post
ln -s /usr/bin/xml /usr/bin/xmlstarlet

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-, root, root)
#%doc AUTHORS ChangeLog NEWS README Copyright TODO
#%doc _docs/*
%{_bindir}/xml
#%{_bindir}/xmlstarlet
#%doc %{_mandir}/man1/xmlstarlet.1%{ext_man}

%changelog
