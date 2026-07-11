%global tl_name havannah
%global tl_revision 36348

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Diagrams of board positions in the games of Havannah and Hex
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/havannah
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/havannah.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/havannah.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/havannah.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines macros for typesetting diagrams of board positions
in the games of Havannah and Hex.

