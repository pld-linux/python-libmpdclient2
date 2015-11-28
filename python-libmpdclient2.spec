%define		module	libmpdclient2

Summary:	Python client library for MPD (Music Player Daemon)
Name:		python-%{module}
Version:	1.0
Release:	0.5
License:	public domain
Group:		Libraries/Python
Source0:	http://incise.org/files/dev/py-%{module}-%{version}.tgz
# Source0-md5:	fd04a669f25827386a29e842a4cbcefe
URL:		http://incise.org/py-libmpdclient2.html
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python client library for MPD (Music Player Daemon)

%prep
%setup -q -n py-%{module}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING.txt
%{py_sitescriptdir}/mpdclient2.py[co]
%{py_sitescriptdir}/*.egg-info
