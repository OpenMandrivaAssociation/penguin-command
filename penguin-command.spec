%define	name	penguin-command
%define	version	1.6.11
%define	release	%mkrel 1
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
BuildRequires:	SDL-devel audiofile-devel esound-devel SDL_mixer-devel SDL_image-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a clone of the classic "Missile Command" Game, but it has better
graphics and music. The gameplay has only been slightly modified. Penguin
Command is completely licensed under the GPL, excluding the music.

%prep
%setup -q

%build
%configure --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" icon="%{name}.png" \
  needs="x11" section="More Applications/Games/Arcade" title="Penguin Command" \
  longtitle="%{Summary}"
EOF

install -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc README NEWS AUTHORS
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_mandir}/*/*
