Summary:	Fast Assembly MPEG Encoder
Summary(pl):	Szybki koder MPEG w asemblerze
Name:		fame
Version:	0.8.10
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/fame/%{name}-%{version}.tar.gz
URL:		http://fame.sourceforge.net/
BuildRequires:	nasm
BuildRequires:	autoconf
BuildRequires:	libfame-devel
BuildRequires:	libstdc++ >= 2.10.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An MPEG encoder optimized for Pentium MMX technology. It can capture
video from various sources and create an MPEG 1 video elementary
stream, which is then recorded in a file or sent over a network. This
is a beta release.

%description -l pl
Koder MPEG zoptymalizowany dla Pentium MMX. Mo�e �apa� ramki z r�nych
�r�de� i tworzy� podstawowy strumie� MPEG 1, kt�ry mo�e by� potem
zapisywany do pliku lub wysy�any przez sie�.

%prep
%setup -q

%build
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT%{_prefix} mandir=$RPM_BUILD_ROOT%{_mandir} libdir=$RPM_BUILD_ROOT%{_libdir} bindir=$RPM_BUILD_ROOT%{_bindir}

gzip -9nf AUTHORS CHANGES BUGS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,CHANGES,BUGS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/fame
%{_mandir}/man1/*
