#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pytest-asyncio
Version  : 0.14.0
Release  : 16
URL      : https://files.pythonhosted.org/packages/65/09/9472d4db0625cf56d40f4e405f955faf6469be00858a273b71332f3fcd1f/pytest-asyncio-0.14.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/65/09/9472d4db0625cf56d40f4e405f955faf6469be00858a273b71332f3fcd1f/pytest-asyncio-0.14.0.tar.gz
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
Provides: pypi(pytest_asyncio)
Requires: pypi(pytest)

%description python3
python3 components for the pytest-asyncio package.


%prep
%setup -q -n pytest-asyncio-0.14.0
cd %{_builddir}/pytest-asyncio-0.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594825954
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pytest-asyncio
cp %{_builddir}/pytest-asyncio-0.14.0/LICENSE %{buildroot}/usr/share/package-licenses/pytest-asyncio/c700a8b9312d24bdc57570f7d6a131cf63d89016
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pytest-asyncio/c700a8b9312d24bdc57570f7d6a131cf63d89016

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
