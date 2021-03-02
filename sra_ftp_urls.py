import argparse
import sys
from os import chmod

import requests

parser = argparse.ArgumentParser(
    description="Download fastQ files from SRA with a (list of) SRA id(s)")
parser.add_argument("--id", default="", dest="sra_id", type=str,
                    help="id of a SRA (e.g. SRR1778454)")
parser.add_argument("--file-ids", dest="file_ids", type=argparse.FileType("r"),
                    help="path to file containing one or more SRA's")
parser.add_argument("--output-dir", dest="output_dir", required=True, type=str,
                    help="path to output dir")


def parse_args(parser):
    args = parser.parse_args()
    if not args.sra_id and not args.file_ids:
        raise ValueError("Please specify either --id or --file-ids")

    if args.sra_id and args.file_ids:
        raise ValueError(
            "Don't specify both --id and --file-ids, only specify one")

    return args


def get_ftp_file_path(input_sra):
    sra_explorer_url = "https://www.ebi.ac.uk/ena/portal/api/filereport?result=read_run&fields=fastq_ftp&format=JSON&accession={}"

    if type(input_sra) == str:
        r = requests.get(sra_explorer_url.format(input_sra))
        data = r.json()
        return data[0]["fastq_ftp"].split(";")

    sra_ids = [line.strip() for line in input_sra.readlines() if line.strip()]

    fastq_paths = []
    for i, sra_id in zip(
            progressbar(sra_ids, prefix="Downloading files: ", size=40),
            sra_ids):
        r = requests.get(sra_explorer_url.format(sra_id))
        data = r.json()
        fastq_paths.extend(data[0]["fastq_ftp"].split(";"))

    return fastq_paths


def write_commands_to_file(ftp_paths, output_dir):
    out_file = f"{output_dir}/wget_commands_sra_paths.sh"

    if " " in output_dir:
        output_dir = f"'{output_dir}'"

    with open(out_file, "w") as f:
        f.write("!/usr/bin/bash\n")
        for ftp_path in ftp_paths:
            ftp_path = f"ftp://{ftp_path}"
            f.write(f"wget -P {output_dir} {ftp_path} \n")

    # make bash file executable
    chmod(out_file, 0o777)
    return out_file


def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size * j / count)
        file.write(
            "%s[%s%s] %i/%i\r" % (prefix, "#" * x, "." * (size - x), j, count))
        file.flush()

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    file.write("\n")
    file.flush()


if __name__ == "__main__":
    args = parse_args(parser)
    ftp_paths = get_ftp_file_path(
        args.sra_id.strip() if args.sra_id.strip() else args.file_ids)
    out_file = write_commands_to_file(ftp_paths, args.output_dir)
