Summary:	Eartraining program for GNOME
Summary(de.UTF-8):	Gehörbildungssoftware für GNOME
Summary(pl.UTF-8):	Program do ćwiczenia słuchu dla GNOME
Name:		solfege
Version:	3.23.4
Release:	1
License:	GPL v3
Group:		X11/Applications/Sound
Source0:	ftp://alpha.gnu.org/gnu/solfege/%{name}-%{version}.tar.gz
# Source0-md5:	7f3044982d188024d0318dccb4bc58d4
Patch0:		%{name}-fix.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-paths.patch
Patch3:		%{name}-python.patch
Patch4:		%{name}-sequencer_tempo.patch
URL:		https://www.gnu.org/software/solfege/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gnome-doc-utils
BuildRequires:	lilypond
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.17
BuildRequires:	python3-devel
BuildRequires:	python3-pygobject3
BuildRequires:	rpm-pythonprov
BuildRequires:	swig-python >= 1.3.25
BuildRequires:	texinfo
# xml2po >= 0.4 - required only on en manual changes
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Solfege is an eartraining program for X written in python, using the
GTK+ and GNOME libraries. This is a development release, things might
be broken. See INSTALL file if you have problems running or installing
Solfege. Report your problems to solfege-devel@lists.sourceforge.net .

Eartraining is a big subject with many connections to music theory and
performance of music, so I won't even try to make "a complete
computerbased eartraining course". But I hope someone find this
software useful.

%description -l de.UTF-8
Solfege ist eine Gehörbildungssoftware geschrieben in Python für X,
die GTK+ und GNOME Bibliotheken verwendet. Es handelt sich hierbei um
eine Entwicklerversion, manches mag noch Fehler haben. Dem INSTALL
Text können Informationen entnommen werden, falls Probleme bei der
Installation oder der Ausführung auftreten sollten. Probleme können
solfege-devel@lists.sourceforge.net mitgeteilt werden.

Gehörbildung stellt eine große Anforderung an viele Bereiche der
Musiktheorie dar, weshalb ich nicht versucht habe, einen vollständigen
Computerkurs Gehörbildung zu erstellen. Ich hoffe aber, dass so
mancher diese Software hilfreich findet.

%description -l pl.UTF-8
Solfege jest programem do ćwiczenia słuchu dla X napisanym w Pythonie,
używającym bibliotek GTK+ i GNOME. Jest w stadium rozwoju, część
funkcji może nie działać prawidłowo - problemy zgłaszaj na adres
solfege-devel@lists.sourceforge.net .

Ćwiczenie słuchu to rozległy temat, z wieloma powiązaniami do teorii
muzyki i jej wykonywania, więc autor nawet nie próbował stworzyć
kompletnego narzędzia. Ale ma nadzieję, że komuś się przyda.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	RSVG=%{_bindir}/rsvg \
	LILYPOND=%{_bindir}/lilypond \
	BZR=%{_bindir}/bzr \
	GS=%{_bindir}/gs \
	PYTHON=%{__python3} \
        --enable-docbook-stylesheet=%{_datadir}/sgml/docbook/xsl-stylesheets/html/chunk.xsl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS FAQ README changelog*
%attr(755,root,root) %{_bindir}/solfege
%dir %{_libdir}/solfege
%attr(755,root,root) %{_libdir}/solfege/_solfege_c_midi.so
%dir %{_datadir}/solfege
%{_datadir}/solfege/solfege
%{_datadir}/solfege/exercises
%{_datadir}/solfege/feta
%{_datadir}/solfege/graphics
%dir %{_datadir}/solfege/help
%{_datadir}/solfege/help/style.css
%{_datadir}/solfege/help/C
%lang(de) %{_datadir}/solfege/help/de
%lang(eo) %{_datadir}/solfege/help/eo
%lang(es) %{_datadir}/solfege/help/es
%lang(et) %{_datadir}/solfege/help/et
%lang(fr) %{_datadir}/solfege/help/fr
%lang(gl) %{_datadir}/solfege/help/gl
%lang(nb) %{_datadir}/solfege/help/nb
%lang(nl) %{_datadir}/solfege/help/nl
%lang(pl) %{_datadir}/solfege/help/pl
%lang(pt_BR) %{_datadir}/solfege/help/pt_BR
%lang(ru) %{_datadir}/solfege/help/ru
%lang(tr) %{_datadir}/solfege/help/tr
%{_datadir}/solfege/default.config
%{_datadir}/solfege/*.xml
%{_datadir}/solfege/solfege.css
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/solfege*
%{_pixmapsdir}/solfege.svg
%{_desktopdir}/solfege.desktop
