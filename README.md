# Custom SRA toolkit

For downloading ftp pahts for fasatQ files of Sequence Read Archive (SRA) ids.
Input can either be a single SRA accession id ```-i``` or can be a file containing one or more SRA accession ids ```-f```.
An output file will be generated in the path specified in ```-o``` containing wget commands to download the fastQ files of the SRA ids.

## Usage
```bash
usage: sra_ftp_urls.py [-h] [-i SRA_ID] [-f FILE_IDS] -o OUTPUT_DIR

Download fastQ files from SRA accessions

optional arguments:
  -h, --help         show this help message and exit
  -i, --id           accession id of a SRA (e.g. SRR1778454)
  -f, --file-ids     path to file containing one or more SRA acessions ids
  -o, --output-dir   path to output dir
```

### Example (Linux)

- With a single SRA accession:
    ```bash
    python3 sra_ftp_urls.py --id SRR1778454 --output-dir /path/to/out/dir
    ```
- With a file containing multiple SRA accessions
     ```bash
    python3 sra_ftp_urls.py --file-ids /path/to/SRA_Accessions.txt --output-dir /path/to/out/dir
    ```