Name:           plank-theme-korora
Version:        0.1
Release:        1%{?dist}
Summary:        Plank theme for the Korora Project
License:        GPLv3
URL:            https://kororaproject.org/
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       plank

%description
This is a plank theme based on Jupiter Redux from the elementary OS project.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/plank/themes/Korora
install -m 0644 Korora/* %{buildroot}%{_datadir}/plank/themes/Korora

%files
%{_datadir}/plank/themes/Korora/*

%changelog
* Mon Feb 16 2015 Ian Firns <firnsy@kororaproject.org> - 0.1-1
- Intial rpm build
