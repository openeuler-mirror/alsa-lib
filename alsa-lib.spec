Name:	 alsa-lib
Version: 1.1.6
Release: 5
Summary: the user space library that developers compile ALSA applications against

License: LGPLv2+
URL:     https://alsa-project.org/
Source0: https://www.alsa-project.org/files/pub/lib/%{name}-%{version}.tar.bz2
Source10: asound.conf
Source11: modprobe-dist-alsa.conf
Source12: modprobe-dist-oss.conf

Patch0:   alsa-lib-1.0.24-config.patch
Patch1:   alsa-lib-1.0.14-glibc-open.patch
Patch2:   alsa-lib-addon-dir.patch

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

# install alsa modprobe configure file ,backup  oss modprobe configure file
mkdir -p -m 755 %{buildroot}%{_prefix}/lib/modprobe.d/
install -p -m 0644 %{SOURCE11} %{buildroot}%{_prefix}/lib/modprobe.d/dist-alsa.conf

mkdir -p -m 755 %{buildroot}/%{_defaultdocdir}/%{name}
install -p -m 0644 %{SOURCE12} %{buildroot}%{_defaultdocdir}/%{name}/

%ldconfig_scriptlets

%files
%license COPYING
%doc doc/asoundrc.txt 
%{_sysconfdir}/*.conf
%{_prefix}/lib/modprobe.d/*.conf
%{_defaultdocdir}/%{name}/*.conf
%{_bindir}/*
%{_libdir}/libasound.so.*
%{_datadir}/alsa/*

%files devel
%doc doc/doxygen/ TODO
%{_libdir}/libasound.so
%exclude %{_libdir}/libasound.la
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/aclocal/*.m4


%changelog
* Thu Oct 24 2019 caomeng <caomeng5@huawei.com> - 1.1.6-5
- Type:NA
- ID:NA
- SUG:NA
- DESC:delete build requirement alsa-utils

* Mon Aug 19 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.1.6-4
- Package init
