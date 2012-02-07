%define cdrname		cdrtools
%define cdrmainvers	2.01
%define cdrvers 	%{cdrmainvers}a38
%define wiprel		WIP4

# For building with SCSI support
%define build_scsi 1
%{?_with_scsi: %global build_scsi 1}
%{?_without_scsi: %global build_scsi 0}

Summary: A software emulation of the Amiga system
Name: fs-uae
Version: 0.9.2
Release: %mkrel 1
URL: http://sourceforge.net/projects/uaedev/
Source0: %{name}-%{version}.tar.bz2
Source1: ftp://ftp.berlios.de/pub/cdrecord/alpha/%{cdrname}-%{cdrvers}.tar.bz2
Patch0:	fs-uae-Makefile.patch
License: GPL
Group: Emulators
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: X11-devel
BuildRequires: SDL-devel glib-devel
BuildRequires: attr-devel glib2.0-devel
BuildRequires: gtk+-devel
BuildRequires: gtk+2-devel

Conflicts: uae
Obsoletes: uaedev
Provides: uaedev

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
%patch0 -p0

%build
make 

%install

%makeinstall


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs/*
%{_bindir}/*
%{_libdir}/uae
%doc docs/*




