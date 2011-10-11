# BurgerVitrine
BurgerVitrine is a utility capable of turning JSON output from [Burger](https://github.com/sadimusi/Burger) or [Hamburglar](https://github.com/sadimusi/Hamburglar) into human-readable HTML.

## Usage
    $ vitrine.py [-b] [-r file] [-o file]
    $ vitrine.py -i | -t file [-o file]

### Options
* `-b`, `--body`: Don't generate a complete HTML document
* `-r`, `--resources file`: Path to resources folder
* `-o`, `--output file`: Output result into a file instead of standard output
* `-i`, `--items file`: Extract items.png from jar file
* `-t`, `--terrain file`: Extract terrain.png from jar file
* `-h`, `--help`: Show this help