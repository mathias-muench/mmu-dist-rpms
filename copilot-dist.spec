Name:          copilot-dist
Version:       1.0.55
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

%install
%{__install} -m 0755 -D copilot %{buildroot}%{_bindir}/copilot
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
echo 'eval "$(copilot completion bash)"' >%{buildroot}%{_datarootdir}/bash-completion/completions/copilot

%files
%defattr (-, root, root, 755)
%{_bindir}/copilot
%{_datarootdir}/bash-completion/completions/copilot

%changelog
* Fri May 29 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 1.0.55-1
- rebuilt

