
Summary: A software emulation of the Amiga system
Name: fs-uae
Version: 2.0.1
Release: %mkrel 1 
URL: http://fengestad.no/fs-uae/files/
Source0: %{name}-%{version}.tar.bz2
Source1:  %{name}-game-server-%{version}.py
License: GPL
Group: Emulators
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: X11-devel openal-devel
BuildRequires: SDL-devel glib-devel
BuildRequires: attr-devel 
BuildRequires: gtk+-devel
BuildRequires: gtk+2-devel

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


%build
make 

%install

%makeinstall

cp %{SOURCE1} %{buildroot}/%{_datadir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/fs-uae

%{_docdir}/%{name}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/fs-uae.desktop
%{_datadir}/icons/hicolor/128x128/apps/fs-uae.png
%{_datadir}/icons/hicolor/16x16/apps/fs-uae.png
%{_datadir}/icons/hicolor/256x256/apps/fs-uae.png
%{_datadir}/icons/hicolor/32x32/apps/fs-uae.png
%{_datadir}/icons/hicolor/48x48/apps/fs-uae.png
%{_datadir}/icons/hicolor/64x64/apps/fs-uae.png
%{_datadir}/locale/de/LC_MESSAGES/fs-uae.mo
%{_datadir}/locale/fr/LC_MESSAGES/fs-uae.mo
%{_datadir}/locale/it/LC_MESSAGES/fs-uae.mo
%{_datadir}/locale/pl/LC_MESSAGES/fs-uae.mo
%{_datadir}/locale/sr/LC_MESSAGES/fs-uae.mo
%{_datadir}/locale/nb/LC_MESSAGES/fs-uae.mo

