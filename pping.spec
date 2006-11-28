
Summary: Utility to ping multiple hosts in parallel
Name: pping
Version: 0.01
Release: 2.of
License: GPL
Group: Applications/Internet
Source: http://www.openfusion.com.au/labs/pping/%{name}-%{version}.tar.gz
URL: http://www.openfusion.com.au/labs/pping/
Packager: Gavin Carr <gavin@openfusion.com.au>
Vendor: Open Fusion Pty. Ltd.
Requires: perl, perl-suidperl
Requires: perl-Term-Size, perl-Term-Size-Unix, perl-Config-Tiny
Requires: perl-POE, perl-POE-Component-Client-Ping
BuildRequires: perl
AutoReq: no
Buildroot: %_tmppath/%{name}-%{version}

%description
pping is a parallel-ping utility for sending multiple ICMP echo requests 
to sets of target hosts. It produces a line of output every second
reporting colour-coded round-trip-times for each host.

%prep
%setup

%build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man8
cp %{name} %{buildroot}/%{_bindir}/%{name}
pod2man --section=8 -r "%{name} %{version}" %{name} > %{buildroot}/%{_mandir}/man8/%{name}.8

%files
%defattr(-,root,root)
%attr(4755,root,root) %{_bindir}/%{name}
%{_mandir}/man8/%{name}*
%doc pping.conf.sample

%changelog
* Tue Nov 21 2006 Gavin Carr <gavin@openfusion.com.au> 0.01-1
- Initial rpm version.

