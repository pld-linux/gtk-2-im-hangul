Summary:	Input module of GTK+ 2.x for Korean using Hangul engine
Summary(pl.UTF-8):	Moduł wejściowy GTK+ 2.x dla języka koreańskiego wykorzystujący silnik Hangul
Name:		gtk+2-im-hangul
Version:	2.1.1
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
#Source0Download: https://github.com/choehwanjin/imhangul/releases
Source0:	https://github.com/choehwanjin/imhangul/archive/imhangul-%{version}.tar.gz
# Source0-md5:	225aa61d1f4ebb44ccd1eb8b824f8fbb
URL:		https://github.com/choehwanjin/imhangul
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	libhangul-devel >= 0.0.12
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
Requires(post,postun):	gtk+2 >= 2:2.10.0
Requires:	gtk+2 >= 2:2.10.0
Requires:	libhangul >= 0.0.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gtk2_immodules_dir	%{_libdir}/gtk-2.0/%(pkg-config --variable=gtk_binary_version gtk+-2.0)/immodules

%if "%{_lib}" != "lib"
%define		libext		%(lib="%{_lib}"; echo ${lib#lib})
%define		pqext		-%{libext}
%else
%define		pqext		%{nil}
%endif

%description
Input module of GTK+ 2.x for Korean using Hangul engine.

%description -l pl.UTF-8
Moduł wejściowy GTK+ 2.x dla języka koreańskiego wykorzystujący silnik
Hangul.

%prep
%setup -q -n imhangul-imhangul-%{version}

%build
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-gtk-im-module-dir=%{gtk2_immodules_dir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{gtk2_immodules_dir}/*.la

%find_lang im-hangul

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
%{_bindir}/gtk-query-immodules-2.0%{pqext} --update-cache
exit 0

%postun
umask 022
%{_bindir}/gtk-query-immodules-2.0%{pqext} --update-cache
exit 0

%files -f im-hangul.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README gtkrc imhangul.conf
%attr(755,root,root) %{gtk2_immodules_dir}/im-hangul.so
