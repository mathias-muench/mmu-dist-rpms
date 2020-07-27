%undefine _disable_source_fetch

%global dist_name apache-maven
%global maven_home /opt/apache-maven

Name:          apache-maven-dist
Version:       3.6.1
Release:       7%{?dist}
Summary:       Java project management and project comprehension tool

License:       ASL 2.0
URL:           https://maven.apache.org/download.cgi

ExclusiveOS:   linux
ExclusiveArch: x86_64
AutoReqProv:   no

Source:        https://archive.apache.org/dist/maven/maven-3/%{version}/binaries/apache-maven-%{version}-bin.tar.gz

Prefix:        /opt

Requires:      java

Provides:      %{dist_name} %{dist_name}-%{version}

%description
%{summary}

%prep
%setup -q -n %{dist_name}-%{version}

%install
%{__mkdir_p} %{buildroot}%{maven_home}
%{__cp} -R ./ %{buildroot}%{maven_home}

%{__mkdir_p} %{buildroot}%{_sysconfdir}/profile.d/
%{__cat} <<\EOF >%{buildroot}%{_sysconfdir}/profile.d/maven.sh
export M2_HOME=%{maven_home}
export M2=%{maven_home}/bin
export PATH=$PATH:%{maven_home}/bin
EOF

%files
%defattr(-,root,root,0755)
%doc %{maven_home}/LICENSE
%doc %{maven_home}/NOTICE
%doc %{maven_home}/README.txt
%{maven_home}/bin
%{maven_home}/boot
%config %{maven_home}/conf
%{maven_home}/lib
%{_sysconfdir}/profile.d/maven.sh
