%define module pip-requirements-parser
%define oname pip_requirements_parser

Name:		python-pip-requirements-parser
Version:	32.0.1
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
Summary:	pip requirements parser - a mostly correct pip requirements parsing library because it uses
URL:		https://pypi.org/project/pip-requirements-parser/
License:	MIT
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
Provides:  python%{pyver}dist(pip-requirements-parser) = %{version}-%{release}
%description
pip requirements parser - a mostly correct pip requirements parsing library because it uses pip's own code.

%files
%{py_sitedir}/%{oname}.py
%{py_sitedir}/packaging_legacy_version.py
%{py_sitedir}/__pycache__/*
%{py_sitedir}/%{oname}-%{version}.dist-info
