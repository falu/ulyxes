#******************************************************************************
#	Ulyses - an open source project to drive total stations and
#			publish observation results
#	GPL license
#	Copyright (C) 2011 Zoltan Siki <siki@agt.bme.hu>
#******************************************************************************
#	Serial communication parameters
#******************************************************************************
set actPars(sendquery) ""
set actPars(buffering) "line"
set actPars(eofchar) ""
set actPars(baud) "9600"
set actPars(init) ""
set actPars(port) "COM4:"
set actPars(stop) "1"
set actPars(buffsize) "4096"
set actPars(dir) ""
set actPars(translation) "auto"
set actPars(encoding) "utf-8"
set actPars(parity) "n"
set actPars(blocking) "0"
set actPars(data) "8"
set actPars(query) ""
