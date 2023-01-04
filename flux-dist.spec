%undefine _disable_source_fetch

Name:          flux-dist
Version:       0.38.2
Release:       0%{?dist}
Summary:       The official CLI for Amazon EKS 
License:       ASL 2.0
URL:           https://github.com/fluxcd/flux2/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      flux

Source:        https://github.com/fluxcd/flux2/releases/download/v%{version}/flux_%{version}_linux_amd64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -m 0755 -D flux %{buildroot}%{_bindir}/flux
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
echo 'eval "$(flux completion bash)"' >%{buildroot}%{_datarootdir}/bash-completion/completions/flux

%files
%defattr (-, root, root, 755)
%{_bindir}/flux
%{_datarootdir}/bash-completion/completions/flux
