Name:          sops-dist
Version:       3.13.1
Release:       1%{?dist}
Summary:       Simple and flexible tool for managing secrets
License:       MPL-2.0
URL:           https://github.com/getsops/sops/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      sops

Source0:       https://github.com/getsops/sops/releases/download/v%{version}/sops-v%{version}.linux.amd64

%define __spec_install_post %{nil}
%global debug_package %{nil}

%description
%{summary}

%prep

%install
%{__install} -m 0755 -D %{SOURCE0} %{buildroot}%{_bindir}/sops

%files
%defattr (-, root, root, 755)
%{_bindir}/sops

%changelog
* Mon Jun 01 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 3.13.1-1
- rebuilt

