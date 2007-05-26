#
# Conditional build:
%bcond_without	gnome	# GNOME components (corba/bonobo, gnome-vfs, libgnome, libgnomeui)
#
Summary:	guile-gnome platform
Summary(pl.UTF-8):	Platforma guile-gnome
Name:		guile-gnome-platform
Version:	2.15.92
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.gnu.org/pub/gnu/guile-gnome/guile-gnome-platform/%{name}-%{version}.tar.gz
# Source0-md5:	936c25bab46578b4b55cf755ace6582d
Patch0:		%{name}-info.patch
URL:		http://www.gnu.org/software/guile-gnome/
BuildRequires:	GConf2-devel >= 2.18
BuildRequires:	atk-devel >= 1:1.12
BuildRequires:	g-wrap-devel >= 2:1.9.8
BuildRequires:	glib2-devel >= 1:2.10.0
%{?with_gnome:BuildRequires:	gnome-vfs2-devel >= 2.16.0}
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	guile-cairo-devel
BuildRequires:	guile-devel >= 5:1.6.4
%{?with_gnome:BuildRequires:	libbonobo-devel >= 2.0}
BuildRequires:	libglade2-devel >= 1:2.6
%{?with_gnome:BuildRequires:	libgnome-devel >= 2.16}
BuildRequires:	libgnomecanvas-devel >= 2.14
%{?with_gnome:BuildRequires:	libgnomeui-devel >= 2.16.0}
BuildRequires:	pango-devel >= 1:1.14
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	texinfo
Requires:	guile >= 5:1.6.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The guile-gnome project brings the power of Scheme to your graphical
application. guile-gnome modules support the entire Gnome library
stack: from Pango to GnomeCanvas, Gtk+ to GStreamer, Glade to
GtkSourceView, you will find in guile-gnome a comprehensive
environment for developing modern applications.

#%description -l pl.UTF-8

%package devel
Summary:	Development files for guile-gnome platform
Summary(pl.UTF-8):	Pliki programistyczne platformy guile-gnome
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for guile-gnome platform.

%description devel -l pl.UTF-8
Pliki programistyczne platformy guile-gnome.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/guile-gnome-0
%dir %{_datadir}/guile-gnome-0/gnome
%{_datadir}/guile-gnome-0/gnome/defs
%dir %{_datadir}/guile-gnome-0/gnome/gw
%dir %{_datadir}/guile-gnome-0/gnome/overrides
%{_infodir}/guile-gnome-tutorial.info*
# devel
%{_pkgconfigdir}/guile-gnome-defs-0.pc

# atk
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-atk.so*
%doc atk/{AUTHORS,ChangeLog,NEWS,README}
%{_datadir}/guile-gnome-0/gnome/atk.scm
%{_datadir}/guile-gnome-0/gnome/gw/atk.scm
%{_datadir}/guile-gnome-0/gnome/gw/atk-spec.scm
#%{_datadir}/guile-gnome-0/gnome/overrides/atk.defs

# cairo
%doc cairo/{AUTHORS,ChangeLog,NEWS,README}
%{_datadir}/guile-gnome-0/gnome/cairo.scm
%{_datadir}/guile-gnome-0/gnome/gw/cairo-spec.scm
# cairo-devel
#%{_pkgconfigdir}/guile-gnome-cairo.pc

# canvas
%doc libgnomecanvas/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-canvas.so*
%{_datadir}/guile-gnome-0/gnome/canvas.scm
%{_datadir}/guile-gnome-0/gnome/gw/canvas.scm
%{_datadir}/guile-gnome-0/gnome/gw/canvas-spec.scm
%{_datadir}/guile-gnome-0/gnome/overrides/libgnomecanvas.defs

%if %{with gnome}
# corba
%doc corba/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-corba.so*
%{_datadir}/guile-gnome-0/gnome/corba.scm
%{_datadir}/guile-gnome-0/gnome/corba
%{_datadir}/guile-gnome-0/gnome/gw/corba-spec.scm

# corba-devel
%{_includedir}/guile-gnome-0/guile-gnome-corba
%endif

# gconf
%doc gconf/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-gconf.so*
%{_datadir}/guile-gnome-0/gnome/gconf.scm
%{_datadir}/guile-gnome-0/gnome/gw/gconf.scm
%{_datadir}/guile-gnome-0/gnome/gw/gconf-spec.scm
%{_datadir}/guile-gnome-0/gnome/overrides/gconf.defs*

