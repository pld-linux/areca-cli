Summary:	Utility to control Areca SATA RAID controllers
Name:		areca-cli
Version:	1.86
Release:	1
# http://www.areca.us/support/download/RaidCards/Documents/Manual_Spec/Downloadable_Software_Licenses.zip
# Linux Exception: redistributable if not modified
License:	License for Customer Use of Areca Software
Group:		Base
Source0:	http://www.areca.us/support/s_linux/cli/i386/cli32.zip
# Source0-md5:	-
Source1:	http://www.areca.us/support/s_linux/cli/x86_64/cli64.zip
# Source1-md5:	-
Source2:	http://www.areca.us/support/download/RaidCards/Documents/Manual_Spec/CLIManual.zip
# Source2-md5:	-
URL:		http://www.areca.us/support/main.htm
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to control Areca SATA RAID controllers.

%prep
%setup -qcT -a2
%ifarch %{ix86}
%{__unzip} -qq %{SOURCE0}
%endif
%ifarch %{x8664}
%{__unzip} -qq %{SOURCE1}
%endif
chmod a+rx cli*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -p cli* $RPM_BUILD_ROOT%{_sbindir}/%{name}
ln -s %{name} $RPM_BUILD_ROOT%{_sbindir}/$(echo cli*)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/%{name}
# this likely conflicts oneday
%attr(755,root,root) %{_sbindir}/cli*
