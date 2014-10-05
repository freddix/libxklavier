Summary:	libXklavier library
Name:		libxklavier
Version:	5.4
Release:	1
License:	GPLv2 / LGPL v2
Group:		Libraries
Source0:	http://cgit.freedesktop.org/libxklavier/snapshot/%{name}-%{version}.tar.gz
# Source0-md5:	a151d7ab853b5862ef0e7fd749da5d9b
URL:		http://www.freedesktop.org/Software/LibXklavier
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk-doc
BuildRequires:	iso-codes
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	xorg-libxkbfile-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you simplify XKB-related development.

%package devel
Summary:	Header files to develop libxklavier applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files to develop libxklavier applications.

%package apidocs
Summary:	libXklavier API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libXklavier API documentation.

%prep
%setup -q

%build
%{__libtoolize}
%{__gtkdocize}
cp /usr/share/gettext/config.rpath build-aux
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules			\
	--disable-static			\
	--with-html-dir=%{_gtkdocdir}		\
	--with-xkb-base=%{_datadir}/X11/xkb	\
	--with-xkb-bin-base=%{_bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %ghost %{_libdir}/lib*.so.??
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/girepository-1.0/Xkl-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc
%{_includedir}/*
%{_datadir}/gir-1.0/Xkl-1.0.gir
%{_datadir}/vala/vapi/libxklavier.deps
%{_datadir}/vala/vapi/libxklavier.vapi

%if 0
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}
%endif

