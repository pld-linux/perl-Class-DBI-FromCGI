#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	DBI-FromCGI
Summary:	Class::DBI::FromCGI - update Class::DBI data using CGI::Untaint
Summary(pl):	Class::DBI::FromCGI - aktualizacja danych Class::DBI przy u�yciu CGI::Untaint
Name:		perl-Class-DBI-FromCGI
Version:	0.94
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	126040b7e83218197786de2c6699100f
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

%description -l pl
Jedn� z najbardziej irytuj�cych rzeczy przy pisaniu aplikacji WWW jest
monotonia pisania ca�y czas w wi�kszo�ci powtarzaj�cego si� kodu. A
tam gdzie wyst�puje monotonia, jest tendencja pomijania tego o czym
wiemy, �e jest bardzo wa�ne, ale bolesne przy pisaniu - jak
sprawdzanie ska�enia i rozs�dna kontrola poprawno�ci wej�cia
(zw�aszcza, �e nadal mo�emy pokaza� "dzia�aj�c�" aplikacje bez tego!).
Teraz CGI::Untaint mo�e o to w wi�kszo�ci zadba� za nas.

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
