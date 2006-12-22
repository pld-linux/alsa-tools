# TODO: make description true (i.e. separate GUIs)
# echomixer,envy24control,rmedigicontrol use GTK+ 2
# hdspconf,hdspmixer use FLTK
# qlo10k1 uses Qt 3
# 
Summary:	Advanced Linux Sound Architecture (ALSA) - tools
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - narzêdzia
Name:		alsa-tools
Version:	1.0.13
Release:	2
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.alsa-project.org/pub/tools/%{name}-%{version}.tar.bz2
# Source0-md5:	3f30a884848a21910195a3c77f1dbde2
Patch0:		%{name}-asneeded.patch
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

%description -l pl
Pakiet zawiera dzia³aj±ce z linii poleceñ narzêdzia dla projektu ALSA
(Advanced Linux Sound Architecture).

%package tascam
Summary:	Hotplug support for Tascam USB devices
Summary(pl):	Wsparcie hotpluga do urz±dzeñ USB Tascam
Group:		Applications/Sound
Requires:	udev

%description tascam
Hotplug support for Tascam USB devices, firmware loader.

%description tascam -l pl
Wsparcie hotpluga do urz±dzeñ USB Tascam, narzêdzie do ³adowania
firmware'u.

%package -n liblo10k1
Summary:	liblo10k1 library
Summary(pl):	Biblioteka liblo10k1
Group:		Libraries
Conflicts:	alsa-tools < 1.0.13

%description -n liblo10k1
liblo10k1 library.

%description -n liblo10k1 -l pl
Biblioteka liblo10k1.

%package -n liblo10k1-devel
Summary:	Header files for liblo10k1 library
Summary(pl):	Pliki nag³ówkowe biblioteki liblo10k1
Group:		Development/Libraries
Requires:	liblo10k1 = %{version}-%{release}

%description -n liblo10k1-devel
Header files for liblo10k1 library.

%description -n liblo10k1-devel -l pl
Pliki nag³ówkowe biblioteki liblo10k1.

%package -n liblo10k1-static
Summary:	Static liblo10k1 library
Summary(pl):	Statyczna biblioteka liblo10k1
Group:		Development/Libraries
Requires:	liblo10k1-devel = %{version}-%{release}

%description -n liblo10k1-static
Static liblo10k1 library.

%description -n liblo10k1-static -l pl
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
	[ -f ltmain.sh ] && %{__libtoolize}
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
%if "%{_lib}" == "lib64"
sed -i 's:QTDIR/lib:QTDIR/lib64:g' acinclude.m4
%endif
cp -f README README.qlo10k1
cp -f NEWS NEWS.qlo10k1
cp -f TODO TODO.qlo10k1
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n liblo10k1 -p /sbin/ldconfig
%postun	-n liblo10k1 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc */README.* */*/README.* */NEWS.*
# alsamixer/TODO.* 
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_datadir}/ld10k1
%{_mandir}/man?/*
%{_desktopdir}/hdspconf.desktop
%{_desktopdir}/hdspmixer.desktop
%{_pixmapsdir}/hdspconf.png
%{_pixmapsdir}/hdspmixer.png
# for sbiload
%{_datadir}/sounds/opl3

%files tascam
%defattr(644,root,root,755)
%attr(755,root,root) %{_sysconfdir}/hotplug/usb/tascam_fpga
%attr(755,root,root) %{_sysconfdir}/hotplug/usb/tascam_fw
%{_sysconfdir}/hotplug/usb/tascam_fw.usermap

%files -n liblo10k1
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblo10k1.so.*.*.*

%files -n liblo10k1-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblo10k1.so
%{_libdir}/liblo10k1.la
%{_includedir}/lo10k1
%{_aclocaldir}/ld10k1.m4

#%files -n liblo10k1-static
#%defattr(644,root,root,755)
#%{_libdir}/liblo10k1.a
