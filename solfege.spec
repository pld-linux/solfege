Summary:	Eartraining program for GNOME
Summary(de):	Geh�rbildungssoftware f�r GNOME
Summary(pl):	Program do �wiczenia s�uchu dla GNOME
Name:		solfege
Version:	0.7.31
Release:	1
License:	GPL
Vendor:		Tom Cato Amundsen <tca@gnu.org>
Group:		X11/Applications/Sound
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/solfege/%{name}-%{version}.tar.gz
URL:		http://solfege.sourceforge.net/
BuildRequires:	m4
BuildRequires:	python-devel >= 2.0
Requires:	pygnome >= 1.0.50, pygtk >= 0.6.3
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

%build
CFLAGS="%{rpmcflags} -I/usr/include/python2.0"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files -f rpm/files.list
%defattr(644,root,root,755)
%doc README TODO changelog
