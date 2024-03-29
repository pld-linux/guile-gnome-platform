#
# Conditional build:
%bcond_without	gnome	# GNOME components (bonobo, libgnome, libgnomeui)
#
Summary:	guile-gnome platform
Summary(pl.UTF-8):	Platforma guile-gnome
Name:		guile-gnome-platform
Version:	2.16.5
Release:	3
License:	GPL v2+
Group:		Development/Languages/Scheme
Source0:	http://ftp.gnu.org/gnu/guile-gnome/guile-gnome-platform/%{name}-%{version}.tar.gz
# Source0-md5:	5fb232f2a236df88072acda203cf72a8
Patch0:		%{name}-info.patch
Patch1:		%{name}-guile3.patch
Patch2:		%{name}-make.patch
URL:		http://www.gnu.org/software/guile-gnome/
BuildRequires:	GConf2-devel >= 2.18
BuildRequires:	atk-devel >= 1:1.12
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.14
BuildRequires:	g-wrap-devel >= 2:1.9.15
BuildRequires:	gdk-pixbuf2-devel >= 2.10.0
BuildRequires:	glib2-devel >= 1:2.10.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	guile-cairo-devel
BuildRequires:	guile-devel >= 5:2.0.14
%{?with_gnome:BuildRequires:	libbonobo-devel >= 2.0}
BuildRequires:	libglade2-devel >= 1:2.6
%{?with_gnome:BuildRequires:	libgnome-devel >= 2.16}
BuildRequires:	libgnomecanvas-devel >= 2.14
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.16.0}
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1:1.14
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	texinfo
Obsoletes:	guile-gnome-corba < 2.16.5
Obsoletes:	guile-gnome-corba-devel < 2.16.5
Obsoletes:	guile-gnome-gnome-vfs < 2.16.5
Requires:	guile >= 5:2.0.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The guile-gnome project brings the power of Scheme to your graphical
application. guile-gnome modules support the entire GNOME library
stack: from Pango to GnomeCanvas, GTK+ to GStreamer, Glade to
GtkSourceView, you will find in guile-gnome a comprehensive
environment for developing modern applications.

%description -l pl.UTF-8
Projekt guile-gnome przenosi potęgę Scheme do aplikacji graficznych.
Moduły guile-gnome obsługują cały stos bibliotek GNOME: od Pango do
GnomeCanvas, GTK+ do GStreamera, Glade do GtkSourceView; w guile-gnome
można znaleźć obszerne środowisko do tworzenia nowoczesnych aplikacji.

%package -n guile-gnome-atk
Summary:	guile-gnome platform - ATK module
Summary(pl.UTF-8):	Platforma gnome-guile - moduł ATK
Group:		Development/Languages/Scheme
Requires:	guile-gnome-glib = %{version}-%{release}
Requires:	atk >= 1:1.12

%description -n guile-gnome-atk
guile-gnome-atk is a Guile wrapper for ATK, the Accessibility Toolkit.

%description -n guile-gnome-atk -l pl.UTF-8
guile-gnome-atk to wrapper Guile dla biblioteki ATK (Accessibility
Toolkit).

%package -n guile-gnome-cairo
Summary:	guile-gnome platform - Cairo module
Summary(pl.UTF-8):	Platforma gnome-guile - moduł Cairo
Group:		Development/Languages/Scheme
Requires:	guile-gnome-glib = %{version}-%{release}
# there is reference, but drop loop
#Requires:	guile-gnome-gtk = %{version}-%{release}
Requires:	guile-cairo

%description -n guile-gnome-cairo
guile-gnome-cairo integrates the Guile-Cairo bindings with G-Wrap,
providing other guile-gnome wrappers with the ability to automatically
wrap Cairo types. It is not a cairo wrapper in and of itself.

%description -n guile-gnome-cairo -l pl.UTF-8
guile-gnome-cairo integruje dowiązania Guile-Cairo z G-Wrap, dając
innym wrapperom guile-gnome możliwość automatycznego obudowywania
typów Cairo. Nie jest to wrapper cairo jako taki.

%package -n guile-gnome-canvas
Summary:	guile-gnome platform - Canvas module
Summary(pl.UTF-8):	Platforma gnome-guile - moduł Canvas
Group:		Development/Languages/Scheme
Requires:	guile-gnome-gtk = %{version}-%{release}
Requires:	libgnomecanvas >= 2.14

%description -n guile-gnome-canvas
guile-gnome-canvas is a Guile wrapper for the GNOME canvas library.

%description -n guile-gnome-canvas -l pl.UTF-8
guile-gnome-canvas to wrapper Guile dla biblioteki widgetu GNOME
canvas.

