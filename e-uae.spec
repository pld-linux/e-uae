Summary:	Unix Amiga Emulator
Summary(pl):	Uniksowy Emulator Amigi
Name:		e-uae
Version:	0.8.27
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://www.rcdrummond.net/uae/e-uae-%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	a5ccafd3d8e74f733293a1beccbf9487
URL:		http://www.rcdrummond.net/uae/
BuildRequires:	gtk+2-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_sound-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a version of UAE, the Ubiquitous Amiga Emulator, with an
emulation core based on WinUAE 0.8.27. It attempts to bring many of
the great features of WinUAE to non-Windows platforms. This version
now finally has a name, E-UAE, since that's what everybody was calling
it anyway. The 'E' can stand for anything you fancy. Experimental,
extreme, exciting, egalitarian, eggplant, ...

%prep
%setup -q

%build
%configure \
	--with-sdl \
	--with-sdl-sound \
	--with-sdl-gfx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/uae $RPM_BUILD_ROOT%{_bindir}/e-uae

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README docs/*
%attr(755,root,root) %{_bindir}/%{name}
