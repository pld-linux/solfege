#
# Conditional build:
# _without_gnome	- without GNOME support
#
# TODO:
# - finish gnome
# - xsltproc crashes (SEGV) on online-docs/C/{gpl,fdl}.html
# - *.py, *.pyc and *.pyo everywhere - exclude some of them?
# - no --without-gtkhtml for _without_gnome (python gtkhtml2 binding needed)
Summary:	Eartraining program for GNOME
Summary(de):	Gehörbildungssoftware für GNOME
Summary(pl):	Program do æwiczenia s³uchu dla GNOME
Name:		solfege
Version:	1.9.10
Release:	1
License:	GPL
Vendor:		Tom Cato Amundsen <tca@gnu.org>
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/solfege/%{name}-%{version}.tar.gz
# Source0-md5:	da687103a29d8ca8afa73599515427b0
Patch0:		%{name}-fix.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://solfege.sourceforge.net/
BuildRequires:	docbook-style-xsl
BuildRequires:	libgtkhtml-devel >= 1.99.9
BuildRequires:	libxslt-progs
BuildRequires:	m4
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-pygtk-gtk >= 1.99.11
%{!?_without_gnome:BuildRequires:	python-pygnome >= 1.99.11}
BuildRequires:	swig >= 1.3
Requires:	libgtkhtml >= 1.99.9
Requires:	python-pygtk-gtk >= 1.99.11
%{!?_without_gnome:Requires:	python-pygnome >= 1.99.11}
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

%description -l pl
Solfege jest programem do æwiczenia s³uchu dla X napisanym w Pythonie,
u¿ywaj±cym bibliotek GTK+ i GNOME. Jest w stadium rozwoju, czê¶æ
funkcji mo¿e nie dzia³aæ prawid³owo - problemy zg³aszaj na adres
solfege-devel@lists.sourceforge.net .

Æwiczenie s³uchu to rozleg³y temat, z wieloma powi±zaniami do teorii
muzyki i jej wykonywania, wiêc autor nawet nie próbowa³ stworzyæ
kompletnego narzêdzia. Ale ma nadziejê, ¿e komu¶ siê przyda.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	PYTHON=/usr/bin/python \
	--enable-docbook-stylesheet=/usr/share/sgml/docbook/xsl-stylesheets/html/chunk.xsl \
	--with-swig13 \
	%{?_without_gnome:--without-gtkhtml --without-gnome}

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
%doc AUTHORS FAQ README TODO changelog
%attr(755,root,root) %{_bindir}/solfege
%attr(755,root,root) %{_libdir}/solfege
%dir %{_datadir}/solfege
%dir %{_datadir}/solfege/%{version}
%{_datadir}/solfege/%{version}/feta
%{_datadir}/solfege/%{version}/gnomeemu
%{_datadir}/solfege/%{version}/graphics
%{_datadir}/solfege/%{version}/lesson-files
%{_datadir}/solfege/%{version}/mpd
%{_datadir}/solfege/%{version}/soundcard
%{_datadir}/solfege/%{version}/src
%{_datadir}/solfege/%{version}/default.config
%{_datadir}/solfege/%{version}/solfege.gtkrc
%dir %{_datadir}/solfege/%{version}/online-docs
%{_datadir}/solfege/%{version}/online-docs/C
%{_datadir}/solfege/%{version}/online-docs/png
%lang(es_MX) %{_datadir}/solfege/%{version}/online-docs/es_MX
%lang(nl) %{_datadir}/solfege/%{version}/online-docs/nl
%lang(no) %{_datadir}/solfege/%{version}/online-docs/no
%lang(ru) %{_datadir}/solfege/%{version}/online-docs/ru
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/solfege*
%{_mandir}/man1/solfege.1*
