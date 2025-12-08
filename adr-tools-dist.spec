%undefine _disable_source_fetch

Name:          adr-tools-dist
Version:       3.0.0
Release:       4%{?dist}
Summary:       Command-line tools for working with Architecture Decision Records 
License:       GPL-3.0-or-later
URL:           https://github.com/google/adr-tools/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      adr-tools

Source:        https://github.com/npryce/adr-tools/archive/refs/tags/%{version}.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -n adr-tools-%{version}

%build
make
cat <<EOF >adr.sh
#!/bin/sh
exec %{_libexecdir}/adr-tools/adr
EOF

%install
%{__install} -m 0755 -D -t %{buildroot}%{_libexecdir}/adr-tools/ src/adr src/adr-* src/_adr_*
%{__install} -m 0644 -D -t %{buildroot}%{_libexecdir}/adr-tools/ src/*.md
%{__install} -m 0755 -D adr.sh %{buildroot}%{_bindir}/adr
%{__install} -m 0644 -D -t %{buildroot}%{_docdir}/adr-tools/ *.txt *.md

%files
%defattr (-, root, root, 755)
%{_libexecdir}/adr-tools/
%{_bindir}/adr
%doc %{_docdir}/adr-tools/

%changelog
* Mon Dec 08 2025 mathias-muench <mathias-muench@users.noreply.github.com> - 3.0.0-4
- rebuilt

* Mon Dec 08 2025 mathias-muench <mathias-muench@users.noreply.github.com> - 3.0.0-2
- rebuilt

