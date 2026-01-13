#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Class
%define		pnam	DBI-FromCGI
Summary:	Class::DBI::FromCGI - update Class::DBI data using CGI::Untaint
Summary(pl.UTF-8):	Class::DBI::FromCGI - aktualizacja danych Class::DBI przy użyciu CGI::Untaint
Name:		perl-Class-DBI-FromCGI
Version:	1.00
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b7ff8430745c3a72930310da5fc39ded
URL:		http://search.cpan.org/dist/Class-DBI-FromCGI/
BuildRequires:	perl-CGI-Untaint >= 0.8
BuildRequires:	perl-Class-DBI >= 0.94
BuildRequires:	perl-DBD-SQLite
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Class-DBI >= 0.94
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
One of the most irritating things about writing web-based applications
is the monotony of writing much of the same stuff over and over again.
And, where there's monotony there's a tendency to skip over stuff that
we all know is really important, but is a pain to write - like Taint
Checking and sensible input validation.  (Especially as we can still
show a 'working' application without it!). So, we now have
CGI::Untaint to take care of a lot of that for us.

%description -l pl.UTF-8
Jedną z najbardziej irytujących rzeczy przy pisaniu aplikacji WWW jest
monotonia pisania cały czas w większości powtarzającego się kodu. A
tam gdzie występuje monotonia, jest tendencja pomijania tego o czym
wiemy, że jest bardzo ważne, ale bolesne przy pisaniu - jak
sprawdzanie skażenia i rozsądna kontrola poprawności wejścia
(zwłaszcza, że nadal możemy pokazać "działającą" aplikacje bez tego!).
Teraz CGI::Untaint może o to w większości zadbać za nas.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/%{pdir}/DBI/FromCGI.pm
%{_mandir}/man3/*
