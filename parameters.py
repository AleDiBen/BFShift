from enum import Enum
    
class Parameters(Enum):
	ALPHABET = 0
	BRUTEFORCE_ALL = 1
	BRUTEFORCE_ALPHABET = 2
	BRUTEFORCE_SHIFT = 3
	CUSTOM_ALPHABET = 4
	DEBUG = 5
	DECODE = 6
	ENCODE = 7
	FLAG_FORMAT = 8
	HELP = 9
	MESSAGE = 10
	SHIFT = 11


class Errors(Enum):
	NO_ERROR = 0
	SAME_OPT = -1
	MUTEX = -2


class Modes(Enum):
	ENCODE = 0
	DECODE = 1


class DebugMessages(Enum):
	INFO = 0
	WARNING = 1
	ERROR = 2
	FATAL = 3


class BruteForceMethod(Enum):
	ALL = 0
	ALPHABET = 1
	SHIFT = 2


	# alph,	bfall,	bfalph,	bfsh,	custm,	dbg,	dec,	enc,	flgfmt,	hlp,	msg,	shft
matrix = [
	[-1,	-2,		-2,		 0,		-2,		 0,		 0,		 0,		 0,		 0,		 0,		 0],		# ALPHABET				OK
	[-2,	-1,		-2,		-2,		 0,		 0,		 0,		-2,		 0,		 0,		 0,		-2],		# BRUTEFORCE_ALL		OK
	[-2,	-2,		-1,		 0,		 0,		 0,		 0,		-2,		 0,		 0,		 0,		 0],		# BRUTEFORCE_ALPHABET	OK
	[ 0,	-2,		 0,		-1,		 0,		 0,		 0,		-2,		 0,		 0,		 0,		-2],		# BRUTEFORCE_SHIFT		OK
	[-2,	 0,		 0,		 0,		-1,		 0,		 0,		 0,		 0,		 0,		 0,		 0],		# CUSTOM_ALPHABET		OK
	[ 0,	 0,		 0,		 0,		 0,		-1,		 0,		 0,		 0,		 0,		 0,		 0],		# DEBUG					OK
	[ 0,	 0,		 0,		 0,		 0,		 0,		-1,		-2,		 0,		 0,		 0,		 0],		# DECODE				OK
	[ 0,	-2,		-2,		-2,		 0,		 0,		-2,		-1,		 0,		 0,		 0,		 0],		# ENCODE				OK
	[ 0,	 0,		 0,		 0,		 0,		 0,		 0,		 0,		-1,		 0,		 0,		 0],		# FLAG_FORMAT			OK
	[ 0,	 0,		 0,		 0,		 0,		 0,		 0,		 0,		 0,		-1,		 0,		 0],		# HELP					OK
	[ 0,	 0,		 0,		 0,		 0,		 0,		 0,		 0,		 0,		 0,		-1,		 0],		# MESSAGE				OK
	[ 0,	-2,		 0,		-2,		 0,		 0,		 0,		 0,		 0,		 0,		 0,		-1]			# SHIFT					OK
]