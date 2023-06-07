import os
import glob
import pandas as pd

path = '/Users/chuyangzhang/Downloads/20230607-Bioinformatics/'

CpG_output_filenames = glob.glob(path+ "/*CpGcluster.txt")
CpG_input_filenames = glob.glob(path+"/*.fa")

file_lists = []
for CpG_output_file in CpG_output_filenames:
    output_filename = CpG_output_file[:-19]
    for CpG_input_file in CpG_input_filenames:
        input_filename = CpG_input_file[:-3]
        if output_filename == input_filename:
            temp_list = [CpG_input_file, CpG_output_file]
            file_lists.append(temp_list)

output_file = open("EvolverInput.gff", "w")

for files in file_lists:
    CpG_input = open(files[0], "r")
    CpG_output = open(files[1], "r")

    name = CpG_input.readline()
    name_arr = name.split(" ")
    seq = CpG_input.readline()

    next(CpG_output)
    for lines in CpG_output:
        seqname = str(8)
        source = name_arr[1][:-1] + "_" + name_arr[0][1:]
        feature = "CpG"
        each_line = lines.split("\t")
        start = each_line[1]
        end = each_line[2]
        score = "."
        strand = "+"
        if name_arr[0][-4:] == "comp" and strand == "+":
            strand = "-"
        elif name_arr[0][-4:] == "comp" and strand == "-":
            strand = "+"
        frame = "."
        gene_name = name_arr[0][1:]
        CpG_seq = seq[int(start):int(end)+1]
        line = seqname + " " + source + " " + feature + " " + start + " " + end + " " + score + " " + strand + " " + frame + " " + "gene_name \"" + gene_name + "\"; sequence \"" + CpG_seq + "\";\n"
        output_file.write(line)


output_file.close()
