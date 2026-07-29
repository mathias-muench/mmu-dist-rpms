%undefine _disable_source_fetch

Name:          cmctl-dist
Version:       2.5.0
Release:       2%{?dist}
Summary:       cmctl is the command line utility that makes cert-manager easier to use
License:       Apache-2.0
URL:           https://github.com/cert-manager/cmctl/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      cmctl

Source:        https://github.com/cert-manager/cmctl/releases/download/v%{version}/cmctl_linux_amd64.tar.gz

%define __spec_install_post %{nil}
%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%build
./cmctl completion bash > cmctl.bash-completion

%install
%{__install} -m 0755 -D cmctl %{buildroot}%{_bindir}/cmctl
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
%{__install} -m 0644 -D cmctl.bash-completion %{buildroot}%{_datarootdir}/bash-completion/completions/cmctl

%files
%defattr (-, root, root, 755)
%{_bindir}/cmctl
%{_datarootdir}/bash-completion/completions/cmctl

%changelog
* Wed Jul 29 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 2.5.0-2
- Generate bash completion in %build phase

* Sat Jul 11 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 2.5.0-1
- Initial package
