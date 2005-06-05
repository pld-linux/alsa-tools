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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# ac3dec skipped - see ac3dec.spec
%define	progs	envy24control hdsploader mixartloader sscape_ctl usx2yloader as10k1 hdspconf rmedigicontrol seq/sbiload us428control vxloader
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

%install
rm -rf $RPM_BUILD_ROOT

odir=$(pwd)
for dir in %{progs}; do
	cd $dir
	%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT
	cd $odir
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc */README.* */*/README.* */NEWS.*
# alsamixer/TODO.* 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_sysconfdir}/hotplug/usb/*
%{_desktopdir}/hdspconf.desktop
%{_pixmapsdir}/hdspconf.png
