Name:		fame
Summary:	Fast Assembly MPEG Encoder
Version:	0.8.7
Release:	1
License:	GPL
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/fame/%{name}-%{version}.tar.gz
URL:		http://fame.sourceforge.net/
BuildRequires:	nasm
BuildRequires:	libstdc++ >= 2.10.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An MPEG encoder optimized for Pentium MMX technology. It can capture
video from various sources and create an MPEG 1 video elementary
stream, which is then recorded in a file or sent over a network. This
is a beta release.

%prep
%setup -q -n fame

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING CHANGES BUGS README TODO doc/
%attr(755,root,root) %{_bindir}/fame
%attr(755,root,root) %{_bindir}/mpegnc
%{_libdir}/fame/*/*.so
%{_mandir}/man1/*
