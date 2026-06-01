Name:          kubeconform-dist
Version:       0.7.0
Release:       1%{?dist}
Summary:       A FAST Kubernetes manifests validator, with support for Custom Resources! 
License:       Apache-2.0
URL:           https://github.com/yannh/kubeconform/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      kubeconform

Source:        https://github.com/yannh/kubeconform/releases/download/v%{version}/kubeconform-linux-amd64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -m 0755 -D kubeconform %{buildroot}%{_bindir}/kubeconform
%{__install} -m 0644 -D LICENSE %{buildroot}%{_docdir}/kubeconform/LICENSE

%files
%defattr (-, root, root, 755)
%{_bindir}/kubeconform
%doc %{_docdir}/kubeconform/LICENSE

%changelog
* Wed Dec 17 2025 Mathias Muench <mathias-muench@users.noreply.github.com> - 0.7.0-1
- rebuilt

