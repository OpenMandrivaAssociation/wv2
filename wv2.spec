
%define lib_name_orig %mklibname wv2
%define lib_major 1
%define lib_name %{lib_name_orig}_%{lib_major}



Summary:	Word97 exporter library
Name:		wv2
Version:	0.2.2
Release:	%mkrel 6
License:	GPL
Group:		Office
URL:		http://sourceforge.net/projects/wvware/
Source: 	wv2-%version.tar.bz2
BuildRequires:	XFree86-devel
BuildRequires:	libgsf-devel
BuildRequires:	autoconf2.5
BuildRoot:	%{_tmppath}/%{name}-buildroot
Patch1:		wv2-security-fix.patch.bz2

%description
wvWare is the continuation of Caolan McNamara's wv - the MSWord library.
Efforts are underway to make this library more correct, robust,
and turn it into a Word97 exporter.

%package -n %lib_name
Summary: 	Word97 exporter library
Group:	 	Development/C
Obsoletes:	wv2
Provides:	wv2 = %version-%release
Provides:	%lib_name_orig = %version-%release



%description -n %lib_name
wvWare is the continuation of Caolan McNamara's wv - the MSWord library. 
Efforts are underway to make this library more correct, robust, 
and turn it into a Word97 exporter.

%package -n %lib_name-devel
Summary: 	Word97 exporter library devel
Group:	 	Development/C
Requires: 	%{name} = %{version}
Requires:	%lib_name = %version-%release

Obsoletes:	wv2-devel
Provides:	wv2-devel = %version-%release


%description -n %lib_name-devel
This is the Wv2 development package.

%prep
%setup -q
%patch1 -p1 -b .fix_security
%build
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/wv2-config


%post -n %lib_name -p /sbin/ldconfig
%postun -n %lib_name -p /sbin/ldconfig

%post -n %lib_name-devel -p /sbin/ldconfig
%postun -n %lib_name-devel -p /sbin/ldconfig


%clean
rm -rf $RPM_BUILD_ROOT

%files -n %lib_name
%defattr(-,root,root)
%_libdir/*.la
%_libdir/*.so.*


%files -n %lib_name-devel
%defattr(-,root,root)
%dir %_includedir/wv2
%_includedir/wv2/*.h

%_libdir/*.so

%_bindir/wv2-config
%multiarch %{multiarch_bindir}/wv2-config
