%undefine _disable_source_fetch

Name:          opencode-dist
Version:       1.18.3
Release:       1%{?dist}
Summary:       OpenCode - The open source coding agent
License:       MIT
URL:           https://github.com/anomalyco/opencode/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      opencode

Source:        https://github.com/anomalyco/opencode/releases/download/v%{version}/opencode-linux-x64.tar.gz

%define __spec_install_post %{nil}
%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%build
./opencode completion bash > opencode.bash-completion

%install
%{__install} -m 0755 -D opencode %{buildroot}%{_bindir}/opencode
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
%{__install} -m 0644 -D opencode.bash-completion %{buildroot}%{_datarootdir}/bash-completion/completions/opencode

%files
%defattr (-, root, root, 755)
%{_bindir}/opencode
%{_datarootdir}/bash-completion/completions/opencode

%changelog
* Mon Jul 20 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 1.18.3-1
- Initial package
