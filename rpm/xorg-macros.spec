Summary: X.Org X11 Autotools macros
Name: xorg-macros
Version: 0.0.0
Release: 1
License: MIT
Group: Development/System
URL: http://www.x.org
BuildArch: noarch
Source0:  xorg-macros-%{version}.tar.bz2
Requires: autoconf automake libtool pkgconfig
 
%description
X.Org X11 autotools macros required for building the various packages that
comprise the X Window System.
 
%prep
%setup -q -n %{pkgname}-%{version}/xorg-macros
 
%build
%autogen
%configure
make %{?_smp_mflags}
 
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
rm -f $RPM_BUILD_ROOT%{_datadir}/util-macros/INSTALL
 
%files
%defattr(-,root,root,-)
%doc COPYING
%{_datadir}/aclocal/xorg-macros.m4
%{_datadir}/pkgconfig/xorg-macros.pc
