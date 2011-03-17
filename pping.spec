
Summary: Utility to ping multiple hosts in parallel
Name: pping
Version: 0.4
Release: 1%{?org_tag}%{?dist}
License: GPL
Group: Applications/Internet
Source: http://www.openfusion.com.au/labs/pping/%{name}-%{version}.tar.gz
URL: http://www.openfusion.com.au/labs/pping/
Packager: Gavin Carr <gavin@openfusion.com.au>
Vendor: Open Fusion Pty. Ltd.
Requires: perl, perl-suidperl
Requires: perl-Term-Size, perl-Term-Size-Unix, perl-Config-Tiny
Requires: perl-POE, perl-POE-Component-Client-Ping
Requires: perl-Time-Piece
BuildRequires: perl
AutoReq: no
Buildroot: %_tmppath/%{name}-%{version}
BuildArch: noarch

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
%doc README
%doc COPYING

%changelog
* Thu Mar 17 2011 Gavin Carr <gavin@openfusion.com.au> 0.4-1
- Convert hostnames to ips for pinging, and back for reporting.

* Wed Nov 14 2007 Gavin Carr <gavin@openfusion.com.au> 0.3-1
- Add timestamp and outfile support.

* Wed Dec 12 2006 Gavin Carr <gavin@openfusion.com.au> 0.2-1
- Add README and COPYING files.

* Tue Nov 21 2006 Gavin Carr <gavin@openfusion.com.au> 0.1-1
- Initial rpm version.

