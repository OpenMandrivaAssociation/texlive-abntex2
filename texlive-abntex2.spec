%global tl_name abntex2
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9.7
Release:	%{tl_revision}.1
Summary:	Typeset technical and scientific Brazilian documents based on ABNT rules
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/abntex2
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abntex2.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/abntex2.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides support for typesetting technical and scientific
Brazilian documents (like academic thesis, articles, reports, research
project and others) based on the ABNT rules (Associacao Brasileira de
Normas Tecnicas). It replaces the old abntex.