%package -n guile-gnome-gconf
Summary:	guile-gnome platform - GConf module
Summary(pl.UTF-8):	Platforma gnome-guile - moduł GConf
Group:		Development/Languages/Scheme
Requires:	guile-gnome-glib = %{version}-%{release}
Requires:	GConf2 >= 2.18

%description -n guile-gnome-gconf
guile-gnome-gconf is a Guile wrapper for GConf.

%description -n guile-gnome-gconf -l pl.UTF-8
guile-gnome-gconf to wrapper Guile dla GConfa.

%package -n guile-gnome-glib
Summary:	guile-gnome platform - GLib/GObject module
Summary(pl.UTF-8):	Platforma gnome-guile - moduł GLib/GObject
Group:		Libraries
Requires(post,postun):	/sbin/ldconfig
Requires:	%{name} = %{version}-%{release}
Requires:	g-wrap >= 2:1.9.15
Requires:	glib2 >= 1:2.10.0

%description -n guile-gnome-glib
guile-gnome-glib is a Guile wrapper for GLib and GObject. It also
includes a bindings generator based on G-Wrap.

%description -n guile-gnome-glib -l pl.UTF-8
guile-gnome-guileto wrapper Guile dla bibliotek GLib i GObject.
Zawiera także generator dowiązań oparty na bibliotece G-Wrap.

%package -n guile-gnome-glib-devel
Summary:	Header files for guile-gnome-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki guile-gnome-glib
Group:		Development/Libraries
Requires:	guile-gnome-glib = %{version}-%{release}
Requires:	g-wrap-devel >= 2:1.9.15
Requires:	glib2-devel >= 1:2.10.0
Requires:	guile-devel >= 1:1.8.0

%description -n guile-gnome-glib-devel
Header files for guile-gnome-glib library.

%description -n guile-gnome-glib-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki guile-gnome-glib.

%package -n guile-gnome-gtk
Summary:	guile-gnome platform - GTK/GDK module
Summary(pl.UTF-8):	Platforma gnome-guile - moduł GTK/GDK
Group:		Development/Languages/Scheme
Requires:	guile-gnome-atk = %{version}-%{release}
Requires:	guile-gnome-cairo = %{version}-%{release}
Requires:	guile-gnome-glib = %{version}-%{release}
Requires:	guile-gnome-pango = %{version}-%{release}
Requires:	gdk-pixbuf2 >= 2.10.0
Requires:	gtk+2 >= 2:2.10.0

%description -n guile-gnome-gtk
guile-gnome-gtk is a Guile wrapper for GTK+ and GDK.

%description -n guile-gnome-gtk -l pl.UTF-8
guile-gnome-gtk to wrapper Guile dla bibliotek GTK+ i GDK.

%package -n guile-gnome-libglade
Summary:	guile-gnome platform - Glade module
Summary(pl.UTF-8):	Platforma gnome-guile - moduł Glade
Group:		Development/Languages/Scheme
Requires:	guile-gnome-gtk = %{version}-%{release}
Requires:	libglade2 >= 1:2.6

%description -n guile-gnome-libglade
guile-gnome-libglade is a Guile wrapper for libglade.

%description -n guile-gnome-libglade -l pl.UTF-8
guile-gnome-libglade to wrapper Guile dla biblioteki libglade.

%package -n guile-gnome-libgnome
Summary:	guile-gnome platform - libgnome module
Summary(pl.UTF-8):	Platforma gnome-guile - moduł libgnome
Group:		Development/Languages/Scheme
Requires:	guile-gnome-glib = %{version}-%{release}
Requires:	libgnome >= 2.16

%description -n guile-gnome-libgnome
guile-gnome-libgnome is a Guile wrapper for libgnome.

%description -n guile-gnome-libgnome -l pl.UTF-8
guile-gnome-libgnome to wrapper Guile dla biblioteki libgnome.

%package -n guile-gnome-libgnomeui
Summary:	guile-gnome platform - libgnomeui module
Summary(pl.UTF-8):	Platforma gnome-guile - moduł libgnomeui
Group:		Development/Languages/Scheme
Requires:	guile-gnome-gtk = %{version}-%{release}
Requires:	guile-gnome-libgnome = %{version}-%{release}
Requires:	libgnomeui >= 2.16

%description -n guile-gnome-libgnomeui
guile-gnome-libgnome is a Guile wrapper for libgnomeui.

%description -n guile-gnome-libgnomeui -l pl.UTF-8
guile-gnome-libgnome to wrapper Guile dla biblioteki libgnomeui.

