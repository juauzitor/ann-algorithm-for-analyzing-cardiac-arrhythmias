# Copyright (C) [2024] [João Vitor Mendes Pinto dos Santos]

# This file is part of [ann-model-for-analyzing-cardiac-arrhythmias] and is licensed under
# the Academic Free License version 3.0. For details, see the LICENSE file
# at the root of this project or <https://opensource.org/licenses/AFL-3.0>.

import re
import wfdb
import glob
import pandas as pd
import numpy as np

class EcgRecord:
    def __init__(self, record_header, record_signal):
        self.record_number = record_header.__dict__['record_name']
        self.fs = record_header.__dict__['fs']
        self.n_sig = record_header.__dict__['n_sig']
        self.lead = record_header.__dict__['sig_name']
        self.unit = record_header.__dict__['units']
        self.gender = record_header.__dict__['comments'][0].split(' ')[1]
        self.age = record_header.__dict__['comments'][0].split(' ')[0]
        record_header.__dict__['comments'].pop(0)
        self.medication = record_header.__dict__['comments']
        self.record_signal = record_signal

    def __str__(self):
        leads_info = ', '.join([f"{lead} ({unit})" for lead, unit in zip(self.lead, self.unit)])
        return (f"ECG Record {self.record_number}\n"
                f"Sampling Frequency: {self.fs} Hz\n"
                f"Number of Signals: {self.n_sig}\n"
                f"Leads: {leads_info}\n"
                f"Gender: {self.gender}\n"
                f"Age: {self.age}\n"
                f"Medications: {self.medication}")

def import_data():
    mitbih_records = []
    for record in glob.glob("../mitdb/*.dat"):
        record_num = re.findall(r'\d+', record)[0]
        record_header = wfdb.rdheader(f'../mitdb/{record_num}')
        record = wfdb.rdrecord(f'../mitdb/{record_num}')
        data = {}
        for j in range(record_header.__dict__['n_sig']):
            data[record_header.__dict__['sig_name'][j]] = array_df = record.p_signal[:,j]
        record_signal = pd.DataFrame(data)
        mitbih_records.append(EcgRecord(record_header, record_signal))
    return mitbih_records
