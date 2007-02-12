Summary:	Fast Assembly MPEG Encoder
Summary(pl.UTF-8):	Szybki koder MPEG w asemblerze
Name:		fame
Version:	0.9.0
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/fame/%{name}-%{version}.tar.gz
# Source0-md5:	4e70f10250e95d6867160f674b91ca93
URL:		http://fame.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libfame-devel
BuildRequires:	libstdc++ >= 2.10.0
BuildRequires:	nasm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An MPEG encoder optimized for Pentium MMX technology. It can capture
video from various sources and create an MPEG 1 video elementary
stream, which is then recorded in a file or sent over a network. This
is a beta release.

%description -l pl.UTF-8
Koder MPEG zoptymalizowany dla Pentium MMX. Może łapać ramki z różnych
źródeł i tworzyć podstawowy strumień MPEG 1, który może być potem
zapisywany do pliku lub wysyłany przez sieć.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES BUGS README TODO
%attr(755,root,root) %{_bindir}/fame
%{_mandir}/man1/*
