%define name	wv2
%define version	0.4.2

%define major		4
%define libname		%mklibname %{name}_ %major
%define develname	%mklibname %{name} -d

Summary:	Word97 exporter library
Name:		%{name}
Version:	%{version}
Release:	%mkrel 3
License:	LGPLv2
Group:		Office
URL:		http://sourceforge.net/projects/wvware/
Source0: 	http://downloads.sourceforge.net/wvware/%{name}-%{version}.tar.bz2
Patch3:		wv2-0.4.2-linkage.patch
BuildRequires:	libgsf-devel
BuildRequires:  cmake
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
wvWare is the continuation of Caolan McNamara's wv - the MSWord library.
Efforts are underway to make this library more correct, robust,
and turn it into a Word97 exporter.

%package -n %libname
Summary: 	Word97 exporter library
Group:	 	Development/C
Obsoletes:	wv2
Provides:	%{name} = %version-%release
Provides:	lib%{name} = %version-%release

%description -n %libname
wvWare is the continuation of Caolan McNamara's wv - the MSWord library. 
Efforts are underway to make this library more correct, robust, 
and turn it into a Word97 exporter.

%package -n %develname
Summary: 	Word97 exporter library devel
Group:	 	Development/C
Requires:	%libname = %version-%release
Obsoletes:	wv2-devel
Provides:	wv2-devel = %version-%release
Obsoletes:	%{mklibname wv2_ 1 -d}

%description -n %develname
This is the Wv2 development package.

%prep
%setup -q
%patch3 -p0 -b .link

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%multiarch_binaries $RPM_BUILD_ROOT%{_bindir}/wv2-config

rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%_libdir/*.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_includedir/%{name}
%_libdir/*.so
%_bindir/wv2-config
%{multiarch_bindir}/wv2-config
%_libdir/wvWare
