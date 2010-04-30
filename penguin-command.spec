%define	name	penguin-command
%define	version	1.6.11
%define	release	%mkrel 5
%define	Summary	A clone of the classic Missile Command game

Name:		%{name}
Summary:	%{Summary}
Version:	%{version}
Release:	%{release}
Source0:	http://belnet.dl.sourceforge.net/sourceforge/penguin-command/%{name}-%{version}.tar.bz2
Source11:	%{name}.16.png
Source12:	%{name}.32.png
Source13:	%{name}.48.png
URL:		http://www.linux-games.com/penguin-command/index.html
License:	GPL
Group:		Games/Arcade
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_image-devel
Requires:	soundwrapper
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
