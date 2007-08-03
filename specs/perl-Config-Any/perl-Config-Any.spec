# $Id$
# Authority: dag
# Upstream: Joel Bernstein <rataxis$cpan,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Config-Any

Summary: Load configuration from different file formats, transparently
Name: perl-Config-Any
Version: 0.07
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Config-Any/

Source: http://www.cpan.org/modules/by-module/Config/Config-Any-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Load configuration from different file formats, transparently.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Config/
%{perl_vendorlib}/Config/Any/
%{perl_vendorlib}/Config/Any.pm

%changelog
* Fri Aug 03 2007 Dag Wieers <dag@wieers.com> - 0.07-1
- Initial package. (using DAR)
