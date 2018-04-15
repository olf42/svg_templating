# SVG Templating

This Project is to demostrate a very basic svg templating workflow.
It can help to batch process lots of data into svg files.

Works with Python 3.6.

## Installation

After cloning the repository, please install the requirements

```zsh
pip install -r requirements.txt
```

## Usage

Modify the code to your needs, and run it by executing

```zsh
python svg_templating.py
```

## Postprocessing


Sometimes output in the pdf format might be required. This can be achieved
by using *convert* and a for-loop.

```zsh
for file in *.svg; do; convert ${file} `basename ${file} .jpg`.pdf; done
```

To combine all output pdfs into one file (e.g. for printing) *pdfjam/pdfjoin* can be used.

```zsh
pdfjoin dnb-dbsm-boe-bl-p-00*.pdf --outfile cards.pdf
```

Please note, that you have to adapt the first part of the filename wildcard to your needs, 
if you happen to choose different files.

## Know Issues

All Files to be put in the template should have the same/similar 
aspect ratios. Otherwise, they will be stretched to match the
aspect ratio defined in the template. 

Preprocessing can be made with [imagemagick](https://imagemagick.org) command line tools
like *mogrify*.

## License

GNU General Public License v3

## Copyright

2018, [Universitätsbibliothek Leipzig](https://ub.uni-leipzig.de)

## Author

Florian Rämisch <raemisch@ub.uni-leipzig.de



