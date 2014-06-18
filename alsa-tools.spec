#
# Conditional build:
%bcond_with	hotplug		# build with hotplug support for Tascam USB devices
#
Summary:	Advanced Linux Sound Architecture (ALSA) - tools
Summary(pl.UTF-8):	Advanced Linux Sound Architecture (ALSA) - narzędzia
Name:		alsa-tools
Version:	1.0.28
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	ftp://ftp.alsa-project.org/pub/tools/%{name}-%{version}.tar.bz2
# Source0-md5:	e6c929175d8ee729c06d49b51439bad6
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-sh.patch
Patch2:		%{name}-csp.patch
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= 1.0.24
BuildRequires:	autoconf
BuildRequires:	automake >= 1.3
BuildRequires:	fltk-devel
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	qt-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
Requires:	alsa-lib >= 1.0.24
# for lo10k1, qlo10k1
Requires:	liblo10k1 = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# qlo10k1 has separate make rule
%define	progs	as10k1 echomixer envy24control hda-verb hdajackretask hdspconf hdsploader hdspmixer hwmixvolume ld10k1 mixartloader pcxhrloader rmedigicontrol sb16_csp seq/sbiload sscape_ctl us428control usx2yloader vxloader

%description
This packages contains command line utilities for the ALSA (Advanced
Linux Sound Architecture) project.

%description -l pl.UTF-8
Pakiet zawiera działające z linii poleceń narzędzia dla projektu ALSA
(Advanced Linux Sound Architecture).

%package gui-echoaudio
Summary:	GTK+ GUI to control Echoaudio soundcard
Summary(pl.UTF-8):	Graficzny interfejs GTK+ do sterowania kartami dźwiękowymi Echoaudio
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description gui-echoaudio
This package contains Echomixer - GTK+ GUI tool to control all the
features of any Echoaudio soundcard. This includes clock sources,
input and output gains, mixers etc.

%description gui-echoaudio -l pl.UTF-8
Ten pakiet zawiera aplikację Echomixer - oparte na GTK+ graficzne
narzędzie do sterowania wszystkimi ustawieniami kart dźwiękowych
Echoaudio. Obejmuje to źródła zegara, wzmacniacze wejściowe i
wyjściowe, miksery itp.

%package gui-emu10k1
Summary:	Qt GUI to load Emu10k1 patches
Summary(pl.UTF-8):	Graficzny interfejs Qt do ładowania próbek Emu10k1
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description gui-emu10k1
This package contains qlo10k1 - Qt GUI for ld10k1, ALSA patch loader
for Emu10k1 based soundcards (SB Live! and Audigy).

%description gui-emu10k1 -l pl.UTF-8
Ten pakiet zawiera aplikację qlo10k1, będącą opartym na Qt graficznym
interfejsem dla ld10k1 - programu służącego do wczytywania próbek
dźwiękowych ALSA dla kart opartych na układzie Emu10k1 (SB Live! i
Audigy).

%package gui-envy24
Summary:	GTK+ GUI to control Envy24 (ice1712) based soundcards
Summary(pl.UTF-8):	Graficzny interfejs GTK+ do sterowania kartami dźwiękowymi Envy24
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description gui-envy24
This package contains envy24control - GTK+ GUI tool to control Envy24
(ice1712) based soundcards.

%description gui-envy24 -l pl.UTF-8
Ten pakiet zawiera aplikację envy24control - graficzny interfejs GTK+
do sterowania ustawieniami kart dźwiękowych opartych na układzie
Envy24 (ice1712).

%package gui-hda
Summary:	GTK+ GUI for HDA Intel soundcards
Summary(pl.UTF-8):	Graficzny interfejs GTK+ do sterowania kartami HDA Intel
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description gui-hda
This package contains hdajackretask - a GUI to make it easy to retask
HDA Intel jacks.

%description gui-hda -l pl.UTF-8
Ten pakiet zawiera aplikację hdajackretask - graficzny interfejs
ułatwiający zmianę funkcji gniazd (typu jack) karty HDA Intel.

