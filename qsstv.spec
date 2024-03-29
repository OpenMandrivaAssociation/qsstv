%define _empty_manifest_terminate_build 0

Name: 		qsstv
Summary: 	Qt-based slow-scan TV, radio and fax, sstv
Version: 	9.5.8
Release: 	1
License: 	GPLv2
Group: 		Communications
Source0: 	http://users.telenet.be/on4qz/qsstv/downloads/%{name}_%{version}.tar.gz
Source1:        qsstv.desktop
Source2:        qsstv.1
BuildRequires:	pkgconfig(fftw3)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libv4lconvert)
BuildRequires:	hamlib-devel
BuildRequires:	qt5-devel

%description
Qsstv is a program for receiving slow-scan television and fax. 
These are modes used by hamradio operators. Qsstv uses a soundcard to send and receive images.

%prep
%setup -q -n qsstv

%build
%qmake_qt5 PREFIX=/usr
%make_build

%install
export INSTALL_ROOT=%{buildroot}
%make_install

# Install icon
mkdir -p %{buildroot}%{_iconsdir}
cp -f icons/qsstv.png %{buildroot}%{_iconsdir}/qsstv.png

desktop-file-install \
        --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

# Install man page borrowed from Debian
mkdir -p %{buildroot}%{_mandir}/man1
install -pm 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/

%files
%{_bindir}/*
%{_datadir}/applications/qsstv.desktop
%{_datadir}/icons/qsstv.png
%{_mandir}/man1/qsstv.1.*
