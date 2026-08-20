%undefine _disable_source_fetch

Name:          eksctl-dist
Version:       0.230.0
Release:       1%{?dist}
Summary:       The official CLI for Amazon EKS 
License:       ASL 2.0
URL:           https://github.com/eksctl-io/eksctl/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      eksctl

Source:        https://github.com/eksctl-io/eksctl/releases/download/v%{version}/eksctl_Linux_amd64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%build
./eksctl completion bash > eksctl.bash-completion

%install
%{__install} -m 0755 -D eksctl %{buildroot}%{_bindir}/eksctl
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
%{__install} -m 0644 -D eksctl.bash-completion %{buildroot}%{_datarootdir}/bash-completion/completions/eksctl

%files
%defattr (-, root, root, 755)
%{_bindir}/eksctl
%{_datarootdir}/bash-completion/completions/eksctl

%changelog
* Thu Aug 20 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 0.230.0-1
- Update to 0.230.0

* Wed Jul 29 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 0.229.0-7
- Generate bash completion in %build phase

* Fri Sep 08 2023 Mathias Muench <mathias-muench@users.noreply.github.com> - 0.156.0-6
- rebuilt

