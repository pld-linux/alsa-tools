#
# TODO: make description true (i.e. separate GUIs)
# echomixer,envy24control,rmedigicontrol use GTK+ 2
# hdspconf,hdspmixer use FLTK
# qlo10k1 uses Qt 3
#
# Conditional build:
%bcond_with	hotplug		# build with hotplug support for Tascam USB devices
#
Summary:	Advanced Linux Sound Architecture (ALSA) - tools
Summary(pl.UTF-8):	Advanced Linux Sound Architecture (ALSA) - narzędzia
Name:		alsa-tools
Version:	1.0.23
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	ftp://ftp.alsa-project.org/pub/tools/%{name}-%{version}.tar.bz2
# Source0-md5:	f286616cf781c81b1636899a104129d1
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-sh.patch
Patch2:		%{name}-csp.patch
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= 1.0.3
BuildRequires:	autoconf
BuildRequires:	automake >= 1.3
BuildRequires:	flex
BuildRequires:	fltk-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	qt-devel
BuildRequires:	sed >= 4.0
# for lo10k1, qlo10k1
Requires:	liblo10k1 = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# ac3dec skipped - see ac3dec.spec
%define	progs	as10k1 echomixer envy24control hdspconf hdsploader hdspmixer ld10k1 mixartloader pcxhrloader rmedigicontrol sb16_csp seq/sbiload sscape_ctl us428control usx2yloader vxloader

%description
This packages contains command line utilities for the ALSA (Advanced
Linux Sound Architecture) project.

%description -l pl.UTF-8
Pakiet zawiera działające z linii poleceń narzędzia dla projektu ALSA
(Advanced Linux Sound Architecture).

%package tascam
Summary:	Hotplug support for Tascam USB devices
Summary(pl.UTF-8):	Wsparcie hotpluga do urządzeń USB Tascam
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	hotplug

%description tascam
Hotplug support for Tascam USB devices, firmware loader.

%description tascam -l pl.UTF-8
Wsparcie hotpluga do urządzeń USB Tascam, narzędzie do ładowania
firmware'u.

%package -n liblo10k1
Summary:	liblo10k1 library
Summary(pl.UTF-8):	Biblioteka liblo10k1
Group:		Libraries
Conflicts:	alsa-tools < 1.0.13

%description -n liblo10k1
liblo10k1 library.

%description -n liblo10k1 -l pl.UTF-8
Biblioteka liblo10k1.

%package -n liblo10k1-devel
Summary:	Header files for liblo10k1 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki liblo10k1
Group:		Development/Libraries
Requires:	liblo10k1 = %{version}-%{release}

%description -n liblo10k1-devel
Header files for liblo10k1 library.

%description -n liblo10k1-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki liblo10k1.

%package -n liblo10k1-static
Summary:	Static liblo10k1 library
Summary(pl.UTF-8):	Statyczna biblioteka liblo10k1
Group:		Development/Libraries
Requires:	liblo10k1-devel = %{version}-%{release}

%description -n liblo10k1-static
Static liblo10k1 library.

%description -n liblo10k1-static -l pl.UTF-8
Statyczna biblioteka liblo10k1.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# don't BR gtk+ 1.2
echo 'AC_DEFUN([AM_PATH_GTK],[])' > echomixer/acinclude.m4
echo 'AC_DEFUN([AM_PATH_GTK],[])' > envy24control/acinclude.m4
echo 'AC_DEFUN([AM_PATH_GTK],[])' > rmedigicontrol/acinclude.m4

%build
odir=$(pwd)
for dir in %{progs}; do
	cd $dir
	[ -f README ] && cp -f README "README.$(basename $dir)"
	[ -f NEWS ] && cp -f NEWS "NEWS.$(basename $dir)"
	[ -f TODO ] && cp -f TODO "TODO.$(basename $dir)"
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	grep -q AC_CONFIG_HEADER configure.* && %{__autoheader}
	%{__automake}
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
	CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
	%configure
	%{__make}
	cd $odir
done

cd qlo10k1
sed -i 's:include:include/qt:g' acinclude.m4
cp -f README README.qlo10k1
cp -f NEWS NEWS.qlo10k1
cp -f TODO TODO.qlo10k1
%{__libtoolize}
%{__aclocal} -I ../ld10k1
%{__autoconf}
%{__autoheader}
%{__automake}
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure \
	--with-qtdir=%{_prefix} \
	--disable-ld10k1test \
	--with-ld10k1-prefix=$odir/ld10k1/src \
	--with-ld10k1-inc-prefix=$odir/ld10k1/include
%{__make}

%{__make} -C $odir/as10k1/examples dsp

%install
rm -rf $RPM_BUILD_ROOT

sed -i -e 's,#!/bin/sh,#!/bin/bash,' ld10k1/setup/init_live

odir=$(pwd)
for dir in %{progs} qlo10k1; do
	%{__make} -C $dir install \
		DESTDIR=$RPM_BUILD_ROOT
done

install $odir/as10k1/examples/*.emu10k1 $RPM_BUILD_ROOT%{_datadir}/ld10k1/effects

%if %{without hotplug}
rm -r $RPM_BUILD_ROOT%{_sysconfdir}/hotplug
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n liblo10k1 -p /sbin/ldconfig
%postun	-n liblo10k1 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc */README.* */*/README.* */NEWS.* */TODO.*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/ld10k1
%{_mandir}/man1/*.1*
%{_desktopdir}/hdspconf.desktop
%{_desktopdir}/hdspmixer.desktop
%{_pixmapsdir}/hdspconf.png
%{_pixmapsdir}/hdspmixer.png
# for sbiload
%{_datadir}/sounds/opl3

%if %{with hotplug}
%files tascam
%defattr(644,root,root,755)
%attr(755,root,root) %{_sysconfdir}/hotplug/usb/tascam_fpga
%attr(755,root,root) %{_sysconfdir}/hotplug/usb/tascam_fw
%{_sysconfdir}/hotplug/usb/tascam_fw.usermap
%endif

%files -n liblo10k1
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblo10k1.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblo10k1.so.0

%files -n liblo10k1-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblo10k1.so
%{_libdir}/liblo10k1.la
%{_includedir}/lo10k1
%{_aclocaldir}/ld10k1.m4

#%files -n liblo10k1-static
#%defattr(644,root,root,755)
#%{_libdir}/liblo10k1.a
