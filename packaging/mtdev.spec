#
# spec file for package mtdev
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           mtdev
Version:        1.1.0
Release:        0
License:        MIT
Summary:        Multitouch Protocol Translation Library
Url:            http://bitmath.org/code/mtdev/
Group:          System/Libraries
Source:         http://bitmath.org/code/mtdev/mtdev-%{version}.tar.bz2
Patch1:         U_mtdev_close-should-ignore-NULL-devices.patch
Patch2:         U_Return-EINVAL-for-invalid-parameters-on-mtdev_init.patch
Patch3:         mtdev-implicit.diff
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The mtdev is a stand-alone library which transforms all variants of kernel MT events to the slotted type B protocol. The events put into mtdev may be from any MT device, specifically type A without contact tracking, type A with contact tracking, or type B with contact tracking. See the kernel documentation for further details.

%package -n libmtdev1
Summary:        Multitouch Protocol Translation Library
Group:          System/Libraries

%description -n libmtdev1
The mtdev is a stand-alone library which transforms all variants of kernel MT events to the slotted type B protocol. The events put into mtdev may be from any MT device, specifically type A without contact tracking, type A with contact tracking, or type B with contact tracking. See the kernel documentation for further details.

%package devel
Summary:        Development package for mtdev library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libmtdev1 = %{version}

%description devel
This package contains the files needed to compile programs that use mtdev library.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%post -n libmtdev1 -p /sbin/ldconfig

%postun -n libmtdev1 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc COPYING ChangeLog README
%{_bindir}/*

%files -n libmtdev1
%defattr(-, root, root)
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%changelog