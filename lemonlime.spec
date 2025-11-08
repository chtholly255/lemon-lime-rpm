Name: lemon-lime
Version: 0.3.6.1
Release: %autorelease
Summary: A tiny judging environment for OI contest based on Lemon + LemonPlus
License: GPLv3
URL: https://github.com/Project-LemonLime/Project_LemonLime
Source0: https://github.com/Project-LemonLime/Project_LemonLime/releases/download/%{version}/Lemon-%{version}-source-all.7z

BuildRequires:  p7zip
BuildRequires:  cmake
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ninja-build
BuildRequires:  xcb-util-cursor

%description
A tiny judging environment for OI contest based on Lemon + LemonPlus

%prep
# %setup -c Lemon-%{version}-source-all
# cd %{_builddir}/%{name}-%{version}
%autosetup -c Lemon-%{version}-source-all

%build
export _LEMON_BUILD_INFO_="LemonLime built by Fedora COPR (Unofficial)"
export _LEMON_BUILD_EXTRA_INFO_="$(uname -a | cut -d ' ' -f3,13), Qt $(pkg-config --modversion Qt6Core)"
%cmake -DBUILD_SHARED_LIBS=OFF
# BUILD_SHARED_LIBS=OFF for sdplog
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/lemon
%{_datadir}/applications/lemon-lime.desktop
%{_datadir}/icons/hicolor
%{_datadir}/metainfo/lemon-lime.metainfo.xml
%{_datadir}/mime/application/x-lemon-contest.xml
%{_includedir}/testlib_for_lemons.h
