Name: perl-Net-Telnet
Summary: Net-Telnet Perl module
Version: 3.03
Release: 11%{?alphatag:.%{alphatag}}%{?dist}
Group: Development/Libraries
License: GPL+ or Artistic
URL: http://search.cpan.org/dist/Net-Telnet/
Source0: ftp://ftp.cpan.org/pub/CPAN/authors/id/J/JR/JROGERS/Net-Telnet-%{version}.tar.gz

ExcludeArch: s390 s390x ppc ppc64

# runtime depends
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# build
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
BuildRequires: perl >= 0:5.00503
BuildRequires: perl-Digest-HMAC
BuildRequires: perl(ExtUtils::MakeMaker)

%description
Net::Telnet allows you to make client connections to a TCP port and do
network I/O, especially to a port using the TELNET protocol. Simple I/O
methods such as print, get, and getline are provided. More sophisticated
interactive features are provided because connecting to a TELNET port
ultimately means communicating with a program designed for human interaction.
These interactive features include the ability to specify a time-out and to
wait for patterns to appear in the input stream, such as the prompt from a
shell.

%prep
%setup -q -n Net-Telnet-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make

%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Wed May 12 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.03-11
- Do not build on ppc and ppc64.
  Resolves: rhbz#590994

* Mon Mar  1 2010 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.03-10
- Resolves: rhbz#569294
- Add ExcludeArch to drop s390 and s390x

* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 3.03-9.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.03-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 23 2008 Fabio M. Di Nitto <fdinitto@redhat.com> - 3.03-7
- Fix bug 226273:
  * Add dist tag.
  * Fix rpmlint errors for %%description.
  * Remove MANIFEST from package.
- General clean up of spec file.

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.03-6.1
Rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 3.03-5.1 
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Mon Jun 30 2006 Jason Vas Dias <jvdias@redhat.com> - 3.03-5
- correct License: tag

* Wed Feb 15 2006 Jason Vas Dias <jvdias@redhat.com> - 3.03-4.3
- fix bug 180591: correct URL: tag

* Fri Feb 03 2006 Jason Vas Dias <jvdias@redhat.com> - 3.03-4.2
- rebuild for new perl-5.8.8
- modify .spec file to conform to Fedora spectemplate-perl.spec

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcc

* Fri Dec 16 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt for new gcj

* Fri Feb 13 2004 Jonathan Brassow <jbrassow@redhat.com>
- initial import
