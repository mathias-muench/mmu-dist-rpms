%undefine _disable_source_fetch

%global dist_name idea-IC
%global idea_home /opt/idea-IC
%global idea_build 203.5981.155

Name:          idea-IC-dist
Version:       2020.3
Release:       0%{?dist}
Summary:       Intelligent Java IDE

License:       ASL 2.0
URL:           https://www.jetbrains.com/de-de/idea/download/

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Source:        https://download.jetbrains.com/idea/ideaIC-%{version}.tar.gz

Prefix:        /opt

Requires:      java

Provides:      %{dist_name}

%global debug_package %{nil}
%global __jar_repack %{nil}
%global __brp_mangle_shebangs %{nil}

%description
%{summary}

%prep
%setup -q -n %{dist_name}-%{idea_build}

%install
export QA_RPATHS=$(( 0x0004|0x0008 ))
%{__mkdir_p} %{buildroot}%{idea_home}
%{__cp} -R ./ %{buildroot}%{idea_home}

%{__mkdir_p} %{buildroot}%{_sysconfdir}/profile.d/
%{__cat} <<\EOF >%{buildroot}%{_sysconfdir}/profile.d/idea.sh
export PATH=$PATH:%{idea_home}/bin
EOF

%files
%defattr(-,root,root,0755)
%{idea_home}/bin
%doc %{idea_home}/build.txt
%doc %{idea_home}/Install-Linux-tar.txt
%{idea_home}/icons.db
%{idea_home}/jbr
%{idea_home}/lib
%doc %{idea_home}/license
%doc %{idea_home}/LICENSE.txt
%doc %{idea_home}/NOTICE.txt
%{idea_home}/plugins
%{idea_home}/product-info.json
%{idea_home}/redist
%{_sysconfdir}/profile.d/idea.sh
