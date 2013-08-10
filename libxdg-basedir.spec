%define		gitver	e44a9fe6006d730ada4d18aee8ac0f53c402e347

Summary:	An implementation of the XDG Base Directory specification
Name:		libxdg-basedir
Version:	1.2.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://repo.or.cz/w/libxdg-basedir.git/snapshot/%{gitver}.tar.gz
# Source0-md5:	176b15af56111e3c885710ff2e6bb76c
Patch0:		%{name}-am.patch
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of the XDG Base Directory specification.

%package devel
Summary:	Header files for libxdg-basedir library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libxdg-basedir library.

%prep
%setup -qn %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxdg-basedir.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.1
%attr(755,root,root) %{_libdir}/%{name}.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}.so
%{_includedir}/basedir.h
%{_includedir}/basedir_fs.h
%{_pkgconfigdir}/%{name}.pc

