# vim: filetype=spec :

%undefine _disable_source_fetch

Name:          pandoc-dist
Version:       2.9.2
Release:       0
Summary:       Universal markup converter
License:       GPLv2+
URL:           https://pandoc.org/

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
%{__install} -m 0755 -D bin/pandoc %{buildroot}%{_bindir}/pandoc-citeproc
%{__install} -m 0644 -D share/man/man1/pandoc.1.gz %{buildroot}%{_mandir}/man1/pandoc.1.gz
%{__install} -m 0644 -D share/man/man1/pandoc-citeproc.1.gz %{buildroot}%{_mandir}/man1/pandoc-citeproc.1.gz

%files
%defattr (-, root, root, 755)
%{_bindir}/pandoc
%{_bindir}/pandoc-citeproc
%doc %{_mandir}/man1/pandoc.1.gz
%doc %{_mandir}/man1/pandoc-citeproc.1.gz