%package gui-hdsp
Summary:	FLTK GUIs to control RME Hammerfall HDSP soundcards
Summary(pl.UTF-8):	Graficzne interfejsy FLTK do sterowania kartami dźwiękowymi RME Hammerfall HDSP
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description gui-hdsp
This package contains two FLTK-based GUI utilities for RME Hammerfall
DSP soundcards:
- HDSPConf to control ALSA settings
- HDSPMixer to control advanced routing feaures.

%description gui-hdsp -l pl.UTF-8
Ten pakiet zawiera dwa narzędzia z opartym na FLTK graficznym
interfejsem użytkownika, przeznaczone dla kart RME Hammerfall DSP:
- HDSPConf do sterowania ustawieniami systemu ALSA
- HDSPMixer do sterowania zaawansowanymi ustawieniami tras sygnału.

%package gui-hwmix
Summary:	PyGTK GUI to control volume of individual streams when using hardware mixing
Summary(pl.UTF-8):	Graficzny interfejs PyGTK do ustawiania głośności strumieni przy sprzętowym miksowaniu
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}
Requires:	python-pyalsa >= 1.0.22
Requires:	python-pygtk-gtk >= 2:2.0

%description gui-hwmix
This package contains hwmixvolume - PyGTK-based GUI to control the
volume of individual streams on soundcards that use hardware mixing,
i.e. those based on the following chips:
- Creative Emu10k1 (SoundBlaster Live!) (driver: snd-emu10k1)
- VIA VT823x southbridge (driver: snd-via82xx)
- Yamaha DS-1 (YMF-724/740/744/754) (driver: snd-ymfpci)

%description gui-hwmix -l pl.UTF-8
Ten pakiet zawiera aplikację hwmixvolume - oparty na PyGTK graficzny
interfejs do sterowania głośnością poszczególnych strumieni w kartach
dźwiękowych korzystających ze sprzętowego miksowania - czyli opartych
na następujących układach:
- Creative Emu10k1 (SoundBlaster Live!) (sterownik: snd-emu10k1)
- mostku VIA VT823x (sterownik: snd-via82xx)
- Yamaha DS-1 (YMF-724/740/744/754) (sterownik: snd-ymfpci)

%package gui-rmedigi
Summary:	GTK+ GUI to control RME Digi32/Digi96 soundcards
Summary(pl.UTF-8):	Graficzny interfejs GTK+ do sterowania kartami dźwiękowymi RME Digi32/Digi96
Group:		X11/Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description gui-rmedigi
This package contains rmedigicontrol - GTK+ GUI control tool for RME
Digi32 and RME Digi96 soundcards.

%description gui-rmedigi -l pl.UTF-8
Ten pakiet zawiera aplikację rmedigicontrol - oparty na GTK+ graficzny
interfejs do sterowania ustawieniami kart dźwiękowych RME Digi32 i RME
Digi96.

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

sed -i -e 's,/usr/bin/env python,/usr/bin/python,' hwmixvolume/hwmixvolume

install -d doc-main doc-sep

%build
odir=$(pwd)
for dir in %{progs}; do
	cd $dir
	[ -s AUTHORS ] && cp -f AUTHORS $odir/doc-main/"AUTHORS.$(basename $dir)"
	[ -s README ] && cp -f README $odir/doc-main/"README.$(basename $dir)"
	[ -s NEWS ] && cp -f NEWS $odir/doc-main/"NEWS.$(basename $dir)"
	[ -s TODO ] && cp -f TODO $odir/doc-main/"TODO.$(basename $dir)"
	%{__libtoolize}
	%{__aclocal}
	%{__autoconf}
	grep -q 'A[CM]_CONFIG_HEADER' configure.* && %{__autoheader}
	%{__automake}
	%configure \
		`[ "$dir" != ld10k1 ] || echo --enable-static ]`
	%{__make}
	cd $odir
done
mv doc-main/AUTHORS.hdajackretask doc-sep
mv doc-main/NEWS.{hdajackretask,hdspmixer,rmedigicontrol} doc-sep
mv doc-main/README.{echomixer,envy24control,hdajackretask,hdspconf,hdspmixer,hwmixvolume,rmedigicontrol} doc-sep
mv doc-main/TODO.hdspmixer doc-sep

