%define upstream_name    Benchmark-Timer
Summary:	Benchmark::Timer - Perl code benchmarking tool
Name:		perl-%{upstream_name}
Epoch:		1
Version:	0.7112
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/coppit/benchmark-timer
Source0:	https://cpan.metacpan.org/authors/id/D/DC/DCOPPIT/Benchmark-Timer-%{version}.tar.gz
Patch0:		Benchmark-Timer-fix-dep.patch
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Statistics::TTest)
BuildRequires:	perl-devel

%description
The Benchmark::Timer class allows you to time portions of code
conveniently, as well as benchmark code by allowing timings of
repeated trials. It is perfect for when you need more precise
information about the running time of portions of your code than the
Benchmark module will give you, but don't want to go all out and
profile your code.

%prep
%setup -qn %{upstream_name}-%{version}
%patch0 -p0

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc CHANGES LICENSE README
%{perl_vendorlib}/Benchmark
%{_mandir}/man3/*

