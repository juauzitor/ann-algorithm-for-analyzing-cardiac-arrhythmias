# Copyright (C) [2024] [João Vitor Mendes Pinto dos Santos]

# This file is part of [ann-model-for-analyzing-cardiac-arrhythmias] and is licensed under
# the Academic Free License version 3.0. For details, see the LICENSE file
# at the root of this project or <https://opensource.org/licenses/AFL-3.0>.

class EcgRecord:
    def __init__(self, record_header):
        self.record_number = record_header.__dict__['record_name']
        self.fs = record_header.__dict__['fs']
        self.n_sig = record_header.__dict__['n_sig']
        self.lead = record_header.__dict__['sig_name']
        self.unit = record_header.__dict__['units']
        self.gender = record_header.__dict__['comments'][0].split(' ')[1]
        self.age = record_header.__dict__['comments'][0].split(' ')[0]
        record_header.__dict__['comments'].pop(0)
        self.medication = record_header.__dict__['comments']

    def __str__(self):
        leads_info = ', '.join([f"{lead} ({unit})" for lead, unit in zip(self.lead, self.unit)])
        return (f"ECG Record {self.record_number}\n"
                f"Sampling Frequency: {self.fs} Hz\n"
                f"Number of Signals: {self.n_sig}\n"
                f"Leads: {leads_info}\n"
                f"Gender: {self.gender}\n"
                f"Age: {self.age}\n"
                f"Medications: {self.medication}")
