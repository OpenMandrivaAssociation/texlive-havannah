Name:		texlive-havannah
Version:	36348
Release:	2
Summary:	Diagrams of board positions in the games of Havannah and Hex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/havannah
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/havannah.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/havannah.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/havannah.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines macros for typesetting diagrams of board
positions in the games of Havannah and Hex.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/havannah
%{_texmfdistdir}/tex/latex/havannah
%doc %{_texmfdistdir}/doc/latex/havannah

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
