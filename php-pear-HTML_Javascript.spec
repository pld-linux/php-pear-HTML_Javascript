%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Javascript
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an interface for creating simple JS scripts
Summary(pl.UTF-8):	%{_pearname} - interfejs do tworzenia prostego JS
Name:		php-pear-%{_pearname}
Version:	1.1.2
Release:	2
License:	PHP 3.0
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	be4770887ba2f727e1d40d709ec24678
URL:		http://pear.php.net/package/HTML_Javascript/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-HTML_Javascript-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides two classes:
- HTML_Javascript for performing basic JS operations
- HTML_Javascript_Convert for converting variables Allow output data
  to a file, to the standart output (print), or return.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
HTML_Javascript dostarcza dwie klasy:
- HTML_Javascript do wykonywania podstawowych operacji JavaScript
- HTML_Javascript_Convert do konwersji zmiennych Możliwe jest
  zapisanie wyniku do pliku, na standardowe wyjście (wypisanie) lub po
  prostu zwrócenie jako zmiennej.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
