
Summary: A software emulation of the Amiga system
Name: fs-uae
Version: 0.9.7
Release: %mkrel 1
URL: http://sourceforge.net/projects/uaedev/
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Emulators
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: X11-devel openal-devel
BuildRequires: SDL-devel glib-devel
BuildRequires: attr-devel 
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


%build
make 

%install

%makeinstall
%ifarch x86_64
mkdir -p %{buildroot}/%{_libdir}/fs-uae
cp -Rf %{buildroot}/usr/lib/fs-uae/libcapsimage.so %{buildroot}/%{_libdir}/fs-uae/libcapsimage.so
rm -f  %{buildroot}/usr/lib/fs-uae/libcapsimage.so
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%{_docdir}/%{name}/*
%{_datadir}/%{name}/*

