#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-cyclocomp
Version  : 1.1.1
Release  : 31
URL      : https://cran.r-project.org/src/contrib/cyclocomp_1.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/cyclocomp_1.1.1.tar.gz
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
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
used to indicate the complexity of a program. It is a quantitative
    measure of the number of linearly independent paths through a program's
    source code. It was developed by Thomas J. McCabe, Sr. in 1976.

%prep
%setup -q -n cyclocomp
pushd ..
cp -a cyclocomp buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693443485

%install
export SOURCE_DATE_EPOCH=1693443485
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

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
