import csv
import random

dataset_rows = []

fields = [
    'srcip',
    'srcport',
    'dstip',
    'dstport',
    'proto',
    'total_fpackets',
    'total_fvolume',
    'total_bpackets',
    'total_bvolume',
    'min_fpktl',
    'mean_fpktl',
    'max_fpktl',
    'std_fpktl',
    'min_bpktl',
    'mean_bpktl',
    'max_bpktl',
    'std_bpktl',
    'min_fiat',
    'mean_fiat',
    'max_fiat',
    'std_fiat',
    'min_biat',
    'mean_biat',
    'max_biat',
    'std_biat',
    'duration',
    'min_active',
    'mean_active',
    'max_active',
    'std_active',
    'min_idle',
    'mean_idle',
    'max_idle',
    'std_idle',
    'sflow_fpackets',
    'sflow_fbytes',
    'sflow_bpackets',
    'sflow_bbytes',
    'fpsh_cnt',
    'bpsh_cnt',
    'furg_cnt',
    'burg_cnt',
    'total_fhlen',
    'total_bhlen',
    'class'
]

with open('vpn_dataset.csv') as csv_file:
    # with open('vpn_dataset_filtered.csv',mode='w') as out_file:
    #     csv_writer = csv.writer(out_file)
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        # print(row[2])
        new_row = row
        new_row.append('1')
        dataset_rows.append(new_row)

with open('filtered_data_nvpn.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        new_row = row
        new_row.append('0')
        dataset_rows.append(new_row)


random.shuffle(dataset_rows)
print(len(dataset_rows[0]))
print(len(fields))

with open('dataset_for_mlp_full.csv','w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fields)
    csv_writer.writerows(dataset_rows)


