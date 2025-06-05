%undefine _disable_source_fetch

Name:          yamlfmt-dist
Version:       0.17.0
Release:       1%{?dist}
Summary:       An extensible command line tool or library to format yaml files.
License:       ASL 2.0
URL:           https://github.com/google/yamlfmt/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      yamlfmt

Source:        https://github.com/google/yamlfmt/releases/download/v%{version}/yamlfmt_%{version}_Linux_x86_64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -m 0755 -D yamlfmt %{buildroot}%{_bindir}/yamlfmt
%{__install} -D LICENSE %{buildroot}%{_docdir}/yamlfmt/LICENSE
%{__install} -D README.md %{buildroot}%{_docdir}/yamlfmt/README.md

%files
%defattr (-, root, root, 755)
%{_bindir}/yamlfmt
%doc %{_docdir}/yamlfmt/LICENSE
%doc %{_docdir}/yamlfmt/README.md

%changelog
* Fri Mar 22 2024 Mathias Muench <Mathias.Muench@de.bosch.com> - 0.11.0-1
- rebuilt