%package -n guile-gnome-pango
Summary:	guile-gnome platform - Pango module
Summary(pl.UTF-8):	Platforma gnome-guile - moduł Pango
Group:		Development/Languages/Scheme
Requires:	guile-gnome-cairo = %{version}-%{release}
Requires:	guile-gnome-glib = %{version}-%{release}
Requires:	pango >= 1:1.14

%description -n guile-gnome-pango
guile-gnome-pango is a Guile wrapper for Pango, an internationalized
text layout library.

%description -n guile-gnome-pango -l pl.UTF-8
guile-gnome-pango to wrapper Guile dla Pango - biblioteki składu
międzynarodowego tekstu.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libguile-gnome-*.la
# dlopened modules
%{__rm} $RPM_BUILD_ROOT%{_libdir}/guile-gnome-2/libgw-guile-gnome-*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n guile-gnome-atk -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n guile-gnome-atk -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n guile-gnome-canvas -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n guile-gnome-canvas -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n guile-gnome-gconf -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n guile-gnome-gconf -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n guile-gnome-glib
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun	-n guile-gnome-glib
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post	-n guile-gnome-gtk -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n guile-gnome-gtk -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n guile-gnome-libglade -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n guile-gnome-libglade -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n guile-gnome-libgnome -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n guile-gnome-libgnome -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n guile-gnome-libgnomeui -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n guile-gnome-libgnomeui -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%post	-n guile-gnome-pango -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-n guile-gnome-pango -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/guile-gnome-2
%dir %{_datadir}/guile-gnome-2/gnome
%{_datadir}/guile-gnome-2/gnome/defs
%dir %{_datadir}/guile-gnome-2/gnome/gw
%dir %{_datadir}/guile-gnome-2/gnome/overrides
# devel
%{_pkgconfigdir}/guile-gnome-defs-2.pc

%files -n guile-gnome-atk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-atk.so*
%doc atk/{AUTHORS,ChangeLog,README}
%{_datadir}/guile-gnome-2/gnome/atk.scm
%{_datadir}/guile-gnome-2/gnome/gw/atk.scm
%{_datadir}/guile-gnome-2/gnome/gw/atk-spec.scm
%{_datadir}/guile-gnome-2/gnome/overrides/atk.defs*
%{_infodir}/guile-gnome-atk.info*

%files -n guile-gnome-cairo
%defattr(644,root,root,755)
%doc cairo/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-cairo.so*
%{_datadir}/guile-gnome-2/gnome/gw/cairo.scm
%{_datadir}/guile-gnome-2/gnome/gw/cairo-spec.scm
# cairo-devel
%{_pkgconfigdir}/guile-gnome-cairo-2.pc

%files -n guile-gnome-canvas
%defattr(644,root,root,755)
%doc libgnomecanvas/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-canvas.so*
%{_datadir}/guile-gnome-2/gnome/canvas.scm
%{_datadir}/guile-gnome-2/gnome/gw/canvas.scm
%{_datadir}/guile-gnome-2/gnome/gw/canvas-spec.scm
%{_datadir}/guile-gnome-2/gnome/overrides/libgnomecanvas.defs
%{_infodir}/guile-gnome-libgnomecanvas.info*

%files -n guile-gnome-gconf
%defattr(644,root,root,755)
%doc gconf/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-gconf.so*
%{_datadir}/guile-gnome-2/gnome/gconf.scm
%{_datadir}/guile-gnome-2/gnome/gw/gconf.scm
%{_datadir}/guile-gnome-2/gnome/gw/gconf-spec.scm
%{_datadir}/guile-gnome-2/gnome/overrides/gconf.defs*
%{_infodir}/guile-gnome-gconf.info*

%files -n guile-gnome-glib
%defattr(644,root,root,755)
%doc glib/{AUTHORS,ChangeLog,NEWS.guile-gobject,README,REFCOUNTING,THREADING,TODO,WARTS}
%attr(755,root,root) %{_bindir}/guile-gnome-2
%attr(755,root,root) %{_libdir}/libguile-gnome-gobject-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguile-gnome-gobject-2.so.0
%dir %{_libdir}/guile-gnome-2
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-glib.so*
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-gobject.so*
%{_datadir}/guile/site/gnome-2.scm
%{_datadir}/guile-gnome-2/gnome/glib.scm
%{_datadir}/guile-gnome-2/gnome/gobject.scm
%{_datadir}/guile-gnome-2/gnome/gobject
%{_datadir}/guile-gnome-2/gnome/gw/generics.scm
%{_datadir}/guile-gnome-2/gnome/gw/glib.scm
%{_datadir}/guile-gnome-2/gnome/gw/glib-spec.scm
%{_datadir}/guile-gnome-2/gnome/gw/gobject.scm
%{_datadir}/guile-gnome-2/gnome/gw/gobject-spec.scm
%{_datadir}/guile-gnome-2/gnome/gw/support
%{_datadir}/guile-gnome-2/gnome/overrides/glib.defs*
%{_infodir}/guile-gnome-glib.info*
%{_infodir}/guile-gnome-gobject.info*

