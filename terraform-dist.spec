%undefine _disable_source_fetch

Name:          terraform-dist
Version:       0.15.0
Release:       1%{?dist}
Summary:       Terraform enables you to safely and predictably create, change, and improve infrastructure. It is an open source tool that codifies APIs into declarative configuration files that can be shared amongst team members, treated as code, edited, reviewed, and versioned.
License:       MPLv2.0
URL:           https://www.terraform.io/downloads.html

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      terraform

Source:        https://releases.hashicorp.com/terraform/%{version}/terraform_%{version}_linux_amd64.zip

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -m 0755 -D terraform %{buildroot}%{_bindir}/terraform

%files
%defattr (-, root, root, 755)
%{_bindir}/terraform
