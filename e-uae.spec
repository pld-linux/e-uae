Summary:	Unix Amiga Emulator
Summary(pl.UTF-8):   Uniksowy emulator Amigi
Name:		e-uae
Version:	0.8.29
%define	_wip	WIP3
Release:	0.%{_wip}.0.1
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.rcdrummond.net/uae/e-uae-%{version}-%{_wip}/%{name}-%{version}-%{_wip}.tar.bz2
# Source0-md5:	cae34d41eaef0336d5182155fd194deb
Source1:	uae.desktop
Source2:	uae.png
URL:		http://www.rcdrummond.net/uae/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	automake
BuildRequires:	cdrtools-devel > 2:2.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
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
Summary(pl.UTF-8):   Uniksowy emulator Amigi, wersja SDL
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

Ta wersja używa SDL jako wyjścia audio i wideo.

%prep
%setup -q -n %{name}-%{version}-%{_wip}

%build
cp -f /usr/share/automake/config.* .
CONFOPTS=`cat` << EOF
	--enable-aga
	--enable-cdtv
	--enable-cd32
	--enable-cycle-exact-cpu
	--enable-compatible-cpu
	--enable-threads
	--enable-autoconfig
	--enable-scsi-device
	--enable-bsdsock
	--enable-bsdsock-new
	--enable-enforcer
	--enable-action-replay
	--enable-ui
	--enable-audio
	--enable-fdi
	--without-caps
	--with-libscg-includedir=%{_includedir}/schily
	--with-libscg-libdir=%{_libdir}
EOF

%configure \
	$CONFOPTS \
	--disable-dga		\
	--disable-vidmode	\
	--without-alsa		\
	--with-sdl		\
	--with-sdl-sound	\
	--with-sdl-gfx
%{__make}
mv src/uae e-uae-sdl
%{__make} clean

%configure \
	$CONFOPTS \
	--enable-dga		\
	--enable-vidmode	\
	--with-alsa		\
	--with-x		\
	--without-sdl		\
	--without-sdl-sound	\
	--without-sdl-gfx
%{__make}
mv src/uae e-uae

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install e-uae* $RPM_BUILD_ROOT%{_bindir}/
sed %{SOURCE1} -e 's/uae/e-uae/' -e 's/UAE/E-UAE/' \
	> $RPM_BUILD_ROOT%{_desktopdir}/e-uae.desktop
sed %{SOURCE1} -e 's/uae/e-uae-sdl/' -e 's/UAE/E-UAE SDL/' \
	> $RPM_BUILD_ROOT%{_desktopdir}/e-uae-sdl.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/e-uae.png
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/e-uae-sdl.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README docs/*
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/e-uae.desktop
%{_pixmapsdir}/e-uae.png

%files sdl
%defattr(644,root,root,755)
%doc ChangeLog README docs/*
%attr(755,root,root) %{_bindir}/%{name}-sdl
%{_desktopdir}/e-uae-sdl.desktop
%{_pixmapsdir}/e-uae-sdl.png
