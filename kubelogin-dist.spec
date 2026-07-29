%undefine _disable_source_fetch

Name:          kubelogin-dist
Version:       0.2.19
Release:       2%{?dist}
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

%build
./bin/linux_amd64/kubelogin completion bash > kubelogin.bash-completion

%install
%{__install} -m 0755 -D bin/linux_amd64/kubelogin %{buildroot}%{_bindir}/kubelogin
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
%{__install} -m 0644 -D kubelogin.bash-completion %{buildroot}%{_datarootdir}/bash-completion/completions/kubelogin

%files
%defattr (-, root, root, 755)
%{_bindir}/kubelogin
%{_datarootdir}/bash-completion/completions/kubelogin

%changelog
* Wed Jul 29 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 0.2.19-2
- Generate bash completion in %build phase

* Mon Dec 08 2025 Mathias Muench <mathias-muench@users.noreply.github.com> - 0.2.13-1
- rebuilt

