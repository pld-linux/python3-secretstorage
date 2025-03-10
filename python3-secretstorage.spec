#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (require dbus stub or some Secret Service daemon running, e.g. GNOME Keyring)

Summary:	Python 3 bindings to Freedesktop.org Secret Service API
Summary(pl.UTF-8):	Wiązania Pythona 3 do API Secret Service z Freedesktop.org
Name:		python3-secretstorage
Version:	3.3.3
Release:	2
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/secretstorage/
Source0:	https://files.pythonhosted.org/packages/source/S/SecretStorage/SecretStorage-%{version}.tar.gz
# Source0-md5:	c6ff1cc866d2f1d274b75c6490726b1b
URL:		https://github.com/mitya57/secretstorage
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:30.3
%if %{with doc}
BuildRequires:	python3-Sphinx
%endif
%if %{with tests}
BuildRequires:	dbus
BuildRequires:	python3-cryptography >= 2.0
BuildRequires:	python3-jeepney >= 0.6
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
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
dbus-run-session -- %{__python3} -m unittest discover -s tests
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
