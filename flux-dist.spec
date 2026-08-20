%undefine _disable_source_fetch

Name:          flux-dist
Version:       2.9.4
Release:       1%{?dist}
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

%build
./flux completion bash > flux.bash-completion

%install
%{__install} -m 0755 -D flux %{buildroot}%{_bindir}/flux
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
%{__install} -m 0644 -D flux.bash-completion %{buildroot}%{_datarootdir}/bash-completion/completions/flux

%files
%defattr (-, root, root, 755)
%{_bindir}/flux
%{_datarootdir}/bash-completion/completions/flux

%changelog
* Thu Aug 20 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 2.9.4-1
- Update to 2.9.4

* Wed Jul 29 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 2.9.3-3
- Generate bash completion in %build phase

* Wed Jul 29 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 2.9.3-2
- Update to 2.9.3

* Mon Jul 20 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 2.9.2-1
- update to 2.9.2
* Fri Sep 08 2023 Mathias Muench <mathias-muench@users.noreply.github.com> - 2.1.0-2
- rebuilt

