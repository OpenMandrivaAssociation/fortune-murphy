%define base_name	murphy
%define name		fortune-%{base_name}
%define version		1.0
%define release		%mkrel 8

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Quotes from Murphy's laws
License:	GPL
Group:		Toys
Url:		http://lis.snv.jussieu.fr/~rousse/linux
Source:		%{name}-%{version}.tar.bz2
Requires:	fortune-mod
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
This is a collection of more than 1250 Murphy's (& Al) laws, ignominously
stolen from the excellent Ultimate Collection of Murphy's Laws by Andreas Götz
(http://www.cpuidle.de/murphy.shtml), at format used by the good old fortune
command.

%prep
%setup -q

%build

%clean 
rm -rf %{buildroot}

%install
install -d -m 755 %{buildroot}%{_gamesdatadir}/fortunes
for file in data/*; do
  install -m 644 $file %{buildroot}%{_gamesdatadir}/fortunes/%{base_name}-`basename $file`
done

%files
%defattr(-,root,root)
%doc COPYING README
%{_gamesdatadir}/fortunes/*

