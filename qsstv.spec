Name: 		qsstv
Summary: 	Sstv application
Version: 	9.5.7
Release: 	1
License: 	GPLv2
Group: 		Communications
Source0: 	http://users.telenet.be/on4qz/qsstv/downloads/%{name}_%{version}.tar.gz
Source1:        qsstv.png
BuildRequires:	pkgconfig(fftw3)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:	hamlib-devel
BuildRequires:	qt5-devel

%description
qsstv is an sstv app.
You can send and receive images sent over radio using your soundcard.

%prep
%setup -q -n qsstv

%build
%qmake_qt5 PREFIX=/usr
%make_build

%install
%make_install

%files
%{_bindir}/*
%{_datadir}/doc/%{name}/*