%files -n guile-gnome-glib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguile-gnome-gobject-2.so
%dir %{_includedir}/guile-gnome-2
%{_includedir}/guile-gnome-2/guile-gnome-gobject.h
%{_includedir}/guile-gnome-2/guile-gnome-gobject
%{_pkgconfigdir}/guile-gnome-glib-2.pc

%files -n guile-gnome-gtk
%defattr(644,root,root,755)
%doc gtk/{AUTHORS,ChangeLog,README,TODO}
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-gdk.so*
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-gtk.so*
%{_datadir}/guile-gnome-2/gnome/contrib
%{_datadir}/guile-gnome-2/gnome/gtk.scm
%{_datadir}/guile-gnome-2/gnome/gtk
%{_datadir}/guile-gnome-2/gnome/gw/gdk.scm
%{_datadir}/guile-gnome-2/gnome/gw/gdk-spec.scm
%{_datadir}/guile-gnome-2/gnome/gw/gtk.scm
%{_datadir}/guile-gnome-2/gnome/gw/gtk-spec.scm
%{_datadir}/guile-gnome-2/gnome/overrides/gdk.defs*
%{_datadir}/guile-gnome-2/gnome/overrides/gdk-pixbuf.defs
%{_datadir}/guile-gnome-2/gnome/overrides/gtk.defs*
%{_datadir}/guile-gnome-2/gnome/overrides/gtk-customs.defs
%{_infodir}/guile-gnome-gdk.info*
%{_infodir}/guile-gnome-gtk.info*
# gtk-devel
%{_pkgconfigdir}/guile-gnome-gtk-2.pc

%files -n guile-gnome-libglade
%defattr(644,root,root,755)
%doc libglade/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-libglade.so*
%{_datadir}/guile-gnome-2/gnome/glade.scm
%{_datadir}/guile-gnome-2/gnome/gw/libglade.scm
%{_datadir}/guile-gnome-2/gnome/gw/libglade-spec.scm
%{_datadir}/guile-gnome-2/gnome/overrides/libglade.defs
%{_infodir}/guile-gnome-libglade.info*

%if %{with gnome}
%files -n guile-gnome-libgnome
%defattr(644,root,root,755)
%doc libgnome/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-libgnome.so*
%{_datadir}/guile-gnome-2/gnome/gnome.scm
%{_datadir}/guile-gnome-2/gnome/gw/libgnome.scm
%{_datadir}/guile-gnome-2/gnome/gw/libgnome-spec.scm
%{_datadir}/guile-gnome-2/gnome/overrides/libgnome.defs
%{_infodir}/guile-gnome-libgnome.info*

%files -n guile-gnome-libgnomeui
%defattr(644,root,root,755)
%doc libgnomeui/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-libgnomeui.so*
%{_datadir}/guile-gnome-2/gnome/gnome-ui.scm
%{_datadir}/guile-gnome-2/gnome/gw/libgnomeui.scm
%{_datadir}/guile-gnome-2/gnome/gw/libgnomeui-spec.scm
%{_datadir}/guile-gnome-2/gnome/overrides/libgnomeui.defs*
%{_infodir}/guile-gnome-libgnomeui.info*
# libgnomeui-devel
%{_pkgconfigdir}/guile-gnome-libgnomeui-2.pc
%endif

%files -n guile-gnome-pango
%defattr(644,root,root,755)
%doc pango/{AUTHORS,ChangeLog,README}
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-pango.so*
%attr(755,root,root) %{_libdir}/guile-gnome-2/libgw-guile-gnome-pangocairo.so*
%{_datadir}/guile-gnome-2/gnome/pango.scm
%{_datadir}/guile-gnome-2/gnome/pangocairo.scm
%{_datadir}/guile-gnome-2/gnome/gw/pango.scm
%{_datadir}/guile-gnome-2/gnome/gw/pango-spec.scm
%{_datadir}/guile-gnome-2/gnome/gw/pangocairo.scm
%{_datadir}/guile-gnome-2/gnome/gw/pangocairo-spec.scm
%{_datadir}/guile-gnome-2/gnome/overrides/pango.defs*
%{_datadir}/guile-gnome-2/gnome/overrides/pangocairo.defs*
%{_infodir}/guile-gnome-pango.info*
%{_infodir}/guile-gnome-pangocairo.info*
