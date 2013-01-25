%define	sname	wavelet-decompose

Summary:	Gimp plugin to decomposes a layer into layers of wavelet scales
Name:		gimp-plugin-%{sname}
Version:	0.1.2
Release:	1
Group:		Graphics
License:	GPLv2
Url:		http://registry.gimp.org/node/11742
Source:		http://registry.gimp.org/files/%{sname}-%{version}.tar.gz
BuildRequires:	pkgconfig(gimp-2.0)
Requires:	gimp

%description
This plugin losslessly decomposes a layer of an image into layers of wavelet
scales. This means that you can edit the image on different detail scales.
The trivial recomposition of the image can be done by GIMP's layer modes so
you can see the results of your modifications instantly.

Among the applications are:
 - retouching
 - noise reduction
 - enhancing global contrast

%prep
%setup -q -n %{sname}-%{version}
sed -i s,"install -v","install -D -v",g po/Makefile

%build
%make

%install
make -C po install LOCALEDIR=%{buildroot}%{_datadir}/locale
install -Dm 755 src/%{sname} %{buildroot}%{_libdir}/gimp/2.0/plug-ins/%{sname}

%find_lang gimp20-%{sname}-plug-in

%files -f gimp20-%{sname}-plug-in.lang
%doc COPYING AUTHORS ChangeLog THANKS README TRANSLATIONS
%{_libdir}/gimp/2.0/plug-ins/%{sname}

