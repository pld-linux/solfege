#
# Conditional build:
# _without_gnome	- without GNOME support
#
# TODO:
# - *.py, *.pyc and *.pyo everywhere - exclude some of them?
Summary:	Eartraining program for GNOME
Summary(de):	Geh�rbildungssoftware f�r GNOME
Summary(pl):	Program do �wiczenia s�uchu dla GNOME
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
%{!?_without_gnome:BuildRequires:	libgtkhtml-devel >= 1.99.9}
BuildRequires:	libxslt-progs >= 1.0.31
BuildRequires:	m4
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-pygtk-devel >= 1.99.11
%{!?_without_gnome:BuildRequires:	python-gnome-devel >= 1.99.11}
BuildRequires:	swig >= 1.3
%{!?_without_gnome:Requires:	libgtkhtml >= 1.99.9}
Requires:	python-pygtk-gtk >= 1.99.11
%{!?_without_gnome:Requires:	python-gnome-gtkhtml >= 1.99.11}
%{!?_without_gnome:Requires:	python-gnome-ui >= 1.99.11}
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
	DESTDIR=$RPM_BUILD_ROOT \
	applnkdir=%{_applnkdir}/Utilities

%{?_without_gnome:install -D solfege.desktop $RPM_BUILD_ROOT%{_applnkdir}/Utilities}
%{?_without_gnome:install -D graphics/solfege.png $RPM_BUILD_ROOT%{_pixmapsdir}/solfege.png}
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
%{?_without_gnome:%{_datadir}/solfege/%{version}/gnomeemu}
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
%{_pixmapsdir}/solfege.png
%{_applnkdir}/Utilities/solfege.desktop
%{_mandir}/man1/solfege.1*
