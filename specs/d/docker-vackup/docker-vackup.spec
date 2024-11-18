
%global commit 2a8a73136302af0bebeb7f210fc14be868ab2958
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: docker-vackup
Version: 0
Release: 1.20241102git
License: Public Domain
URL: https://github.com/BretFisher/docker-vackup 
Source: docker-vackup-%{commit}.tar.gz
BuildArch: noarch
Requires: bash

Summary: Backup and Restore Docker Volumes

%description
Vackup: (contraction of "volume backup")

Easily backup and restore Docker volumes using either tarballs or container images. 
It's designed for running from any host/container where you have the docker CLI.

Note that for open files like databases, it's usually better to use their preferred 
backup tool to create a backup file, but if you stored that file on a Docker volume, 
this could still be a way you get the Docker volume into a image or tarball for 
moving to remote storage for safe keeping.

%prep
%autosetup -n %{name}-%{commit} 

%build

%install
install -d %{buildroot}%{_bindir}
install -m 0755 vackup %{buildroot}%{_bindir}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/vackup

%changelog
* Mon Nov 18 2024 IWAI, Masaharu <iwaim.sub@gmail.com> - 1-0.20241102git
- fix License tag

* Sun Nov 17 2024 IWAI, Masaharu <iwaim.sub@gmail.com> - 0-0.20241102git
- initial release

