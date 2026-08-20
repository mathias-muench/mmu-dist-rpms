%undefine _disable_source_fetch

Name:          copilot-dist
Version:       1.0.80
Release:       1%{?dist}
Summary:       GitHub Copilot CLI brings the power of Copilot coding agent directly to your terminal.
License:       Proprietary
URL:           https://github.com/github/copilot-cli/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      copilot

Source:        https://github.com/github/copilot-cli/releases/download/v%{version}/copilot-linux-x64.tar.gz

%define __spec_install_post %{nil}
%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%build
./copilot completion bash > copilot.bash-completion

%install
%{__install} -m 0755 -D copilot %{buildroot}%{_bindir}/copilot
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
%{__install} -m 0644 -D copilot.bash-completion %{buildroot}%{_datarootdir}/bash-completion/completions/copilot

%files
%defattr (-, root, root, 755)
%{_bindir}/copilot
%{_datarootdir}/bash-completion/completions/copilot

%changelog
* Thu Aug 20 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 1.0.80-1
- Update to 1.0.80

* Wed Jul 29 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 1.0.75-2
- Generate bash completion in %build phase

* Wed Jul 29 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 1.0.75-1
- Update to 1.0.75

* Mon Jul 20 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 1.0.71-1
- update to 1.0.71
* Fri May 29 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 1.0.55-1
- rebuilt

