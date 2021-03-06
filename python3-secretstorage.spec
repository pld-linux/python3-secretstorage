#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests [require dbus and some Secret Service daemon running]

Summary:	Python 3 bindings to Freedesktop.org Secret Service API
Summary(pl.UTF-8):	Wiązania Pythona 3 do API Secret Service z Freedesktop.org
Name:		python3-secretstorage
Version:	3.1.2
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/secretstorage/
Source0:	https://files.pythonhosted.org/packages/source/S/SecretStorage/SecretStorage-%{version}.tar.gz
# Source0-md5:	c2a8c0e08e5da198fc38c379b98c28f1
URL:		https://github.com/mitya57/secretstorage
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with doc}
BuildRequires:	python3-Sphinx
%endif
%if %{with tests}
BuildRequires:	python3-cryptography
BuildRequires:	python3-jeepney >= 0.4.2
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a way for securely storing passwords and other
secrets.

It uses D-Bus Secret Service API that is supported by GNOME Keyring
(since version 2.30) and KSecretsService.

%description -l pl.UTF-8
Ten moduł udostępnia sposób bezpiecznego przechowywania haseł i innych
tajnych danych.

Wykorzystuje API D-Bus Secret Service, obsługiwane przez GNOME Keyring
(od wersji 2.30) oraz KSecretsService.

%package apidocs
Summary:	secretstorage API documentation
Summary(pl.UTF-8):	Dokumentacja API secretstorage
Group:		Documentation

%description apidocs
API documentation for secretstorage.

%description apidocs -l pl.UTF-8
Dokumentacja API secretstorage.

%prep
%setup -q -n SecretStorage-%{version}

%build
%py3_build %{?with_doc:build_sphinx}

%if %{with tests}
# TODO: proper value
export DBUS_SESSION_BUS_ADDRESS=???
%{__python3} tests/run_tests.py
%endif

%install
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst changelog
%{py3_sitescriptdir}/secretstorage
%{py3_sitescriptdir}/SecretStorage-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc build-3/sphinx/html/{_static,*.html,*.js}
%endif
