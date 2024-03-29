import os
import sys
import findimports
import importlib
import importlib.util


modulelist = ['__future__', '__main__', '_dummy_thread', '_thread', 'abc', 'aifc', 'argparse', 'array', 'ast', 'asynchat', 'asyncio', 'asyncore', 'atexit', 'audioop', 'base64', 'bdb', 'binascii', 'binhex', 'bisect', 'builtins', 'bz2', 'cProfile', 'calendar', 'cgi', 'cgitb', 'chunk', 'cmath', 'cmd', 'code', 'codecs', 'codeop', 'collections', 'collections.abc', 'colorsys', 'compileall', 'concurrent.futures', 'configparser', 'contextlib', 'copy', 'copyreg', 'crypt', 'csv', 'ctypes', 'curses', 'curses.ascii', 'curses.panel', 'curses.textpad', 'datetime', 'dbm', 'dbm.dumb', 'dbm.gnu', 'dbm.ndbm', 'decimal', 'difflib', 'dis', 'distutils', 'distutils.archive_util', 'distutils.bcppcompiler', 'distutils.ccompiler', 'distutils.cmd', 'distutils.command', 'distutils.command.bdist', 'distutils.command.bdist_dumb', 'distutils.command.bdist_msi', 'distutils.command.bdist_packager', 'distutils.command.bdist_rpm', 'distutils.command.bdist_wininst', 'distutils.command.build', 'distutils.command.build_clib', 'distutils.command.build_ext', 'distutils.command.build_py', 'distutils.command.build_scripts', 'distutils.command.check', 'distutils.command.clean', 'distutils.command.config', 'distutils.command.install', 'distutils.command.install_data', 'distutils.command.install_headers', 'distutils.command.install_lib', 'distutils.command.install_scripts', 'distutils.command.register', 'distutils.command.sdist', 'distutils.core', 'distutils.cygwinccompiler', 'distutils.debug', 'distutils.dep_util', 'distutils.dir_util', 'distutils.dist', 'distutils.errors', 'distutils.extension', 'distutils.fancy_getopt', 'distutils.file_util', 'distutils.filelist', 'distutils.log', 'distutils.msvccompiler', 'distutils.spawn', 'distutils.sysconfig', 'distutils.text_file', 'distutils.unixccompiler', 'distutils.util', 'distutils.version', 'doctest', 'dummy_threading', 'email', 'email.charset', 'email.contentmanager', 'email.encoders', 'email.errors', 'email.generator', 'email.header', 'email.headerregistry', 'email.iterators', 'email.message', 'email.mime', 'email.parser', 'email.policy', 'email.utils', 'encodings.idna', 'encodings.mbcs', 'encodings.utf_8_sig', 'ensurepip', 'enum', 'errno', 'faulthandler', 'fcntl', 'filecmp', 'fileinput', 'fnmatch', 'formatter', 'fpectl', 'fractions', 'ftplib', 'functools', 'gc', 'getopt', 'getpass', 'gettext', 'glob', 'grp', 'gzip', 'hashlib', 'heapq', 'hmac', 'html', 'html.entities', 'html.parser', 'http', 'http.client', 'http.cookiejar', 'http.cookies', 'http.server', 'imaplib', 'imghdr', 'imp', 'importlib', 'importlib.abc', 'importlib.machinery', 'importlib.util', 'inspect', 'io', 'ipaddress', 'itertools', 'json', 'json.tool', 'keyword', 'lib2to3', 'linecache', 'locale', 'logging', 'logging.config', 'logging.handlers', 'lzma', 'macpath', 'mailbox', 'mailcap', 'marshal', 'math', 'mimetypes', 'mmap', 'modulefinder', 'msilib', 'msvcrt', 'multiprocessing', 'multiprocessing.connection', 'multiprocessing.dummy', 'multiprocessing.managers', 'multiprocessing.pool', 'multiprocessing.sharedctypes', 'netrc', 'nis', 'nntplib', 'numbers', 'operator', 'optparse', 'os', 'os.path', 'ossaudiodev', 'parser', 'pathlib', 'pdb', 'pickle', 'pickletools', 'pipes', 'pkgutil', 'platform', 'plistlib', 'poplib', 'posix', 'pprint', 'profile', 'pstats', 'pty', 'pwd', 'py_compile', 'pyclbr', 'pydoc', 'queue', 'quopri', 'random', 're', 'readline', 'reprlib', 'resource', 'rlcompleter', 'runpy', 'sched', 'secrets', 'select', 'selectors', 'shelve', 'shlex', 'shutil', 'signal', 'site', 'smtpd', 'smtplib', 'sndhdr', 'socket', 'socketserver', 'spwd', 'sqlite3', 'ssl', 'stat', 'statistics', 'string', 'stringprep', 'struct', 'subprocess', 'sunau', 'symbol', 'symtable', 'sys', 'sysconfig', 'syslog', 'tabnanny', 'tarfile', 'telnetlib', 'tempfile', 'termios', 'test', 'test.support', 'textwrap', 'threading', 'time', 'timeit', 'tkinter', 'tkinter.scrolledtext', 'tkinter.tix', 'tkinter.ttk', 'token', 'tokenize', 'trace', 'traceback', 'tracemalloc', 'tty', 'turtle', 'turtledemo', 'types', 'typing', 'unicodedata', 'unittest', 'unittest.mock', 'urllib', 'urllib.error', 'urllib.parse', 'urllib.request', 'urllib.response', 'urllib.robotparser', 'uu', 'uuid', 'venv', 'warnings', 'wave', 'weakref', 'webbrowser', 'winreg', 'winsound', 'wsgiref', 'wsgiref.handlers', 'wsgiref.headers', 'wsgiref.simple_server', 'wsgiref.util', 'wsgiref.validate', 'xdrlib', 'xml', 'xml.dom', 'xml.dom.minidom', 'xml.dom.pulldom', 'xml.etree.ElementTree', 'xml.parsers.expat', 'xml.parsers.expat.errors', 'xml.parsers.expat.model', 'xml.sax', 'xml.sax.handler', 'xml.sax.saxutils', 'xml.sax.xmlreader', 'xmlrpc.client', 'xmlrpc.server', 'zipapp', 'zipfile', 'zipimport', 'zlib']

def getImports(path):
   sys.path.insert(0, os.path.dirname(path))
   sizes = []
   imports = []
   sizes.append(os.stat(path).st_size)
   imp = []
   obj_loaded = {}
   for im in findimports.find_imports(path):
       imp.append(im)
   imports.extend(imp)
   mdls = list(filter(lambda x: x.name.split('.')[0] not in modulelist, imports))
   mdls = set(map(lambda x: x.name.split('.')[0], mdls))
   stdlibs = list(filter(lambda x: x.name.split('.')[0] in modulelist, imports))
   stdlibs = set(map(lambda x: x.name.split('.')[0], stdlibs))
   sub = set()
   for n in mdls:
       try:
           m = importlib.import_module(n)
           obj_loaded[n] = m
           #print(sys.getsizeof(m)) ??? 80 all
           if "site-packages" in str(m.__file__):
               stdlibs.add(n)
               sub.add(n)
       except Exception as e:
           print(e, 'here!')

   mdls = mdls - sub
   #print(m_with_addr)
  # getSizeMetrics(mdls_w_addr)
   return list(mdls), list(stdlibs), obj_loaded


def getSizeMetrics(planets):
    print(planets)

    #return (planet, size)
