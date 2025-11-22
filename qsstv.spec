%global debug_package %{nil}
%define _empty_manifest_terminate_build 0
# NOTE upstream  have not made a release tarball, run package-source.sh to create
# NOTE an archive out of the latest git master branch and adjust the
# NOTE sourcedate parameter to match it
%define sourcedate 20251120

Name:		qsstv
URL:		https://github.com/ON4QZ/QSSTV
Summary:	Qt6-based slow-scan TV, radio and fax, sstv
Version:	9.5.11.%{sourcedate}
Release:	1
License:	GPL-3.0-only
Group:		Communications
Source0:	qsstv-%{sourcedate}.tar.zst
Source1:	qsstv.desktop
Source2:        qsstv.1
# Fix broken DRM decode for Qt6
Patch0:		https://github.com/ON4QZ/QSSTV/pull/67/commits/659ef0c02068d76d82622875e413aa362407b677.patch#/fix-broken-drm-decode-for-qt6.patch

BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(hamlib)
BuildRequires:	pkgconfig(libpulse-simple)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libopenjp2)
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	pkgconfig(libv4lconvert)
BuildRequires:	pkgconfig(Qt6Concurrent)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Help)
BuildRequires:	pkgconfig(Qt6Multimedia)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6OpenGLWidgets)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Qml)
BuildRequires:	pkgconfig(Qt6QmlModels)
BuildRequires:	pkgconfig(Qt6Quick)
BuildRequires:	pkgconfig(Qt6SerialPort)
BuildRequires:	pkgconfig(Qt6Sql)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6UiTools)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6UiPlugin)
#qt6-qttools-devel
BuildRequires:	pkgconfig(Qt6Xml)

%description
Qsstv is a program for receiving slow-scan television and fax. 
These are modes used by hamradio operators. Qsstv uses a soundcard to send and receive images.

%prep
%autosetup -n qsstv-%{sourcedate} -p1
mkdir src/build

%build
cd src/build
qmake-qt6 .. PREFIX=%{buildroot}%{_prefix}
%make_build

%install
cd src/build
export INSTALL_DIR=%{buildroot}
%make_install

cd ..
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
