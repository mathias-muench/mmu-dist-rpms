%undefine _disable_source_fetch

Name:          k9s-dist
Version:       0.32.4
Release:       3%{?dist}
Summary:       Kubernetes CLI To Manage Your Clusters In Style!
License:       ASL 2.0
URL:           https://github.com/derailed/k9s/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      k9s

Source:        https://github.com/derailed/k9s/releases/download/v%{version}/k9s_Linux_amd64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -m 0755 -D k9s %{buildroot}%{_bindir}/k9s
%{__install} -D LICENSE %{buildroot}%{_docdir}/k9s/LICENSE
%{__install} -D README.md %{buildroot}%{_docdir}/k9s/README.md

%files
%defattr (-, root, root, 755)
%{_bindir}/k9s
%doc %{_docdir}/k9s/LICENSE
%doc %{_docdir}/k9s/README.md

%changelog
* Thu Jun 06 2024 Mathias Muench <Mathias.Muench@de.bosch.com> - 0.32.4-3
- rebuilt

* Thu Jun 06 2024 Mathias Muench <Mathias.Muench@de.bosch.com> - 0.32.4-2
- rebuilt

