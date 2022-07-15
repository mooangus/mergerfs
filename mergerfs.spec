Name:     mergerfs
Version:  2.33.5
Release:  2%{?dist}
Summary:  A featureful FUSE based union filesystem

Group:    Applications/System
License:	ISC
URL:      https://github.com/trapexit/mergerfs

Source:   https://github.com/trapexit/mergerfs/releases/download/%{version}/mergerfs-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:	git

Requires:	fuse

%global debug_package %{nil}

%prep
%setup -q

%description
mergerfs is a union filesystem geared towards simplifying storage and
management of files across numerous commodity storage devices. It is
similar to mhddfs, unionfs, and aufs.

%build
find %{buildroot} -iname Makefile
sed 's/chown/echo/g' /builddir/build/SOURCES/mergerfs%{version}/libfuse/Makefile > /builddir/build/SOURCES/mergerfs-%{version}/libfuse/Makefile
make %{?_smp_mflags}

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
/usr/bin/mergerfs
/usr/bin/mergerfs-fusermount
/sbin/mount.mergerfs
%doc %{_mandir}/*

%changelog
