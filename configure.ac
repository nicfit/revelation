dnl
dnl configure.ac
dnl
dnl $Id$
dnl

dnl initialize autoconf/automake
AC_PREREQ(2.53)
AC_INIT([revelation],[0.5.0],[https://bitbucket.org/erikg/revelation/issues/new],[revelation],[http://revelation.olasagasti.info/])
AM_INIT_AUTOMAKE([1.11 tar-ustar dist-xz no-dist-gzip -Wno-portability foreign])

RVL_PYTHON_PATH(3.5)
RVL_PYGTK()
RVL_GETTEXT()
RVL_MMAN()
RVL_GCONF()
RVL_FDO_MIME()

RVL_PYTHON_MODULE(Crypto, yes)
RVL_PYTHON_MODULE(dbus, yes)
RVL_PYTHON_MODULE(cracklib, yes)


dnl output files
AC_OUTPUT([
	Makefile
	data/Makefile
	data/gconf/Makefile
	data/icons/Makefile
	data/icons/16x16/Makefile
	data/icons/24x24/Makefile
	data/icons/32x32/Makefile
	data/icons/48x48/Makefile
	data/icons/256x256/Makefile
	data/icons/scalable/Makefile
	data/mime/revelation.desktop.in
	data/mime/Makefile
	data/ui/Makefile
	po/Makefile.in
	src/Makefile
	src/bundle/Makefile
	src/lib/Makefile
	src/lib/datahandler/Makefile
])

echo "

------------------------------------------------------------------
-- revelation compilation options

revelation version:        ${PACKAGE_VERSION}
------------------------------------------------------------------
"

