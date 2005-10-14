Summary:	Advanced Linux Sound Architecture (ALSA) - tools
Summary(pl):	Advanced Linux Sound Architecture (ALSA) - narzêdzia
Name:		alsa-tools
Version:	1.0.9
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.alsa-project.org/pub/tools/%{name}-%{version}.tar.bz2
# Source0-md5:	3139b9d6c10e14acbb926f23b488e745
URL:		http://www.alsa-project.org/
BuildRequires:	alsa-lib-devel >= 1.0.3
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	fltk-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	sed >= 4.0
BuildRequires:	qt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# ac3dec skipped - see ac3dec.spec
%define	progs	envy24control hdsploader mixartloader sscape_ctl usx2yloader as10k1 hdspconf rmedigicontrol seq/sbiload us428control vxloader ld10k1
# hdspmixer sb16_csp - FIXME: these do not build

%description
This packages contains command line utilities for the ALSA (Advanced
Linux Sound Architecture) project.

%description -l pl
Pakiet zawiera dzia³aj±ce z linii poleceñ, narzêdzia dla projektu ALSA
(Advanced Linux Sound Architecture).

%prep
%setup -q

%build
for dir in hdsploader hdspconf/src hdspmixer/src sb16_csp sscape_ctl; do
	ln -s %{_includedir} $dir/alsa
done

odir=$(pwd)
for dir in %{progs}; do
	cd $dir
	[ -f README ] && cp -f README "README.$(basename $dir)"
	[ -f NEWS ] && cp -f NEWS "NEWS.$(basename $dir)"
	[ -f TODO ] && cp -f TODO "TODO.$(basename $dir)"
	%{__aclocal}
	%{__autoconf}
	%{__autoheader}
	%{__automake}
	CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
	CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
	%configure
	%{__make}
	cd $odir
done

cd qlo10k1
sed -i s/'include'/'include\/qt'/ acinclude.m4
[ -f README ] && cp -f README README.qlo10k1
[ -f NEWS ] && cp -f NEWS NEWS.qlo10k1
[ -f TODO ] && cp -f TODO TODO.qlo10k1
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

cd $odir/as10k1/examples
%{__make} dsp

%install
rm -rf $RPM_BUILD_ROOT

sed -i s/'#!\/bin\/sh'/'#!\/bin\/bash'/ ld10k1/setup/init_live

odir=$(pwd)
for dir in %{progs} qlo10k1; do
	cd $dir
	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT
	cd $odir
done

install $odir/as10k1/examples/*.emu10k1 $RPM_BUILD_ROOT%{_datadir}/ld10k1/effects

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc */README.* */*/README.* */NEWS.*
# alsamixer/TODO.* 
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/*
%{_datadir}/ld10k1
%{_mandir}/man?/*
%{_sysconfdir}/hotplug/usb/*
%{_desktopdir}/hdspconf.desktop
%{_pixmapsdir}/hdspconf.png
