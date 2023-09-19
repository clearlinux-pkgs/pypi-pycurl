#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-pycurl
Version  : 7.45.2
Release  : 98
URL      : https://files.pythonhosted.org/packages/a8/af/24d3acfa76b867dbd8f1166853c18eefc890fc5da03a48672b38ea77ddae/pycurl-7.45.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/a8/af/24d3acfa76b867dbd8f1166853c18eefc890fc5da03a48672b38ea77ddae/pycurl-7.45.2.tar.gz
Summary  : PycURL -- A Python Interface To The cURL library
Group    : Development/Tools
License  : LGPL-2.1 MIT
Requires: pypi-pycurl-license = %{version}-%{release}
Requires: pypi-pycurl-python = %{version}-%{release}
Requires: pypi-pycurl-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : curl
BuildRequires : curl-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libidn)
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
PycURL -- A Python Interface To The cURL library
================================================

%package doc
Summary: doc components for the pypi-pycurl package.
Group: Documentation

%description doc
doc components for the pypi-pycurl package.


%package license
Summary: license components for the pypi-pycurl package.
Group: Default

%description license
license components for the pypi-pycurl package.


%package python
Summary: python components for the pypi-pycurl package.
Group: Default
Requires: pypi-pycurl-python3 = %{version}-%{release}

%description python
python components for the pypi-pycurl package.


%package python3
Summary: python3 components for the pypi-pycurl package.
Group: Default
Requires: python3-core
Provides: pypi(pycurl)

%description python3
python3 components for the pypi-pycurl package.


%prep
%setup -q -n pycurl-7.45.2
cd %{_builddir}/pycurl-7.45.2
pushd ..
cp -a pycurl-7.45.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695153936
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build  --with-openssl

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build  --with-openssl

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pycurl
cp %{_builddir}/pycurl-%{version}/COPYING-LGPL %{buildroot}/usr/share/package-licenses/pypi-pycurl/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
cp %{_builddir}/pycurl-%{version}/COPYING-MIT %{buildroot}/usr/share/package-licenses/pypi-pycurl/dc04ce10edbb511f5111a0c65eb5a3e23c8fe681 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/pycurl/AUTHORS
/usr/share/doc/pycurl/COPYING-LGPL
/usr/share/doc/pycurl/COPYING-MIT
/usr/share/doc/pycurl/ChangeLog
/usr/share/doc/pycurl/INSTALL.rst
/usr/share/doc/pycurl/README.rst
/usr/share/doc/pycurl/RELEASE-NOTES.rst
/usr/share/doc/pycurl/examples/basicfirst.py
/usr/share/doc/pycurl/examples/file_upload.py
/usr/share/doc/pycurl/examples/linksys.py
/usr/share/doc/pycurl/examples/multi-socket_action-select.py
/usr/share/doc/pycurl/examples/opensocketexception.py
/usr/share/doc/pycurl/examples/quickstart/file_upload_buffer.py
/usr/share/doc/pycurl/examples/quickstart/file_upload_real.py
/usr/share/doc/pycurl/examples/quickstart/file_upload_real_fancy.py
/usr/share/doc/pycurl/examples/quickstart/follow_redirect.py
/usr/share/doc/pycurl/examples/quickstart/form_post.py
/usr/share/doc/pycurl/examples/quickstart/get.py
/usr/share/doc/pycurl/examples/quickstart/get_python2.py
/usr/share/doc/pycurl/examples/quickstart/get_python2_https.py
/usr/share/doc/pycurl/examples/quickstart/get_python3.py
/usr/share/doc/pycurl/examples/quickstart/get_python3_https.py
/usr/share/doc/pycurl/examples/quickstart/put_buffer.py
/usr/share/doc/pycurl/examples/quickstart/put_file.py
/usr/share/doc/pycurl/examples/quickstart/response_headers.py
/usr/share/doc/pycurl/examples/quickstart/response_info.py
/usr/share/doc/pycurl/examples/quickstart/write_file.py
/usr/share/doc/pycurl/examples/retriever-multi.py
/usr/share/doc/pycurl/examples/retriever.py
/usr/share/doc/pycurl/examples/sfquery.py
/usr/share/doc/pycurl/examples/smtp.py
/usr/share/doc/pycurl/examples/ssh_keyfunction.py
/usr/share/doc/pycurl/examples/xmlrpc_curl.py

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pycurl/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/pypi-pycurl/dc04ce10edbb511f5111a0c65eb5a3e23c8fe681

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
