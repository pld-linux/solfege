#
# Conditional build:
%bcond_without	gnome	# without GNOME support
#
Summary:	Eartraining program for GNOME
Summary(de):	Gehörbildungssoftware für GNOME
Summary(pl):	Program do æwiczenia s³uchu dla GNOME
Name:		solfege
Version:	2.1.3
Release:	2
License:	GPL v2+
Vendor:		Tom Cato Amundsen <tca@gnu.org>
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/solfege/%{name}-%{version}.tar.gz
# Source0-md5:	ef4e964a8d8345debc5c7b78888969d2
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-fix.patch
Patch2:		%{name}-exdata.patch
Patch3:		%{name}-desktop.patch
URL:		http://solfege.sourceforge.net/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
%{?with_gnome:BuildRequires:	libgtkhtml-devel >= 1.99.9}
BuildRequires:	libxslt-progs >= 1.0.31
BuildRequires:	lilypond
BuildRequires:	m4
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-pygtk-devel >= 1.99.11
%{?with_gnome:BuildRequires:	python-gnome-devel >= 1.99.11}
BuildRequires:	swig >= 1.3
%{?with_gnome:Requires:	libgtkhtml >= 1.99.9}
Requires:	python-pygtk-gtk >= 1.99.11
%{?with_gnome:Requires:	python-gnome-gtkhtml >= 1.99.11}
%{?with_gnome:Requires:	python-gnome-ui >= 1.99.11}
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
%patch2 -p1
%patch3 -p1

mv -f po/{no,nb}.po

# different version of lilypond req'd? doesn't work with 2.2.[1-4]
%{__perl} -pi -e 's/--outdir/--output/' online-docs/Makefile

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	PYTHON=/usr/bin/python \
	--enable-docbook-stylesheet=/usr/share/sgml/docbook/xsl-stylesheets/html/chunk.xsl \
	%{!?with_gnome:--without-gtkhtml --without-gnome}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	applnkdir=%{_desktopdir}

%{!?with_gnome:install -D solfege.desktop $RPM_BUILD_ROOT%{_desktopdir}/solfege.desktop}
%{!?with_gnome:install -D graphics/solfege.png $RPM_BUILD_ROOT%{_pixmapsdir}/solfege.png}

# no *.py[co] now
#find $RPM_BUILD_ROOT%{_datadir}/solfege -name '*.py' | xargs rm -f

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
%{_datadir}/solfege/%{version}/example-lesson-files
%{_datadir}/solfege/%{version}/feta
%{!?with_gnome:%{_datadir}/solfege/%{version}/gnomeemu}
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
# temporarily disabled - waits for update
#%lang(nl) %{_datadir}/solfege/%{version}/online-docs/nl
%lang(nb) %{_datadir}/solfege/%{version}/online-docs/no
%lang(ru) %{_datadir}/solfege/%{version}/online-docs/ru
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/solfege*
%{_pixmapsdir}/solfege.png
%{_desktopdir}/solfege.desktop
%{_mandir}/man1/solfege.1*
