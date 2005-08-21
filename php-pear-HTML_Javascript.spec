%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Javascript
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an interface for creating simple JS scripts
Summary(pl):	%{_pearname} - interfejs do tworzenia prostego JS
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	1
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5381cb0a53d8185b3a276daacb4f7655
URL:		http://pear.php.net/package/HTML_Javascript/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides two classes:
- HTML_Javascript for performing basic JS operations
- HTML_Javascript_Convert for converting variables
Allow output data to a file, to the standart output (print), or
return.

In PEAR status of this package is: %{_status}.

%description -l pl
HTML_Javascript dostarcza dwie klasy:
- HTML_Javascript do wykonywania podstawowych operacji JavaScript
- HTML_Javascript_Convert do konwersji zmiennych
Mo�liwe jest zapisanie wyniku do pliku, na standardowe wyj�cie
(wypisanie) lub po prostu zwr�cenie jako zmiennej.

Ta klasa ma w PEAR status: %{_status}.

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
