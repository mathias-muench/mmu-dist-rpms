%undefine _disable_source_fetch

Name:          kubeseal-dist
Version:       0.38.4
Release:       5%{?dist}
Summary:       A Kubernetes controller and tool for one-way encrypted Secrets
License:       Apache-2.0
URL:           https://github.com/bitnami/sealed-secrets/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      kubeseal

Source:        https://github.com/bitnami/sealed-secrets/releases/download/v%{version}/kubeseal-%{version}-linux-amd64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -D kubeseal %{buildroot}%{_bindir}/kubeseal
%{__install} -m 0644 -D LICENSE %{buildroot}%{_docdir}/kubeseal/LICENSE
%{__install} -m 0644 -D README.md %{buildroot}%{_docdir}/kubeseal/README.md

%files
%defattr (-, root, root, 755)
%{_bindir}/kubeseal
%doc %{_docdir}/kubeseal/LICENSE
%doc %{_docdir}/kubeseal/README.md

%changelog
* Thu Jul 09 2026 Mathias Muench <mathias-muench@users.noreply.github.com> - 0.38.4-5
- Update to new upstream version 0.38.4
- Update URL/Source: repo moved from bitnami-labs/sealed-secrets to bitnami/sealed-secrets

* Wed Dec 17 2025 Mathias Muench <mathias-muench@users.noreply.github.com> - 0.33.1-4
- rebuilt

* Fri Sep 08 2023 Mathias Muench <mathias-muench@users.noreply.github.com> - 0.23.1-3
- rebuilt

