Name:      fame
Summary:   Fast Assembly MPEG Encoder
Version:   0.1.3
Release:   1
Copyright: GPL
Group:     Applications/Graphics
Source:    http://www.enst-bretagne.fr/~chappeli/fame/download/%{name}-%{version}.tar.gz
URL:       http://www.enst-bretagne.fr/~chappeli/fame/
Packager:  Jan ONDREJ (SAL) <ondrejj@salstar.shadow.sk>
Buildroot: /tmp/%{name}-root

%description
An MPEG encoder optimized for Pentium MMX technology.
It can capture video from various sources and create an MPEG 1 video elementary
stream, which is then recorded in a file or sent over a network.
This is a beta release.

%prep
%setup -n fame

%build
./configure --prefix=/usr
make

%install
make install prefix=$RPM_BUILD_ROOT/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS COPYING CHANGES BUGS README TODO doc/
/usr/bin/fame
/usr/bin/mpegnc
/usr/lib/fame/*/*.so
/usr/man/man1/*

%changelog
* Mon May 15 2000 Jan ONDREJ (SAL) <ondrejj@salstar.shadow.sk>
- added mpegnc binary
- added all modules in /usr/lib/fame/*/
