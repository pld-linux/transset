Summary:	Simple program to toggle Translucency property
Summary(pl):	Program do w³±czania przezroczysto¶ci
Name:		transset
Version:	040915
Release:	1
License:	GPL
Group:		X11	
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	49aacd06de18eddd31d85e15de54a465
URL:		http://freedesktop.org/cgi-bin/viewcvs.cgi/xapps/transset/
BuildRequires:	X11-devel >= 1:6.8.0
BuildRequires:	pkgconfig
Requires:	X11-libs >= 1:6.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		%{_usr}/X11R6

%description
Simple program to toggle Translucency property.

%description -l pl
Program do w³±czania przezroczysto¶ci.

%prep
%setup -q -n %{name}

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install transset $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
