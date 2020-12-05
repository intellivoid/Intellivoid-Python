# COA - Intellivoid Python API Authentication

This repository contains the open source parts of COA, Intellivoid's Python implementation of API Authentication.

The main source code is under `intellivoid/coa`

To install run `python3 -m pip install -r requirements.txt` and then `python3 setup.py install`.
Some usage examples are given under `examples/authentication`.

Python 3.6 or above is needed. The COA interface is provided both an asynchronous and a synchronous
implementation, to avoid issues when integrating this library in highly concurrent systems.

The synchronous package lies in `intellivoid.coa.sync`, while the async one resides in `intellivoid.coa.aio`.
The packages are specular and their methods and contents are identical, except for the async part.

Feel free to file an issue if you find bugs and to contribute code via pull requests, but note that
low quality or low effort contributions will be ignored.

## WORK IN PROGRESS

This project is not completed as it's currently being used to test the internal development
builds of Intellivoid API. Incomplete code and or bugs may be a frequent yet expected occurrence
in this project until the first version is officially released.

## Credits

This library is developed by and copyrighted by Zi Xing Narrakas and/or Intellivoid and may only be used in compliance with the
included license, which you can find in this repo inside the LICENSE file.

## License

```
Licensed under GPL v3. See the LICENSE for more information.
```
