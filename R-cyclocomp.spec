#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-cyclocomp
Version  : 1.1.0
Release  : 13
URL      : https://cran.r-project.org/src/contrib/cyclocomp_1.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cyclocomp_1.1.0.tar.gz
Summary  : Cyclomatic Complexity of R Code
Group    : Development/Tools
License  : MIT
Requires: R-callr
Requires: R-crayon
Requires: R-desc
Requires: R-remotes
Requires: R-withr
BuildRequires : R-callr
BuildRequires : R-crayon
BuildRequires : R-desc
BuildRequires : R-remotes
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
used to indicate the complexity of a program. It is a quantitative
    measure of the number of linearly independent paths through a program's
    source code. It was developed by Thomas J. McCabe, Sr. in 1976.

%prep
%setup -q -c -n cyclocomp
cd %{_builddir}/cyclocomp

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589584328

%install
export SOURCE_DATE_EPOCH=1589584328
rm -rf %{buildroot}
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cyclocomp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cyclocomp
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library cyclocomp
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc cyclocomp || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/cyclocomp/DESCRIPTION
/usr/lib64/R/library/cyclocomp/INDEX
/usr/lib64/R/library/cyclocomp/LICENSE
/usr/lib64/R/library/cyclocomp/Meta/Rd.rds
/usr/lib64/R/library/cyclocomp/Meta/features.rds
/usr/lib64/R/library/cyclocomp/Meta/hsearch.rds
/usr/lib64/R/library/cyclocomp/Meta/links.rds
/usr/lib64/R/library/cyclocomp/Meta/nsInfo.rds
/usr/lib64/R/library/cyclocomp/Meta/package.rds
/usr/lib64/R/library/cyclocomp/NAMESPACE
/usr/lib64/R/library/cyclocomp/NEWS.md
/usr/lib64/R/library/cyclocomp/R/cyclocomp
/usr/lib64/R/library/cyclocomp/R/cyclocomp.rdb
/usr/lib64/R/library/cyclocomp/R/cyclocomp.rdx
/usr/lib64/R/library/cyclocomp/help/AnIndex
/usr/lib64/R/library/cyclocomp/help/aliases.rds
/usr/lib64/R/library/cyclocomp/help/cyclocomp.rdb
/usr/lib64/R/library/cyclocomp/help/cyclocomp.rdx
/usr/lib64/R/library/cyclocomp/help/paths.rds
/usr/lib64/R/library/cyclocomp/html/00Index.html
/usr/lib64/R/library/cyclocomp/html/R.css
/usr/lib64/R/library/cyclocomp/tests/testthat.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-andor.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-break.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-calls.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-cyclocomp-package.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-cyclocomp_q.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-function.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-if.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-next.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-repeat.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-return.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-seq.R
/usr/lib64/R/library/cyclocomp/tests/testthat/test-stress.R
