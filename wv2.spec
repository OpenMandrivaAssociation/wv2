%define major		4
%define libname		%mklibname %{name}_ %{major}
%define develname	%mklibname %{name} -d

Summary:	Word97 exporter library
Name:		wv2
Version:	0.4.2
Release:	12
License:	LGPLv2
Group:		Office
URL:		https://sourceforge.net/projects/wvware/
Source0: 	http://downloads.sourceforge.net/wvware/%{name}-%{version}.tar.bz2
Patch0:		wv2-0.4.2-glib.patch
Patch3:		wv2-0.4.2-linkage.patch
BuildRequires:	pkgconfig(libgsf-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	cmake

%description
wvWare is the continuation of Caolan McNamara's wv - the MSWord library.
Efforts are underway to make this library more correct, robust,
and turn it into a Word97 exporter.

%package -n %{libname}
Summary: 	Word97 exporter library
Group:	 	Development/C
Provides:	%{name} = %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
wvWare is the continuation of Caolan McNamara's wv - the MSWord library. 
Efforts are underway to make this library more correct, robust, 
and turn it into a Word97 exporter.

%package -n %{develname}
Summary: 	Word97 exporter library devel
Group:	 	Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	wv2-devel = %{version}-%{release}

%description -n %{develname}
This is the Wv2 development package.

%prep
%setup -q
%patch0 -p1 -b .glib
%patch3 -p0 -b .link

%build
%cmake
%make

%install
%makeinstall_std -C build

%multiarch_binaries %{buildroot}%{_bindir}/wv2-config

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_bindir}/wv2-config
%{multiarch_bindir}/wv2-config
%{_libdir}/wvWare

%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-3mdv2011.0
+ Revision: 661757
- multiarch fixes

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.2-2mdv2011.0
+ Revision: 608176
- rebuild

* Wed Nov 04 2009 Funda Wang <fwang@mandriva.org> 0.4.2-1mdv2010.1
+ Revision: 460420
- New version 0.4.2

* Sat Oct 10 2009 Funda Wang <fwang@mandriva.org> 0.4.0-4mdv2010.0
+ Revision: 456503
- fix libdir declaration in wv2-config

* Sat Oct 10 2009 Funda Wang <fwang@mandriva.org> 0.4.0-3mdv2010.0
+ Revision: 456502
- fix include dir for glib

* Thu Oct 08 2009 Funda Wang <fwang@mandriva.org> 0.4.0-2mdv2010.0
+ Revision: 456123
- link against gojbect too

* Tue Sep 15 2009 Frederik Himpe <fhimpe@mandriva.org> 0.4.0-1mdv2010.0
+ Revision: 443271
- Add patch from Fedora fixing lib suffix on 64 bit

  + Nicolas LÃ©cureuil <nlecureuil@mandriva.com>
    - Fix BuildRequires
    - New version 0.4.0

* Mon Mar 16 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 0.3.1-2mdv2009.1
+ Revision: 355730
- Do not package .la files
- Remove unneeded macros

* Fri Mar 06 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 0.3.1-1mdv2009.1
+ Revision: 349640
- Update to 0.3.1

* Sun Feb 22 2009 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 0.3.0-3mdv2009.1
+ Revision: 343791
- Update to 0.3.0
  Disable patch1 ( does not seems needed )

* Tue Aug 26 2008 Funda Wang <fwang@mandriva.org> 0.2.3-3mdv2009.0
+ Revision: 276383
- add patch fix building

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-2mdv2008.1
+ Revision: 179672
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Aug 04 2007 Adam Williamson <awilliamson@mandriva.org> 0.2.3-1mdv2008.0
+ Revision: 58814
- rebuild for 2008
- new devel policy
- drop patch1 (fixed upstream)
- clean buildrequires
- use Fedora license policy, correct license (LGPLv2, not GPL)
- spec clean
- new release 0.2.3
- Import wv2




* Tue Jun 20 2006 Laurent MONTEL <lmontel@mandriva.com> 0.2.2-6
- Add patch1: security fix

* Sat Mar 11 2006 Laurent MONTEL <lmontel@mandriva.com> 0.2.2-5mdk
- Rebuild with new libgsf

* Wed Oct 12 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.2-4mdk
- Rebuild for new libgsf-1_1

* Mon Jan 31 2005 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2.2-3mdk
- Fix multiarch

* Thu Jun  3 2004 Laurent Montel <lmontel@mandrakesoft.com> 0.2.2-2mdk
- Rebuild against new gcc

* Wed May 19 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2.2-1mdk
- 0.2.2

* Mon Dec 29 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2.1-1mdk
- 0.2.1

* Wed Nov 05 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.2-1mdk
- 0.2

* Mon Sep 01 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1.9-1mdk
- 0.1.9

* Thu Aug 07 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1.8-1mdk
- 0.1.8

* Thu Jul 31 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1.7-2mdk
- libification

* Thu Jul 31 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1.7-1mdk
- 0.1.7

* Thu Jul 31 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1-6mdk
- fix buildrequires and requires
- autoconf2.5 macro

* Fri Jul 18 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.1-5mdk
- grmpf, more buildrequires

* Mon Jul 14 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.1-4mdk
- cosmetics
- quiet setup
- buildrequires
- fix library-without-ldconfig-post{un,in} (package name should really
  be changed to follow mdk library police!!)

* Thu Jul 10 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1-3mdk
- Rebuild

* Wed Jul 09 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1-2mdk
- Rebuild

* Thu Jul 03 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.1-1mdk
- First import
