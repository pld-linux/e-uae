#
# Conditional build:
%bcond_with	capsimage	# use capsimage for .IPF, .RAW and .CTR disk image support

Summary:	Unix Amiga Emulator
Summary(pl.UTF-8):	Uniksowy emulator Amigi
Name:		e-uae
Version:	0.8.29
%define	subver	WIP4
Release:	0.%{subver}.0.1
License:	GPL v2
Group:		Applications/Emulators
Source0:	http://www.rcdrummond.net/uae/e-uae-%{version}-%{subver}/%{name}-%{version}-%{subver}.tar.bz2
# Source0-md5:	cbfd7e3d7a1b323331afbb92ea7ff4f0
Source1:	uae.desktop
Source2:	uae.png
Patch0:		%{name}-format.patch
Patch1:		%{name}-ucontext.patch
Patch2:		%{name}-system-libscg.patch
URL:		http://www.rcdrummond.net/uae/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.55
BuildRequires:	automake >= 1:1.7
BuildRequires:	cdrtools-devel > 2:2.0
BuildRequires:	gtk+2-devel >= 2.0.0
%{?with_capsimage:BuildRequires:	libcapsimage-devel}
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a version of UAE, the Ubiquitous Amiga Emulator, with an
emulation core based on WinUAE 0.8.27. It attempts to bring many of
the great features of WinUAE to non-Windows platforms. This version
now finally has a name, E-UAE, since that's what everybody was calling
it anyway. The 'E' can stand for anything you fancy. Experimental,
extreme, exciting, egalitarian, eggplant, ...

%description -l pl.UTF-8
To jest wersja UAE (Ubiquitous Amiga Emulator - wszędobylskiego
emulatora Amigi) z rdzeniem emulatora opartym na WinUAE 0.8.27. Jest
to próba przeniesienia wielu wspaniałych możliwości WinUAE na
platformy inne niż Windows. Ta wersja ma wreszcie nazwę - E-UAE - jako
że właśnie tak wszyscy ją nazywali. "E" może oznaczać co tylko chcemy.
Eksperymentalny, ekstremalny, ekscytujący, egalitarny...

%package sdl
Summary:	Unix Amiga Emulator, SDL version
Summary(pl.UTF-8):	Uniksowy emulator Amigi, wersja SDL
Group:		Applications/Emulators

%description sdl
This is a version of UAE, the Ubiquitous Amiga Emulator, with an
emulation core based on WinUAE 0.8.27. It attempts to bring many of
the great features of WinUAE to non-Windows platforms. This version
now finally has a name, E-UAE, since that's what everybody was calling
it anyway. The 'E' can stand for anything you fancy. Experimental,
extreme, exciting, egalitarian, eggplant, ...

This version uses SDL as audio and video output.

%description sdl -l pl.UTF-8
To jest wersja UAE (Ubiquitous Amiga Emulator - wszędobylskiego
emulatora Amigi) z rdzeniem emulatora opartym na WinUAE 0.8.27. Jest
to próba przeniesienia wielu wspaniałych możliwości WinUAE na
platformy inne niż Windows. Ta wersja ma wreszcie nazwę - E-UAE - jako
że właśnie tak wszyscy ją nazywali. "E" może oznaczać co tylko chcemy.
Eksperymentalny, ekstremalny, ekscytujący, egalitarny...

Ta wersja używa SDL jako wyjścia dźwięk i obrazu.

%prep
%setup -q -n %{name}-%{version}-%{subver}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
CONFOPTS=`cat` << EOF
	--enable-action-replay
	--enable-aga
	--enable-audio
	--enable-autoconfig
	--enable-bsdsock
	--enable-bsdsock-new
	--enable-cd32
	--enable-cdtv
	--enable-compatible-cpu
	--enable-cycle-exact-cpu
	--enable-enforcer
	--enable-fdi
	--enable-scsi-device
	--enable-threads
	--enable-ui
	--with-caps%{!?with_capsimage:=no}
EOF

%configure \
	$CONFOPTS \
	--disable-dga		\
	--disable-vidmode	\
	--without-alsa		\
	--with-sdl		\
	--with-sdl-gfx		\
	--with-sdl-gl		\
	--with-sdl-sound
%{__make} -j1
%{__mv} src/uae e-uae-sdl
%{__make} clean

%configure \
	$CONFOPTS \
	--enable-dga		\
	--enable-vidmode	\
	--with-alsa		\
	--without-sdl		\
	--without-sdl-gfx	\
	--without-sdl-sound	\
	--with-x
%{__make} -j1
%{__mv} src/uae e-uae

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install e-uae* $RPM_BUILD_ROOT%{_bindir}
sed %{SOURCE1} -e 's/uae/e-uae/' -e 's/UAE/E-UAE/' \
	> $RPM_BUILD_ROOT%{_desktopdir}/e-uae.desktop
sed %{SOURCE1} -e 's/uae/e-uae-sdl/' -e 's/UAE/E-UAE SDL/' \
	> $RPM_BUILD_ROOT%{_desktopdir}/e-uae-sdl.desktop
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/e-uae.png
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/e-uae-sdl.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README docs/*
%attr(755,root,root) %{_bindir}/e-uae
%{_desktopdir}/e-uae.desktop
%{_pixmapsdir}/e-uae.png

%files sdl
%defattr(644,root,root,755)
%doc ChangeLog README docs/*
%attr(755,root,root) %{_bindir}/e-uae-sdl
%{_desktopdir}/e-uae-sdl.desktop
%{_pixmapsdir}/e-uae-sdl.png
