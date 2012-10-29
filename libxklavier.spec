Summary:	libXklavier library
Name:		libxklavier
Version:	5.3
Release:	1
License:	GPLv2 / LGPL v2
Group:		Libraries
Source0:	http://download.gnome.org/sources/libxklavier/5.3/%{name}-%{version}.tar.xz
# Source0-md5:	290ea2a8abc40f78a3a16bdae6f02808
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
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
cp /usr/share/gettext/config.rpath .
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static			\
	--with-html-dir=%{_gtkdocdir}		\
	--with-xkb-base=%{_datadir}/X11/xkb	\
	--with-xkb-bin-base=%{_bindir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/*
%{_datadir}/gir-1.0/Xkl-1.0.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/%{name}

