%undefine _disable_source_fetch

Name:          bun-dist
Version:       1.4.2
Release:       1%{?dist}
Summary:       Bun is a fast JavaScript runtime, package manager, bundler, and test runner
License:       MIT
URL:           https://github.com/oven-sh/bun/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      bun

Source:        https://github.com/oven-sh/bun/releases/download/bun-v%{version}/bun-linux-x64.zip

%define __spec_install_post %{nil}
%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -C

%build
./bun completions bash > bun.bash-completion

%install
%{__install} -m 0755 -D bun %{buildroot}%{_bindir}/bun
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
%{__install} -m 0644 -D bun.bash-completion %{buildroot}%{_datarootdir}/bash-completion/completions/bun

%files
%defattr (-, root, root, 755)
%{_bindir}/bun
%{_datarootdir}/bash-completion/completions/bun

%changelog
* Sat Sep 05 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 1.4.2-1
- Initial package
