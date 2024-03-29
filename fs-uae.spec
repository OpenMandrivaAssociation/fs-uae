Summary:	A software emulation of the Amiga system
Name:		fs-uae
Version:	3.1.66
Release:	1
License:	GPLv2
Group:		Emulators
URL:		https://fs-uae.net
Source0:	https://fs-uae.net/files/FS-UAE/Stable/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	gettext
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libmpeg2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	zip

%description
UAE is a software emulation of the Amiga system hardware, which
enables you to run most available Amiga software.  Since it is a
software emulation, no extra or special hardware is needed.  The Amiga
hardware is emulated accurately, so that Amiga software is tricked
into thinking it is running on the real thing.  Your computer's
display, keyboard, hard disk and mouse assume the roles of their
emulated counterparts.

Note that to fully emulate the Amiga you need the Amiga KickStart ROM
images, which are copyrighted and, of course, not included here.

[This is in an unofficial branch of UAE (the Ubiquitous Amiga Emulator)
with the aim of bringing the features of WinUAE to non-Windows platforms
such as Linux, Mac OS X and BeOS.]

%prep
%setup -q
export CC=gcc
export CXX=g++
%configure

%build
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/fs-uae
%{_bindir}/fs-uae-device-helper
%{_docdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/mime/packages/fs-uae.xml
%{_datadir}/applications/fs-uae.desktop
%{_datadir}/icons/hicolor/*/apps/fs-uae.png

