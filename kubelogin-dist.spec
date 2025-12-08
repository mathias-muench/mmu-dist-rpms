%undefine _disable_source_fetch

Name:          kubelogin-dist
Version:       0.2.13
Release:       1%{?dist}
Summary:       A Kubernetes credential (exec) plugin implementing azure authentication 
License:       MIT
URL:           https://github.com/Azure/kubelogin/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      kubelogin

Source:        https://github.com/Azure/kubelogin/releases/download/v%{version}/kubelogin-linux-amd64.zip

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -m 0755 -D bin/linux_amd64/kubelogin %{buildroot}%{_bindir}/kubelogin

%files
%defattr (-, root, root, 755)
%{_bindir}/kubelogin

%changelog
* Mon Dec 08 2025 Mathias Muench <mathias-muench@users.noreply.github.com> - 0.2.13-1
- rebuilt

