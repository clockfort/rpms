# $Id$
# Authority: dries
# Upstream:

%define real_version 2.0.0-pre5

%{?dist: %{expand: %%define %dist 1}}

%{?fc1:%define _without_xorg 1}
%{?el3:%define _without_xorg 1}
%{?rh9:%define _without_xorg 1}
%{?rh8:%define _without_xorg 1}
%{?rh7:%define _without_xorg 1}
%{?el2:%define _without_xorg 1}
%{?rh6:%define _without_xorg 1}
%{?yd3:%define _without_xorg 1}

Summary: 1394-based digital camera control library
Name: libdc1394
Version: 2.0.0
Release: 0.1.pre5.2
License: LGPL
Group: System Environment/Libraries
URL: http://sourceforge.net/projects/libdc1394/

Source: http://dl.sf.net/libdc1394/libdc1394-%{real_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: libraw1394-devel, gcc-c++
%{?_without_xorg:BuildRequires: XFree86-devel}
%{!?_without_xorg:BuildRequires: xorg-x11-devel}

%description
Libdc1394 is a library that is intended to provide a high level programming
interface for application developers who wish to control IEEE 1394 based
cameras that conform to the 1394-based Digital Camera Specification.

%package devel
Summary: Header files, libraries and development documentation for %{name}.
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, libraw1394-devel

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -n libdc1394-%{real_version}

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING NEWS README
%{_bindir}/dc1394_vloopback
%{_libdir}/libdc1394*.so.*

%files devel
%defattr(-, root, root, 0755)
%{_includedir}/libdc1394/
%{_libdir}/libdc1394*.a
%{_libdir}/libdc1394*.so
%exclude %{_libdir}/*.la

%changelog
* Sat Apr 08 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.0-0.1.pre5.2
- Rebuild for Fedora Core 5.

* Thu Dec  8 2005 Matthias Saou <http://freshrpms.net/> 2.0.0-0.1.pre5
- Update to 2.0.0-pre5.
- Add missing libraw1394-devel dependency to the devel package.

* Tue Aug 30 2005 Dries Verachtert <dries@ulyssis.org> - 2.0.0-0.pre4
- Update to release 2.0.0-0.pre4.

* Thu Aug 25 2005 Dries Verachtert <dries@ulyssis.org> - 1.1.0-1
- Initial package.

