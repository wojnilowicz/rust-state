# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate state

Name:           rust-state
Version:        0.6.0
Release:        %autorelease
Summary:        Library for safe and effortless global and thread-local state management

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/state
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          state-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
%{summary}}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tls-devel %{_description}

This package contains library source intended for building other packages which
use the "tls" feature of the "%{crate}" crate.

%files       -n %{name}+tls-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install
rm %{buildroot}/%{crate_instdir}/src/thread_local/LICENSE-APACHE
rm %{buildroot}/%{crate_instdir}/src/thread_local/LICENSE-MIT

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
