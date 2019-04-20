#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-asyncio
Version  : 0.10.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/dc/20/a35b6fbb9b97859ed2203ad474e4dd8591ef369b7387f6ef08270a0a3e84/pytest-asyncio-0.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/dc/20/a35b6fbb9b97859ed2203ad474e4dd8591ef369b7387f6ef08270a0a3e84/pytest-asyncio-0.10.0.tar.gz
Summary  : Pytest support for asyncio.
Group    : Development/Tools
License  : Apache-2.0
Requires: pytest-asyncio-license = %{version}-%{release}
Requires: pytest-asyncio-python = %{version}-%{release}
Requires: pytest-asyncio-python3 = %{version}-%{release}
Requires: pytest
BuildRequires : buildreq-distutils3
BuildRequires : pytest

%description
pytest-asyncio: pytest support for asyncio
==========================================

%package license
Summary: license components for the pytest-asyncio package.
Group: Default

%description license
license components for the pytest-asyncio package.


%package python
Summary: python components for the pytest-asyncio package.
Group: Default
Requires: pytest-asyncio-python3 = %{version}-%{release}

%description python
python components for the pytest-asyncio package.


%package python3
Summary: python3 components for the pytest-asyncio package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pytest-asyncio package.


%prep
%setup -q -n pytest-asyncio-0.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546957296
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-asyncio
cp LICENSE %{buildroot}/usr/share/package-licenses/pytest-asyncio/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-asyncio/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
