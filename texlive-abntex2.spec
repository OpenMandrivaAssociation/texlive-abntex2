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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides support for typesetting technical and scientific
Brazilian documents (like academic thesis, articles, reports, research
project and others) based on the ABNT rules (Associacao Brasileira de
Normas Tecnicas). It replaces the old abntex.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bib
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bib/abntex2
%dir %{_datadir}/texmf-dist/bibtex/bst/abntex2
%dir %{_datadir}/texmf-dist/doc/latex/abntex2
%dir %{_datadir}/texmf-dist/tex/latex/abntex2
%dir %{_datadir}/texmf-dist/doc/latex/abntex2/examples
%{_datadir}/texmf-dist/bibtex/bib/abntex2/abntex2-options.bib
%{_datadir}/texmf-dist/bibtex/bst/abntex2/abntex2-alf.bst
%{_datadir}/texmf-dist/bibtex/bst/abntex2/abntex2-num.bst
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/README
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/abntex2-doc-abnt-10520.bib
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/abntex2-doc-abnt-6023.bib
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/abntex2-doc-options.bib
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/abntex2-doc-test.bib
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/abntex2-doc.bib
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/abntex2.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/abntex2.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/abntex2cite-alf.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/abntex2cite-alf.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/abntex2cite.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/abntex2cite.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-artigo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-artigo.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-glossarios.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-glossarios.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-img-grafico.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-img-marca.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-include-comandos.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-livro.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-livro.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-projeto-pesquisa.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-projeto-pesquisa.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-references.bib
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-relatorio-tecnico.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-relatorio-tecnico.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-slides.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-slides.tex
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-trabalho-academico.pdf
%doc %{_datadir}/texmf-dist/doc/latex/abntex2/examples/abntex2-modelo-trabalho-academico.tex
%{_datadir}/texmf-dist/tex/latex/abntex2/abntex2.cls
%{_datadir}/texmf-dist/tex/latex/abntex2/abntex2abrev.sty
%{_datadir}/texmf-dist/tex/latex/abntex2/abntex2cite.sty
