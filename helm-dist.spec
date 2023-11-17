%undefine _disable_source_fetch

Name:          helm-dist
Version:       3.13.2
Release:       1%{?dist}
Summary:       The official CLI for Amazon EKS 
License:       ASL 2.0
URL:           https://github.com/helm/helm/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      helm

Source:        https://get.helm.sh/helm-v%{version}-linux-amd64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -D linux-amd64/helm %{buildroot}%{_bindir}/helm
%{__install} -D linux-amd64/README.md %{buildroot}%{_docdir}/helm/README.md
%{__install} -D linux-amd64/LICENSE %{buildroot}%{_docdir}/helm/LICENSE
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
echo 'eval "$(helm completion bash)"' >%{buildroot}%{_datarootdir}/bash-completion/completions/helm

%files
%defattr (-, root, root, 755)
%{_bindir}/helm
%doc %{_docdir}/helm/README.md
%doc %{_docdir}/helm/LICENSE
%{_datarootdir}/bash-completion/completions/helm
