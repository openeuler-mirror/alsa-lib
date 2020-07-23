Name:	 alsa-lib
Version: 1.2.3
Release: 1
Summary: the user space library that developers compile ALSA applications against

License: LGPLv2+
URL:     https://alsa-project.org/
Source0: https://www.alsa-project.org/files/pub/lib/%{name}-%{version}.tar.bz2
Source10: asound.conf

BuildRequires: autoconf, automake, libtool, doxygen
Requires: coreutils

%description
The alsa-lib is a library to interface with ALSA in the Linux kernel
and virtual devices using a plugin system.
More detail: https://alsa.opensrc.org/Alsa-lib

%package devel
Summary:  Development header files
Requires: %{name} = %{version}
Requires: pkgconfig
Provides: %{name}-devel = %{version}
Provides: pkgconfig(alsa)

%description devel
This package contains libraries and header files for the ALSA development.

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -vif
%configure --disable-aload \
           --with-plugindir=%{_libdir}/alsa-lib \
           --disable-alisp 

%disable_rpath

make %{?_smp_mflags} VERBOSE=1
make doc %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# the asound.conf configuration files are required for ALSA to work properly
mkdir -p -m 755 %{buildroot}%{_sysconfdir} 
install -p -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}

%ldconfig_scriptlets

%files
%license COPYING
%doc doc/asoundrc.txt 
%{_sysconfdir}/*.conf
%{_bindir}/*
%{_libdir}/libasound.so.*
%{_libdir}/libatopology.so.*
%{_datadir}/alsa/*

%files devel
%doc doc/doxygen/ TODO
%{_libdir}/libasound.so
%{_libdir}/libatopology.so
%exclude %{_libdir}/libasound.la
%exclude %{_libdir}/libatopology.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/aclocal/*.m4


%changelog
* Wed Jul 22 2020 jinzhimin <jinzhimin2@huawei.com> - 1.2.3-1
- update to 1.2.3

* Fri Apr 24 2020 SuperHugePan <zhangpan26@huawei.com> - 1.2.2-1
- update to 1.2.2

* Fri Jan 10 2020 SuperHugePan <zhangpan26@huawei.com> - 1.1.6-6
- remove useless code

* Thu Oct 24 2019 caomeng <caomeng5@huawei.com> - 1.1.6-5
- Type:NA
- ID:NA
- SUG:NA
- DESC:delete build requirement alsa-utils

* Mon Aug 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.6-4
- Package init
