# revision 23021
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-documentation-czechslovak
Epoch:		1
Version:	20120224
Release:	4
Summary:	Czech/Slovak documentation
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-documentation-czechslovak.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-lshort-czech
Requires:	texlive-lshort-slovak
Requires:	texlive-texlive-cz
Requires:	texlive-collection-documentation-base

%description
TeXLive collection-documentation-czechslovak package.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780209
- Update to latest release.
- Import texlive-collection-documentation-czechslovak
- Import texlive-collection-documentation-czechslovak

