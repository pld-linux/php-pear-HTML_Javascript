%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Javascript
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - an interface for creating simple JS scripts
Summary(pl):	%{_class}_%{_subclass} - interfejs do tworzenia prostego JS
Name:		php-pear-%{_pearname}
Version:	0.9.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides an interface for creating simple JS scripts.

%description -l pl
Dostarcza interfejs do tworzenia prostego skryptów JavaScriptu.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
