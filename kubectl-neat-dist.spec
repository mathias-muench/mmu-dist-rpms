%undefine _disable_source_fetch

Name:          kubectl-neat-dist
Version:       2.0.3
Release:       0%{?dist}
Summary:       A Kubernetes controller and tool for one-way encrypted Secrets
License:       ASL 2.0
URL:           https://github.com/itaysk/kubectl-neat/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      kubectl-neat

Source:        https://github.com/itaysk/kubectl-neat/releases/download/v%{version}/kubectl-neat_linux_amd64.tar.gz

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -m 0755 -D kubectl-neat %{buildroot}%{_bindir}/kubectl-neat
%{__install} -D LICENSE %{buildroot}%{_docdir}/kubectl-neat/LICENSE

%files
%defattr (-, root, root, 755)
%{_bindir}/kubectl-neat
%doc %{_docdir}/kubectl-neat/LICENSE
