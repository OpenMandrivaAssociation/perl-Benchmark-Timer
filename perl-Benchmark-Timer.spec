%define upstream_name    Benchmark-Timer
%define	upstream_version 0.7102

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6
Epoch:		1

Summary:	Benchmark::Timer - Perl code benchmarking tool
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Benchmark/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		Benchmark-Timer-fix-dep.patch

BuildRequires:	perl(Statistics::TTest)
BuildRequires:	perl-devel

BuildArch:	noarch

%description
The Benchmark::Timer class allows you to time portions of code
conveniently, as well as benchmark code by allowing timings of
repeated trials. It is perfect for when you need more precise
information about the running time of portions of your code than the
Benchmark module will give you, but don't want to go all out and
profile your code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc CHANGES LICENSE README
%{perl_vendorlib}/Benchmark
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.710.200-4mdv2012.0
+ Revision: 765073
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.710.200-3
+ Revision: 763634
- bump release
- rebuilt for perl-5.14.x

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.7102

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.710.200-2
+ Revision: 676877
- rebuild

* Mon Aug 31 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1:0.710.200-1mdv2011.0
+ Revision: 422881
- bumping epoch
- update to 0.7102

* Mon Jul 21 2008 Thierry Vignaud <tv@mandriva.org> 0.7101-2mdv2009.0
+ Revision: 239336
- patch 0: fix dependancy on /usr/local/bin/perl

* Sat Jul 19 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.7101-1mdv2009.0
+ Revision: 238736
- own containing directory

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.7100-3mdv2008.0
+ Revision: 25447
- rebuild


* Thu Apr 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.7100-2mdk
- Fix SPEC Using perl Policies
	- BuildRequires
	- Source URL
- use mkrel

* Sun Jul 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7100-1mdk
- initial Mandriva package

