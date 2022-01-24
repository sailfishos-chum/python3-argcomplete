# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       python3-argcomplete

# >> macros
# << macros

Summary:    Tab complete all the things!
Version:    2.0.0
Release:    0
Group:      Applications
License:    Apache-2.0
BuildArch:  noarch
URL:        https://pypi.org/project/argcomplete/
Source0:    %{name}-%{version}.tar.gz
Source100:  python3-argcomplete.yaml
BuildRequires:  pkgconfig(python)
BuildRequires:  python3-rpm-macros

%description

Argcomplete provides easy, extensible command line tab completion of
arguments for your Python script.

%if "%{?vendor}" == "chum"
PackageName: argcomplete
Type: console-application
Categories:
 - Library
Custom:
  PackagingRepo: https://github.com/sailfishos-chum/python3-argcomplete
Url:
  Homepage: https://pypi.org/project/argcomplete/
%endif


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%{py3_build}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%{py3_install}

# >> install post
# << install post

%files
%defattr(-,root,root,-)
# >> files
%license LICENSE.rst
%doc README.rst
%{_bindir}/*
%{python3_sitelib}/*
# << files
