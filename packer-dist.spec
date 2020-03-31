%undefine _disable_source_fetch

Name:          packer-dist
Version:       1.5.5
Release:       1
Summary:       Packer is a tool for creating identical machine images for multiple platforms from a single source configuration.
License:       MPLv2.0
URL:           https://www.packer.io/downloads.html

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      packer

Source:        https://releases.hashicorp.com/packer/%{version}/packer_%{version}_linux_amd64.zip

%description
%{summary}

%prep
%setup -q -c

%install
%{__install} -m 0755 -D packer %{buildroot}%{_bindir}/packer

%files
%defattr (-, root, root, 755)
%{_bindir}/packer
