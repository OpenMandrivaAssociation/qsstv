Name: 		qsstv
Summary: 	Sstv application
Version: 	9.5.7
Release: 	1
License: 	GPLv2
Group: 		Communications
Source0: 	http://users.telenet.be/on4qz/qsstv/downloads/%{name}_%{version}.tar.gz
Source1:        qsstv.png
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	hamlib-devel
BuildRequires:	qt5-devel

%description
qsstv is an sstv app.
You can send and receive images sent over radio using your soundcard.

%prep
%setup -q -n qsstv_%{version}
    sed -i -e "s:/doc/\$\$TARGET:/doc/qsstv:" \
        -e "s:/usr/local/bin:%{buildroot}/usr/bin:" \
        -e "s:/usr/share/doc:%{buildroot}/usr/share/doc:" \
        -e "s:target.extra:#target.extra:" \
        -e "s:-lhamlib:-L%{_libdir}/hamlib -lhamlib:g" src/src.pro
    sed -i -e "s:doc/qsstv:doc/qsstv:" src/configdialog.cpp

%patch0 -p0

%build
%qmake
%make

%install
%makeinstall_std
%files
%{_bindir}/*
%{_datadir}/doc/%{name}/*
