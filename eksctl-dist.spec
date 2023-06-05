%undefine _disable_source_fetch

Name:          eksctl-dist
Version:       0.143.0
Release:       4%{?dist}
Summary:       The official CLI for Amazon EKS 
License:       ASL 2.0
URL:           https://github.com/weaveworks/eksctl/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      eksctl

Source:        https://github.com/weaveworks/eksctl/releases/download/v%{version}/eksctl_Linux_amd64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -m 0755 -D eksctl %{buildroot}%{_bindir}/eksctl
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
echo 'eval "$(eksctl completion bash)"' >%{buildroot}%{_datarootdir}/bash-completion/completions/eksctl

%files
%defattr (-, root, root, 755)
%{_bindir}/eksctl
%{_datarootdir}/bash-completion/completions/eksctl
