# revision 32013
# category Package
# catalog-ctan /macros/latex/contrib/abntex2
# catalog-date 2013-10-27 11:00:02 +0100
# catalog-license lppl1.3
# catalog-version 1.9
Name:		texlive-abntex2
Version:	1.9
Release:	4
Summary:	Typeset technical and scientific Brazilian documents based on ABNT rules
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/abntex2
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abntex2.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/abntex2.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides support for writing technical and
scientific Brazilian documents (like academic thesis, articles,
reports, research project and others) based on ABNT rules
(Associacao Brasileira de Normas Tecnicas). It replaces the old
abntex.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/abntex2/abntex2-options.bib
%{_texmfdistdir}/bibtex/bst/abntex2/abntex2-alf.bst
%{_texmfdistdir}/bibtex/bst/abntex2/abntex2-num.bst
%{_texmfdistdir}/tex/latex/abntex2/abntex2.cls
%{_texmfdistdir}/tex/latex/abntex2/abntex2abrev.sty
%{_texmfdistdir}/tex/latex/abntex2/abntex2cite.sty
%doc %{_texmfdistdir}/doc/latex/abntex2/README
%doc %{_texmfdistdir}/doc/latex/abntex2/abntex2-doc-abnt-10520.bib
%doc %{_texmfdistdir}/doc/latex/abntex2/abntex2-doc-abnt-6023.bib
%doc %{_texmfdistdir}/doc/latex/abntex2/abntex2-doc-options.bib
%doc %{_texmfdistdir}/doc/latex/abntex2/abntex2-doc-test.bib
%doc %{_texmfdistdir}/doc/latex/abntex2/abntex2-doc.bib
%doc %{_texmfdistdir}/doc/latex/abntex2/abntex2.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/abntex2.tex
%doc %{_texmfdistdir}/doc/latex/abntex2/abntex2cite-alf.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/abntex2cite-alf.tex
%doc %{_texmfdistdir}/doc/latex/abntex2/abntex2cite.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/abntex2cite.tex
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-artigo.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-artigo.tex
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-glossarios.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-glossarios.tex
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-img-grafico.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-img-marca.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-include-comandos.tex
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-livro-bandeirinha.jpg
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-livro-pintassilgo.jpg
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-livro-saira-amarela.jpg
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-livro.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-livro.tex
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-projeto-pesquisa.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-projeto-pesquisa.tex
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-references.bib
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-relatorio-tecnico.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-relatorio-tecnico.tex
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-slides.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-slides.tex
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-trabalho-academico.pdf
%doc %{_texmfdistdir}/doc/latex/abntex2/examples/abntex2-modelo-trabalho-academico.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
