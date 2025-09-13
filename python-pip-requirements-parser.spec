Name:		python-pip-requirements-parser
Version:	32.0.1
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/p/pip-requirements-parser/pip-requirements-parser-%{version}.tar.gz
Summary:	pip requirements parser - a mostly correct pip requirements parsing library because it uses
URL:		https://pypi.org/project/pip-requirements-parser/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch
Provides:  python3.11dist(pip-requirements-parser)=%{version}
%description
pip requirements parser - a mostly correct pip requirements parsing library because it uses pip's own code.

%files
%{py_sitedir}/pip_requirements_parser.py
%{py_sitedir}/packaging_legacy_version.py
%{py_sitedir}/__pycache__/pip_requirements_parser.cpython-311.pyc
%{py_sitedir}/__pycache__/packaging_legacy_version.cpython-311.pyc
%{py_sitedir}/pip_requirements_parser-*.*-info