cd qlo10k1
sed -i 's:include:include/qt:g' acinclude.m4
cp -f README $odir/doc-sep/README.qlo10k1
cp -f NEWS $odir/doc-sep/NEWS.qlo10k1
cp -f TODO $odir/doc-sep/TODO.qlo10k1
%{__libtoolize}
%{__aclocal} -I ../ld10k1
%{__autoconf}
%{__autoheader}
%{__automake}
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

for dir in %{progs} qlo10k1; do
	%{__make} -C $dir install \
		DESTDIR=$RPM_BUILD_ROOT
done

install as10k1/examples/*.emu10k1 $RPM_BUILD_ROOT%{_datadir}/ld10k1/effects

%if %{without hotplug}
%{__rm} -r $RPM_BUILD_ROOT%{_sysconfdir}/hotplug
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n liblo10k1 -p /sbin/ldconfig
%postun	-n liblo10k1 -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc-main/{README,NEWS,TODO}.*
%attr(755,root,root) %{_bindir}/as10k1
%attr(755,root,root) %{_bindir}/cspctl
%attr(755,root,root) %{_bindir}/hda-verb
%attr(755,root,root) %{_bindir}/hdsploader
%attr(755,root,root) %{_bindir}/init_audigy
%attr(755,root,root) %{_bindir}/init_audigy_eq10
%attr(755,root,root) %{_bindir}/init_live
%attr(755,root,root) %{_bindir}/lo10k1
%attr(755,root,root) %{_bindir}/mixartloader
%attr(755,root,root) %{_bindir}/pcxhrloader
%attr(755,root,root) %{_bindir}/sbiload
%attr(755,root,root) %{_bindir}/sscape_ctl
%attr(755,root,root) %{_bindir}/us428control
%attr(755,root,root) %{_bindir}/usx2yloader
%attr(755,root,root) %{_bindir}/vxloader
%attr(755,root,root) %{_sbindir}/dl10k1
%attr(755,root,root) %{_sbindir}/ld10k1
%attr(755,root,root) %{_sbindir}/ld10k1d
%{_datadir}/ld10k1
%{_mandir}/man1/cspctl.1*
# for sbiload
%{_datadir}/sounds/opl3

%files gui-echoaudio
%defattr(644,root,root,755)
%doc doc-sep/README.echomixer
%attr(755,root,root) %{_bindir}/echomixer

%files gui-emu10k1
%defattr(644,root,root,755)
%doc doc-sep/{README,NEWS,TODO}.qlo10k1
%attr(755,root,root) %{_bindir}/qlo10k1

%files gui-envy24
%defattr(644,root,root,755)
%doc doc-sep/README.envy24control envy24control/README.profiles
%attr(755,root,root) %{_bindir}/envy24control
%{_mandir}/man1/envy24control.1*

%files gui-hda
%defattr(644,root,root,755)
%doc doc-sep/{AUTHORS,NEWS,README}.hdajackretask
%attr(755,root,root) %{_bindir}/hdajackretask

%files gui-hdsp
%defattr(644,root,root,755)
%doc doc-sep/README.hdspconf doc-sep/{NEWS,README,TODO}.hdspmixer
%attr(755,root,root) %{_bindir}/hdspconf
%attr(755,root,root) %{_bindir}/hdspmixer
%{_desktopdir}/hdspconf.desktop
%{_desktopdir}/hdspmixer.desktop
%{_pixmapsdir}/hdspconf.png
%{_pixmapsdir}/hdspmixer.png

%files gui-hwmix
%defattr(644,root,root,755)
%doc doc-sep/README.hwmixvolume
%attr(755,root,root) %{_bindir}/hwmixvolume

%files gui-rmedigi
%defattr(644,root,root,755)
%doc doc-sep/{NEWS,README}.rmedigicontrol
%attr(755,root,root) %{_bindir}/rmedigicontrol

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

%files -n liblo10k1-static
%defattr(644,root,root,755)
%{_libdir}/liblo10k1.a