# glib
%doc glib/{AUTHORS,ChangeLog,NEWS*,README,REFCOUNTING,TODO,WARTS}
%attr(755,root,root) %{_bindir}/guile-gnome-0
%attr(755,root,root) %{_libdir}/libguile-gnome-gobject-0.so.*.*.*
%dir %{_libdir}/guile-gnome-0
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-glib.so*
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-gobject.so*
%{_datadir}/guile/site/gnome-0.scm
%{_datadir}/guile-gnome-0/gnome/glib.scm
%{_datadir}/guile-gnome-0/gnome/gobject.scm
%{_datadir}/guile-gnome-0/gnome/gobject
%{_datadir}/guile-gnome-0/gnome/gw/generics.scm
%{_datadir}/guile-gnome-0/gnome/gw/glib.scm
%{_datadir}/guile-gnome-0/gnome/gw/glib-spec.scm
%{_datadir}/guile-gnome-0/gnome/gw/gobject.scm
%{_datadir}/guile-gnome-0/gnome/gw/gobject-spec.scm
%{_datadir}/guile-gnome-0/gnome/gw/support
%{_datadir}/guile-gnome-0/gnome/overrides/glib.defs*

# glib-devel
%attr(755,root,root) %{_libdir}/libguile-gnome-gobject-0.so
%{_libdir}/libguile-gnome-gobject-0.la
%dir %{_includedir}/guile-gnome-0
%{_includedir}/guile-gnome-0/guile-gnome-gobject.h
%{_includedir}/guile-gnome-0/guile-gnome-gobject
%{_pkgconfigdir}/guile-gnome-glib-0.pc

%if %{with gnome}
# gnome-vfs
%doc gnome-vfs/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-gnome-vfs.so*
%{_datadir}/guile-gnome-0/gnome/vfs.scm
%{_datadir}/guile-gnome-0/gnome/gw/gnome-vfs-spec.scm
%{_datadir}/guile-gnome-0/gnome/overrides/gnome-vfs.defs*
%endif

# gtk
%doc gtk/{AUTHORS,ChangeLog,NEWS,README,TODO}
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-gdk.so*
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-gtk.so*
%{_datadir}/guile-gnome-0/gnome/contrib
%{_datadir}/guile-gnome-0/gnome/gtk.scm
%{_datadir}/guile-gnome-0/gnome/gtk
%{_datadir}/guile-gnome-0/gnome/gw/gdk.scm
%{_datadir}/guile-gnome-0/gnome/gw/gdk-spec.scm
%{_datadir}/guile-gnome-0/gnome/gw/gtk.scm
%{_datadir}/guile-gnome-0/gnome/gw/gtk-spec.scm
%{_datadir}/guile-gnome-0/gnome/overrides/gdk.defs*
%{_datadir}/guile-gnome-0/gnome/overrides/gdk-pixbuf.defs
%{_datadir}/guile-gnome-0/gnome/overrides/gtk.defs*
%{_datadir}/guile-gnome-0/gnome/overrides/gtk-customs.defs

# gtk-devel
%{_pkgconfigdir}/guile-gnome-gtk-0.pc

# libglade
%doc libglade/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-libglade.so*
%{_datadir}/guile-gnome-0/gnome/glade.scm
%{_datadir}/guile-gnome-0/gnome/gw/libglade.scm
%{_datadir}/guile-gnome-0/gnome/gw/libglade-spec.scm
%{_datadir}/guile-gnome-0/gnome/overrides/libglade.defs

%if %{with gnome}
# libgnome
%doc libgnome/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-libgnome.so*
%{_datadir}/guile-gnome-0/gnome/gnome.scm
%{_datadir}/guile-gnome-0/gnome/gw/libgnome-spec.scm
%{_datadir}/guile-gnome-0/gnome/overrides/libgnome.defs

# libgnomeui
%doc libgnomeui/{AUTHORS,ChangeLog,NEWS,README}
%{_datadir}/guile-gnome-0/gnome/gnome-ui.scm
%{_datadir}/guile-gnome-0/gnome/gw/libgnomeui-spec.scm
%{_datadir}/guile-gnome-0/gnome/overrides/libgnomeui.defs*
# libgnomeui-devel
%{_pkgconfigdir}/guile-gnome-libgnomeui.pc
%endif

# pango
%doc pango/{AUTHORS,ChangeLog,NEWS,README}
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-pango.so*
%attr(755,root,root) %{_libdir}/guile-gnome-0/libgw-guile-gnome-pangocairo.so*
%{_datadir}/guile-gnome-0/gnome/pango.scm
%{_datadir}/guile-gnome-0/gnome/gw/pango.scm
%{_datadir}/guile-gnome-0/gnome/gw/pango-spec.scm
%{_datadir}/guile-gnome-0/gnome/gw/pangocairo.scm
%{_datadir}/guile-gnome-0/gnome/gw/pangocairo-spec.scm
%{_datadir}/guile-gnome-0/gnome/overrides/pango.defs*
%{_datadir}/guile-gnome-0/gnome/overrides/pangocairo.defs*
