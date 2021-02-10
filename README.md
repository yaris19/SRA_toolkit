# Custom SRA toolkit

For downloading ftp pahts for fasatQ files of Sequence Read Archive (SRA) ids.
Input can either be a single SRA id ```--id``` or can be a list containing one or more SRA ids ```--file-ids```.
An output file will be generated in the path specified in ```output-dir``` containing wget commands to download the fastQ files of the SRA ids.

Usage:
```bash
usage: sra_ftp_urls.py [-h] [--id SRA_ID] [--file-ids FILE_IDS] --output-dir OUTPUT_DIR

Download fastQ files from SRA with a (list of) SRA id(s)

optional arguments:
  -h, --help                show this help message and exit
  --id SRA_ID               id of a SRA (e.g. SRR1778454)
  --file-ids FILE_IDS       path to file containing one or more SRA's
  --output-dir OUTPUT_DIR   path to output dir
```

