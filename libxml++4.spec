#
# Conditional build:
%bcond_without	static_libs	# static library
#
%define	glibmm_ver	2.68.0
Summary:	C++ interface for working with XML files
Summary(pl.UTF-8):	Interfejs C++ do pracy z plikami XML
Name:		libxml++4
Version:	4.0.3
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	https://download.gnome.org/sources/libxml++/4.0/libxml++-%{version}.tar.xz
# Source0-md5:	4fb9ca065659856aef74b37ff53e20ef
URL:		http://libxmlplusplus.sourceforge.net/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.11
BuildRequires:	docbook-dtd50-xml
BuildRequires:	docbook-style-xsl-ns
BuildRequires:	doxygen >= 1:1.8.9
BuildRequires:	glibmm2.68-devel >= %{glibmm_ver}
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-devel >= 1:2.7.7
BuildRequires:	mm-common >= 0.9.10
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.752
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glibmm2.68 >= %{glibmm_ver}
Requires:	libxml2 >= 1:2.7.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libxml++ is a C++ interface for the libxml XML parser library.

%description -l pl.UTF-8
libxml++ jest interfejsem C++ do biblioteki libxml.

%package devel
Summary:	Header files for libxml++
Summary(pl.UTF-8):	Pliki nagłówkowe do libxml++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm2.68-devel >= %{glibmm_ver}
Requires:	libstdc++-devel >= 6:7
Requires:	libxml2-devel >= 1:2.7.7

%description devel
Header files for libxml++.

%description devel -l pl.UTF-8
Pliki nagłówkowe do libxml++.

%package static
Summary:	Static libxml++ libraries
Summary(pl.UTF-8):	Biblioteka statyczna libxml++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxml++ libraries.

%description static -l pl.UTF-8
Biblioteka statyczna libxml++.

%package apidocs
Summary:	libxml++ API documentation
Summary(pl.UTF-8):	Dokumentacja API libxml++
Group:		Documentation
BuildArch:	noarch

%description apidocs
libxml++ API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libxml++.

%package examples
Summary:	libxml++ - example programs
Summary(pl.UTF-8):	libxml++ - przykładowe programy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description examples
libxml++ - example programs.

%description examples -l pl.UTF-8
libxml++ - przykładowe programy.

%prep
%setup -q -n libxml++-%{version}

%build
mm-common-prepare --copy --force
%{__libtoolize}
%{__aclocal} -I build
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_static_libs:--enable-static} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxml++-4.0.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README.md
%attr(755,root,root) %{_libdir}/libxml++-4.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxml++-4.0.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxml++-4.0.so
%{_libdir}/libxml++-4.0
%{_includedir}/libxml++-4.0
%{_pkgconfigdir}/libxml++-4.0.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libxml++-4.0.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_datadir}/devhelp/books/libxml++-4.0
%{_docdir}/libxml++-4.0

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
