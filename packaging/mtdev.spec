Name:           mtdev
Version:        1.1.3
Release:        0
License:        MIT
Summary:        Multitouch Protocol Translation Library
Url:            http://bitmath.org/code/mtdev/
Group:          System/Libraries
Source:         http://bitmath.org/code/mtdev/mtdev-%{version}.tar.bz2
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

%post -n libmtdev -p /sbin/ldconfig

%postun -n libmtdev -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc COPYING 
%{_bindir}/*

%files -n libmtdev
%defattr(-, root, root)
%{_libdir}/lib*.so.*

%files devel
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%changelog
