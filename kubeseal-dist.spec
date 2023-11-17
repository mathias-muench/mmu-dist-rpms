%undefine _disable_source_fetch

Name:          kubeseal-dist
Version:       0.24.4
Release:       3%{?dist}
Summary:       A Kubernetes controller and tool for one-way encrypted Secrets
License:       ASL 2.0
URL:           https://github.com/bitnami-labs/sealed-secrets/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      kubeseal

Source:        https://github.com/bitnami-labs/sealed-secrets/releases/download/v%{version}/kubeseal-%{version}-linux-amd64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -m 0755 -D kubeseal %{buildroot}%{_bindir}/kubeseal
%{__install} -D LICENSE %{buildroot}%{_docdir}/kubeseal/LICENSE
%{__install} -D README.md %{buildroot}%{_docdir}/kubeseal/README.md

%files
%defattr (-, root, root, 755)
%{_bindir}/kubeseal
%doc %{_docdir}/kubeseal/LICENSE
%doc %{_docdir}/kubeseal/README.md

%changelog
* Fri Sep 08 2023 Mathias Muench <Mathias.Muench@de.bosch.com> - 0.23.1-3
- rebuilt

