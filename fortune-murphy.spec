%define base_name	murphy
%define name		fortune-%{base_name}
%define version		1.0
%define release		14

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Quotes from Murphy's laws
License:	GPL
Group:		Toys
Url:		https://lis.snv.jussieu.fr/~rousse/linux
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0-13mdv2011.0
+ Revision: 618335
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.0-12mdv2010.0
+ Revision: 428880
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.0-11mdv2009.0
+ Revision: 245328
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-9mdv2008.1
+ Revision: 132426
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import fortune-murphy


* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-8mdv2007.0
- %%mkrel

* Fri Aug 19 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-7mdk
- rebuild 
- spec cleanup

* Thu Aug 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0-6mdk 
- fix spec encoding (tvignaud@mandrakesoft.com)

* Wed Jul 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0-5mdk 
- rebuild

* Sat Feb 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.0-4mdk
- rebuild

* Sat Jan 04 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0-3mdk
- rebuild

* Fri Nov 02 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0-2mdk
- moved files to %%{_gamesdatadir}/fortunes

* Thu Nov 01 2001 Guillaume Rousse <g.rousse@linux-mandrake.com> 1.0-1mdk 
- first Mandrake release
