%undefine _disable_source_fetch

Name:          kubectl-neat-dist
Version:       2.0.4
Release:       1%{?dist}
Summary:       Clean up Kubernetes yaml and json output to make it readable 
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

%build
./kubectl-neat completion bash > kubectl-neat.bash-completion

%install
%{__install} -m 0755 -D kubectl-neat %{buildroot}%{_bindir}/kubectl-neat
%{__mkdir_p} %{buildroot}%{_datarootdir}/bash-completion/completions
%{__install} -m 0644 -D kubectl-neat.bash-completion %{buildroot}%{_datarootdir}/bash-completion/completions/kubectl-neat
%{__install} -D LICENSE %{buildroot}%{_docdir}/kubectl-neat/LICENSE

%files
%defattr (-, root, root, 755)
%{_bindir}/kubectl-neat
%{_datarootdir}/bash-completion/completions/kubectl-neat
%doc %{_docdir}/kubectl-neat/LICENSE
