Name:           mtdev
Version:        1.1.5
Release:        0
License:        MIT
Summary:        Multitouch Protocol Translation Library
Url:            http://bitmath.org/code/mtdev/
Group:          System/Libraries
Source:         http://bitmath.org/code/mtdev/mtdev-%{version}.tar.bz2
Source1001:     mtdev.manifest
BuildRequires:  pkgconfig

%description
The mtdev is a stand-alone library which transforms all variants of kernel MT events to the slotted type B protocol. The events put into mtdev may be from any MT device, specifically type A without contact tracking, type A with contact tracking, or type B with contact tracking. See the kernel documentation for further details.

%package -n libmtdev
Summary:        Multitouch Protocol Translation Library
Group:          System/Libraries

%description -n libmtdev
The mtdev is a stand-alone library which transforms all variants of kernel MT events to the slotted type B protocol. The events put into mtdev may be from any MT device, specifically type A without contact tracking, type A with contact tracking, or type B with contact tracking. See the kernel documentation for further details.

%package devel
Summary:        Development package for mtdev library
Group:          System/Libraries
Requires:       glibc-devel
Requires:       libmtdev = %{version}

%description devel
This package contains the files needed to compile programs that use mtdev library.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%reconfigure --disable-static
%__make %{?_smp_mflags}

%install
%make_install

%post -n libmtdev -p /sbin/ldconfig

%postun -n libmtdev -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-, root, root)
%license COPYING 
%{_bindir}/*

%files -n libmtdev
%manifest %{name}.manifest
%defattr(-, root, root)
%{_libdir}/lib*.so.*

%files devel
%manifest %{name}.manifest
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
