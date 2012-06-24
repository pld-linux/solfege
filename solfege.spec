Summary:	Eartraining program for GNOME
Summary(de):	Geh�rbildungssoftware f�r GNOME
Summary(pl):	Program do �wiczenia s�uchu dla GNOME
Name:		solfege
Version:	3.6.4
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/solfege/%{name}-%{version}.tar.gz
# Source0-md5:	71401b22158410d95595c308c6fee714
Patch0:		%{name}-fix.patch
Patch1:		%{name}-desktop.patch
URL:		http://solfege.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	ghostscript
# rsvg program
BuildRequires:	librsvg
BuildRequires:	libxslt-progs >= 1.0.31
BuildRequires:	lilypond
BuildRequires:	m4
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.17
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-pygtk-devel >= 2.6.0
BuildRequires:	swig-python >= 1.3.25
BuildRequires:	tetex-dvips
# xml2po >= 0.4 - required only on en manual changes
Requires:	python-pygtk-gtk >= 2.6.0
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

%description -l de
Solfege ist eine Geh�rbildungssoftware geschrieben in Python f�r X,
die GTK+ und GNOME Bibliotheken verwendet. Es handelt sich hierbei um
eine Entwicklerversion, manches mag noch Fehler haben. Dem INSTALL
Text k�nnen Informationen entnommen werden, falls Probleme bei der
Installation oder der Ausf�hrung auftreten sollten. Probleme k�nnen
solfege-devel@lists.sourceforge.net mitgeteilt werden.

Geh�rbildung stellt eine gro�e Anforderung an viele Bereiche der
Musiktheorie dar, weshalb ich nicht versucht habe, einen vollst�ndigen
Computerkurs Geh�rbildung zu erstellen. Ich hoffe aber, dass so
mancher diese Software hilfreich findet.

%description -l pl
Solfege jest programem do �wiczenia s�uchu dla X napisanym w Pythonie,
u�ywaj�cym bibliotek GTK+ i GNOME. Jest w stadium rozwoju, cz��
funkcji mo�e nie dzia�a� prawid�owo - problemy zg�aszaj na adres
solfege-devel@lists.sourceforge.net .

�wiczenie s�uchu to rozleg�y temat, z wieloma powi�zaniami do teorii
muzyki i jej wykonywania, wi�c autor nawet nie pr�bowa� stworzy�
kompletnego narz�dzia. Ale ma nadziej�, �e komu� si� przyda.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mv -f po/{no,nb}.po

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	PYTHON=/usr/bin/python \
	--enable-docbook-stylesheet=/usr/share/sgml/docbook/xsl-stylesheets/html/chunk.xsl

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/solfege/help/{no,nb}

# no *.py[co] now
#find $RPM_BUILD_ROOT%{_datadir}/solfege -name '*.py' | xargs rm -f

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FAQ README changelog
%attr(755,root,root) %{_bindir}/lessonfile_editor
%attr(755,root,root) %{_bindir}/solfege
%dir %{_libdir}/solfege
%attr(755,root,root) %{_libdir}/solfege/_solfege_c_midi.so
%dir %{_datadir}/solfege
%{_datadir}/solfege/example-lesson-files
%{_datadir}/solfege/feta
%{_datadir}/solfege/graphics
%dir %{_datadir}/solfege/help
%{_datadir}/solfege/help/C
%lang(fr) %{_datadir}/solfege/help/fr
%lang(nb) %{_datadir}/solfege/help/nb
%lang(tr) %{_datadir}/solfege/help/tr
%{_datadir}/solfege/lesson-files
%{_datadir}/solfege/mpd
%{_datadir}/solfege/soundcard
%{_datadir}/solfege/src
%{_datadir}/solfege/themes
%{_datadir}/solfege/default.config
%{_datadir}/solfege/solfege.gtkrc
%{_datadir}/solfege/*tree.txt
%{_datadir}/solfege/*.xml
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/solfege*
%{_pixmapsdir}/solfege.png
%{_desktopdir}/solfege.desktop
%{_mandir}/man1/lessonfile_editor.1*
%{_mandir}/man1/solfege.1*
