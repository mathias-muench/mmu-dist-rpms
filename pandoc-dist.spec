%undefine _disable_source_fetch

Name:          pandoc-dist
Version:       3.6.2
Release:       3%{?dist}
Summary:       Universal markup converter
License:       GPLv2+
URL:           https://github.com/jgm/pandoc/releases/latest

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Provides:      pandoc

Source:        https://github.com/jgm/pandoc/releases/download/%{version}/pandoc-%{version}-linux-amd64.tar.gz

%description
%{summary}

%prep
%setup -q -n pandoc-%{version}

%install
%{__install} -m 0755 -D bin/pandoc %{buildroot}%{_bindir}/pandoc
%{__install} -m 0644 -D share/man/man1/pandoc.1.gz %{buildroot}%{_mandir}/man1/pandoc.1.gz

%files
%defattr (-, root, root, 755)
%{_bindir}/pandoc
%doc %{_mandir}/man1/pandoc.1.gz

%changelog
* Fri Sep 08 2023 Mathias Muench <Mathias.Muench@de.bosch.com> - 3.1.7-3
- rebuilt

