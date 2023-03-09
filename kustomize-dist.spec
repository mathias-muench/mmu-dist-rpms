%undefine _disable_source_fetch

Name:          kustomize-dist
Version:       5.0.0
Release:       0%{?dist}
Summary:       The official CLI for Amazon EKS 
License:       ASL 2.0
URL:           https://github.com/kubernetes-sigs/kustomize/releases

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      kustomize

Source:        https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize/v%{version}/kustomize_v%{version}_linux_amd64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -m 0755 -D kustomize %{buildroot}%{_bindir}/kustomize
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
echo 'eval "$(kustomize completion bash)"' >%{buildroot}%{_datarootdir}/bash-completion/completions/kustomize

%files
%defattr (-, root, root, 755)
%{_bindir}/kustomize
%{_datarootdir}/bash-completion/completions/kustomize
