# Generated automatically from solfege.spec.in by configure.
Summary: Eartaining program for GNOME
Summary(de): Gehörbildungssoftware für GNOME
Name: solfege
Version: 0.7.28
Release: 1
Vendor: Tom Cato Amundsen (tca@gnu.org)
Source: http://download.sourceforge.net/solfege/%{name}-%{version}.tar.gz
URL: http://solfege.sourceforge.net/
Copyright: GPL, see file COPYING for details
Group: Applications/Multimedia
Requires: pygnome >= 1.0.50, pygtk >= 0.6.3
BuildRoot: /tmp/%name-%{version}

%description
Solfege is an eartraining program for X written in python, using the
GTK+ and GNOME libraries. This is a development release, things might
be broken. See INSTALL file if you have problems running or installing
Solfege. Report your problems to solfege-devel@lists.sourceforge.net

Eartraining is a big subject with many connections to music theory and
performance of music, so I won't even try to make "a complete
computerbased eartraining course". But I hope someone find this
software useful.

%description -l de
Solfege ist eine Gehörbildungssoftware geschrieben in Python für X, die
GTK+ und GNOME Bibliotheken verwendet. Es handelt sich hierbei um eine
Entwicklerversion, manches mag noch Fehler haben. Dem INSTALL Text können
Informationen entnommen werden, falls Probleme bei der Installation oder
der Ausführung auftreten sollten. Probleme können solfege-devel@lists.sourceforge.net
mitgeteilt werden.

Gehörbildung stellt eine große Anforderung an viele Bereiche der
Musiktheorie dar, weshalb ich nicht versucht habe, einen vollständigen
Computerkurs Gehörbildung zu erstellen. Ich hoffe aber, dass so
mancher diese Software hilfreich findet.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build
./configure --prefix=/usr
make

%install
make sysconfdir="$RPM_BUILD_ROOT/etc" prefix="$RPM_BUILD_ROOT/usr" nopycompile=YES install

%clean
rm -rf $RPM_BUILD_ROOT

%files -f rpm/files.list

%defattr(-,root,root)
%doc INSTALL README TODO COPYING changelog
