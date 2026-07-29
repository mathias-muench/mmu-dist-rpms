%undefine _disable_source_fetch

Name:          sops-dist
Version:       3.13.3
Release:       2%{?dist}
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

%build
%{__install} -m 0755 %{SOURCE0} ./sops
./sops completion bash > sops.bash-completion

%install
%{__install} -m 0755 -D %{SOURCE0} %{buildroot}%{_bindir}/sops
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
%{__install} -m 0644 -D sops.bash-completion %{buildroot}%{_datarootdir}/bash-completion/completions/sops

%files
%defattr (-, root, root, 755)
%{_bindir}/sops
%{_datarootdir}/bash-completion/completions/sops

%changelog
* Wed Jul 29 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 3.13.3-2
- Generate bash completion in %build phase

* Wed Jul 29 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 3.13.3-1
- Update to 3.13.3

* Mon Jun 01 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 3.13.1-1
- rebuilt

