#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Logger
%define		pnam	Syslog
%include	/usr/lib/rpm/macros.perl
Summary:	Logger::Syslog -- an intuitive wrapper over Syslog for Perl
Name:		perl-Logger-Syslog
Version:	1.1
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Logger/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8ce1bb5e34a4e56b2e0d03159cb5185c
URL:		http://search.cpan.org/dist/Logger-Syslog/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You want to deal with syslog, but you don't want to bother with
Sys::Syslog, that module is for you.

Logger::Syslog takes care of everything regarding the Syslog
communication, all you have to do is to use the function you need to
send a message to syslog.

Logger::Syslog provides one function per Syslog message level: debug,
info, warning, error, notice, critic, alert.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%dir %{perl_vendorlib}/Logger
%{perl_vendorlib}/Logger/Syslog.pm
%{_mandir}/man3/Logger::Syslog.3pm*
