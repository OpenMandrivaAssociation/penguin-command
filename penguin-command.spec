%define	name	penguin-command
%define	version	1.6.11
%define release	8
%define	Summary	A clone of the classic Missile Command game

Name:		%{name}
Summary:	%{Summary}
Version:	%{version}
Release:	%{release}
Source0:	http://belnet.dl.sourceforge.net/sourceforge/penguin-command/%{name}-%{version}.tar.bz2
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
URL:		https://www.linux-games.com/penguin-command/index.html
License:	GPL
Group:		Games/Arcade
BuildRequires:	pkgconfig(sdl)
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
BuildRequires:  pkgconfig(zlib)
# Disable it, since soundwrapper is not anymore available for cooker. (penguin)
#Requires:	soundwrapper
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a clone of the classic "Missile Command" Game, but it has better
graphics and music. The gameplay has only been slightly modified. Penguin
Command is completely licensed under the GPL, excluding the music.

%prep
%setup -q

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Penguin Command
Comment=%{Summary}
Exec=soundwrapper %{_gamesbindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README NEWS AUTHORS
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_mandir}/*/*


%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.6.11-6mdv2011.0
+ Revision: 614493
- the mass rebuild of 2010.1 packages

* Fri Apr 30 2010 Funda Wang <fwang@mandriva.org> 1.6.11-5mdv2010.1
+ Revision: 541242
- update BR

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 1.6.11-4mdv2009.1
+ Revision: 350226
- 2009.1 rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.6.11-3mdv2009.0
+ Revision: 255181
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.6.11-1mdv2008.1
+ Revision: 136656
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Thu Aug 02 2007 Olivier Blin <oblin@mandriva.com> 1.6.11-1mdv2008.0
+ Revision: 58068
- use soundwrapper
- XDG menu
- 1.6.11
- Import penguin-command



* Fri Jan 14 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.6.8-2mdk
- fix buildrequires

* Fri Nov 12 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.6.8-1mdk
- 1.6.8
- cosmetics

* Sun Sep 05 2004 Michael Scherer <misc@mandrake.org> 1.6.6-3mdk
- rebuild
- clean BuildRequires
- remove packager tag
- do not bzip2 icons
- use new menu scheme

* Wed May 07 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.6.6-2mdk
- use normal configure (Arkadiusz Lipiec)

* Fri Apr 25 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 1.6.6-1mdk
- new version
- fix buildrequires thx to stefan's robot

* Thu Sep 05 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.6.5-3mdk

* Sun Jul 21 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.6.5-2mdk
- recompile against new vorbis stuff

* Wed Jun 12 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.6.5-1mdk
- 1.6.5
- bzip tarball
- png icons (out xpm!)

* Mon Apr 29 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 1.6.2-2mdk
- rebuild for new alsa

* Fri Oct 12 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.6.2-1mdk
- new version
- rebuild for libpng3
- fix obsolete-tag Copyright
- fix large-icon-not-in-package
- include man page

* Fri Jun 15 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.6.1-1mdk
- version 1.6.1

* Mon May 14 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.5.1-1mdk
- version 1.5.1
- new SDL

* Sun Apr 22 2001  Stew Benedict <sbenedict@mandrakesoft.com> 1.5.0-2mdk
- no kgcc for PPC

* Fri Mar 30 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.5.0-1mdk
- 1.5.0

* Wed Mar 28 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2-7mdk
- change URL per request of author Karl Bartel <karlb@gmx.net>

* Sun Dec 25 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 1.2-6mdk
- fix BuildRequires

* Wed Nov 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2-5mdk
- rebuild to follow new lib policy of SDL_mixer

* Wed Aug 30 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2-4mdk
- remove binary-or-shlib-refines-rpath

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2-3mdk
- automatically added packager tag

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.2-2mdk
- automatically added BuildRequires

* Wed Jul 26 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2-1mdk
- first package for Linux-Mandrake
