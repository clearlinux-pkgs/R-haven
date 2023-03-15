#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-haven
Version  : 2.5.2
Release  : 62
URL      : https://cran.r-project.org/src/contrib/haven_2.5.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/haven_2.5.2.tar.gz
Summary  : Import and Export 'SPSS', 'Stata' and 'SAS' Files
Group    : Development/Tools
License  : MIT
Requires: R-haven-lib = %{version}-%{release}
Requires: R-haven-license = %{version}-%{release}
Requires: R-cli
Requires: R-cpp11
Requires: R-forcats
Requires: R-hms
Requires: R-lifecycle
Requires: R-readr
Requires: R-rlang
Requires: R-tibble
Requires: R-tidyselect
Requires: R-vctrs
BuildRequires : R-cli
BuildRequires : R-cpp11
BuildRequires : R-forcats
BuildRequires : R-hms
BuildRequires : R-lifecycle
BuildRequires : R-readr
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-tidyselect
BuildRequires : R-vctrs
BuildRequires : buildreq-R
BuildRequires : pkgconfig(zlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# haven <a href='https://haven.tidyverse.org'><img src='man/figures/logo.png' align="right" height="139" /></a>

%package lib
Summary: lib components for the R-haven package.
Group: Libraries
Requires: R-haven-license = %{version}-%{release}

%description lib
lib components for the R-haven package.


%package license
Summary: license components for the R-haven package.
Group: Default

%description license
license components for the R-haven package.


%prep
%setup -q -n haven
cd %{_builddir}/haven

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1677627819

%install
export SOURCE_DATE_EPOCH=1677627819
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/R-haven
cp %{_builddir}/haven/src/readstat/LICENSE %{buildroot}/usr/share/package-licenses/R-haven/2d80377f5d525b4dc065c8d0a6228d28872a846f || :
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/haven/DESCRIPTION
/usr/lib64/R/library/haven/INDEX
/usr/lib64/R/library/haven/LICENSE
/usr/lib64/R/library/haven/Meta/Rd.rds
/usr/lib64/R/library/haven/Meta/features.rds
/usr/lib64/R/library/haven/Meta/hsearch.rds
/usr/lib64/R/library/haven/Meta/links.rds
/usr/lib64/R/library/haven/Meta/nsInfo.rds
/usr/lib64/R/library/haven/Meta/package.rds
/usr/lib64/R/library/haven/Meta/vignette.rds
/usr/lib64/R/library/haven/NAMESPACE
/usr/lib64/R/library/haven/NEWS.md
/usr/lib64/R/library/haven/R/haven
/usr/lib64/R/library/haven/R/haven.rdb
/usr/lib64/R/library/haven/R/haven.rdx
/usr/lib64/R/library/haven/doc/datetimes.Rmd
/usr/lib64/R/library/haven/doc/datetimes.html
/usr/lib64/R/library/haven/doc/index.html
/usr/lib64/R/library/haven/doc/semantics.R
/usr/lib64/R/library/haven/doc/semantics.Rmd
/usr/lib64/R/library/haven/doc/semantics.html
/usr/lib64/R/library/haven/examples/iris.dta
/usr/lib64/R/library/haven/examples/iris.sas7bdat
/usr/lib64/R/library/haven/examples/iris.sav
/usr/lib64/R/library/haven/help/AnIndex
/usr/lib64/R/library/haven/help/aliases.rds
/usr/lib64/R/library/haven/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/haven/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/haven/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/haven/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/haven/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/haven/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/haven/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/haven/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/haven/help/figures/logo.png
/usr/lib64/R/library/haven/help/haven.rdb
/usr/lib64/R/library/haven/help/haven.rdx
/usr/lib64/R/library/haven/help/paths.rds
/usr/lib64/R/library/haven/html/00Index.html
/usr/lib64/R/library/haven/html/R.css
/usr/lib64/R/library/haven/tests/testthat.R
/usr/lib64/R/library/haven/tests/testthat/_snaps/haven-sas.md
/usr/lib64/R/library/haven/tests/testthat/_snaps/haven-spss.md
/usr/lib64/R/library/haven/tests/testthat/_snaps/haven-stata.md
/usr/lib64/R/library/haven/tests/testthat/_snaps/labelled-pillar.md
/usr/lib64/R/library/haven/tests/testthat/_snaps/labelled.md
/usr/lib64/R/library/haven/tests/testthat/_snaps/labelled_spss.md
/usr/lib64/R/library/haven/tests/testthat/_snaps/tagged_na.md
/usr/lib64/R/library/haven/tests/testthat/helper-roundtrip.R
/usr/lib64/R/library/haven/tests/testthat/helpers-types.R
/usr/lib64/R/library/haven/tests/testthat/sas/datetime.sas7bdat
/usr/lib64/R/library/haven/tests/testthat/sas/formats.sas7bcat
/usr/lib64/R/library/haven/tests/testthat/sas/hadley.sas7bdat
/usr/lib64/R/library/haven/tests/testthat/sas/hadley.zip
/usr/lib64/R/library/haven/tests/testthat/sas/tagged-na.sas7bcat
/usr/lib64/R/library/haven/tests/testthat/sas/tagged-na.sas7bdat
/usr/lib64/R/library/haven/tests/testthat/spss/datetime.sav
/usr/lib64/R/library/haven/tests/testthat/spss/labelled-num-na.sav
/usr/lib64/R/library/haven/tests/testthat/spss/labelled-num.sav
/usr/lib64/R/library/haven/tests/testthat/spss/labelled-str.sav
/usr/lib64/R/library/haven/tests/testthat/spss/umlauts.sav
/usr/lib64/R/library/haven/tests/testthat/spss/variable-label.sav
/usr/lib64/R/library/haven/tests/testthat/stata/datetime-d.dta
/usr/lib64/R/library/haven/tests/testthat/stata/notes.dta
/usr/lib64/R/library/haven/tests/testthat/stata/tagged-na-double.dta
/usr/lib64/R/library/haven/tests/testthat/stata/tagged-na-int.dta
/usr/lib64/R/library/haven/tests/testthat/stata/types.dta
/usr/lib64/R/library/haven/tests/testthat/test-as_factor.R
/usr/lib64/R/library/haven/tests/testthat/test-force_utc.R
/usr/lib64/R/library/haven/tests/testthat/test-haven-sas.R
/usr/lib64/R/library/haven/tests/testthat/test-haven-spss.R
/usr/lib64/R/library/haven/tests/testthat/test-haven-stata.R
/usr/lib64/R/library/haven/tests/testthat/test-labelled-pillar.R
/usr/lib64/R/library/haven/tests/testthat/test-labelled.R
/usr/lib64/R/library/haven/tests/testthat/test-labelled_spss.R
/usr/lib64/R/library/haven/tests/testthat/test-tagged_na.R
/usr/lib64/R/library/haven/tests/testthat/test-zap-empty.R
/usr/lib64/R/library/haven/tests/testthat/test-zap_label.R
/usr/lib64/R/library/haven/tests/testthat/test-zap_labels.R
/usr/lib64/R/library/haven/tests/testthat/test-zap_missing.R
/usr/lib64/R/library/haven/tests/testthat/test-zap_widths.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/haven/libs/haven.so
/usr/lib64/R/library/haven/libs/haven.so.avx2
/usr/lib64/R/library/haven/libs/haven.so.avx512

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/R-haven/2d80377f5d525b4dc065c8d0a6228d28872a846f
