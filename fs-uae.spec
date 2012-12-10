
Summary: A software emulation of the Amiga system
Name: fs-uae
Version: 1.3.27
Release: %mkrel 2 
URL: http://fengestad.no/fs-uae/files/
Source0: %{name}-%{version}.tar.bz2
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
%ifarch x86_64
mkdir -p %{buildroot}/%{_libdir}/fs-uae
# cp -Rf %{buildroot}/usr/lib/fs-uae/libcapsimage.so %{buildroot}/%{_libdir}/fs-uae/libcapsimage.so
# rm -f  %{buildroot}/usr/lib/fs-uae/libcapsimage.so
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/fs-uae
# %{_libdir}/fs-uae/libcapsimage.so
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



%changelog
* Mon Sep 24 2012 Zombie Ryushu <ryushu@mandriva.org> 1.3.27-2mdv2012.0
+ Revision: 817491
- remove libcapsimage
- Upgrade to 1.3.27
- Upgrade to 1.3.27
- Upgrade to 1.3.27

* Sat Sep 15 2012 Zombie Ryushu <ryushu@mandriva.org> 1.3.26u1-1
+ Revision: 816968
- Upgrade to 1.3.26u1
- Upgrade to 1.3.23
- Upgrade to 1.3.22
- Upgrade to 1.3.15
- Update to 1.3.14
- Upgrade to 1.3.9
- fix locale
- libcapsimage deprecated?
- libcapsimage deprecated?
- Upgrade to 1.3.7
- package icon and desktop shortcut
- Upgrade to version 1.2.0 stable
- Upgrade to 1.1.9
- Update to 1.1.5
- Upgrade to 1.1.4
- Upgrade to 1.1.1
- Upgrade to 1.1.1
- Upgrade to 1.1.0
- Upgrade to 1.1.0
- Upgrade to version 1.0.2
- Upgrade to 1.0.0rc5 and correct URL
- Upgrade to 0.9.13beta
- Upgrade to 0.9.12
- Remove Obsoletes
- Upgrade to 0.9.10
- Upgrade to 0.9.8
- Upgrade to 0.9.7
- Upgrade to 0.9.5
- Makefile patch
- Add glib dep
- Add glib dep
- correct libs
- imported package fs-uae


* Fri Jan 27 2012 codebase7 <codebase7@yahoo.com> 0.8.29-2.WIP4.1mdv2011.0
- Add wahcade patch for Zombie Ryushu.
- Fix string format bugs.

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.29-1.WIP4.1mdv2009.1
+ Revision: 311430
- fix spec file again...
- spec file cleanup

  + Zombie Ryushu <ryushu@mandriva.org>
    - Disable fucomi patch which is obsolete here
    - Fix Macros
    - Version bump
    - Version bump

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.8.29-1.WIP3.4mdv2009.0
+ Revision: 244983
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.8.29-1.WIP3.2mdv2008.1
+ Revision: 136407
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel


* Mon Mar 19 2007 Giuseppe GhibÃ² <ghibo@mandriva.com> 0.8.29-1.WIP3.2mdv2007.1
+ Revision: 146623
- Added attr-devel, gtk+2-devel to BuildRequires.
- Rebuilt.
- Import e-uae

* Sun Sep 03 2006 Giuseppe Ghibò <ghibo@mandriva.com> 0.8.29-1.WIP3.1mdv2007.0
- Release 0.8.29-WIP3.

* Sun Feb 19 2006 Giuseppe Ghibò <ghibo@mandriva.com> 0.8.28-2.cvs20060219.1mdk
- cvs 20060219.

* Fri Oct 21 2005 Giuseppe Ghibò <ghibo@mandriva.com> 0.8.28-1mdk
- 0.8.28 final.

* Wed Sep 07 2005 Giuseppe Ghibò <ghibo@mandriva.com> 0.8.28-0.rc2.4mdk
- use -Wa,--execstack instead of execstack -s from prelink (Gwenole).

* Tue Sep 06 2005 Giuseppe Ghibò <ghibo@mandriva.com> 0.8.28-0.rc2.3mdk
- cvs 20050905.
- make binary executable stack, otherwise segfaults on A64.

* Fri Aug 26 2005 Giuseppe Ghibò <ghibo@mandriva.com> 0.8.28-0.rc2.2mdk
- Updated to final 0.8.28-RC2.

* Wed Aug 17 2005 Giuseppe Ghibò <ghibo@mandriva.com> 0.8.28-0.rc2.1mdk
- Relase 0.8.28rc2.

* Sat Jan 08 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.8.27-2mdk
- Added Provides.

* Sat Jan 08 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.8.27-1mdk
- Release 0.8.27.
- Readapted fucomi patch.

* Mon Dec 06 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.8.27-0.20041204.1mdk
- Updated to CVS 20041205.

* Thu Sep 02 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.8.27-0.20040831.1mdk
- Initial release based on uae spec file.
- Disabled fucomi patch (needs to be rebuilt for new sources).

