from collections import defaultdict
import json
import sys
from time import sleep

import rv.api as rv
import sunvox.api as sv
from sunvox.buffered import BufferedProcess


def find_note_periods():
    # Each frequency that has a corresponding period or note
    # will have one or both of 'period' or 'note' keys.
    freq_info = defaultdict(dict)
    # Build project
    project = rv.Project()
    filterpro = project.new_module(rv.m.FilterPro)
    freq_hz_ctl_num = filterpro.controllers['freq_hz'].number
    pitch2ctl = project.new_module(
        rv.m.Pitch2Ctl,
        out_controller=freq_hz_ctl_num,
    )
    multisynth = project.new_module(rv.m.MultiSynth)
    multisynth >> pitch2ctl >> filterpro
    # Build the map
    process = BufferedProcess(size=4096)
    try:
        slot = sv.Slot(project, process=process)
        # Iterate through all notes.
        for note in range(rv.NOTE.C0.value, rv.NOTE.B9.value + 1):
            slot.send_event(0, note, 1, multisynth, 0, 0)
            process.fill_buffer()
            hz = slot.get_module_ctl_value(
                mod_num=filterpro.index,
                ctl_num=freq_hz_ctl_num - 1,
                scaled=False,
            )
            freq_info[hz]['note'] = rv.NOTE(note)
        # Iterate through all pitches.
        for period in range(1, 0x8000 + 1):
            slot.send_event(0, rv.NOTECMD.SET_PITCH, 1, multisynth, 0, period)
            process.fill_buffer()
            hz = slot.get_module_ctl_value(
                mod_num=filterpro.index,
                ctl_num=freq_hz_ctl_num - 1,
                scaled=False,
            )
            freq_info[hz]['period'] = period
    finally:
        process.kill()
    for hz, info in list(freq_info.items()):
        # Only keep freqs that have both period and note
        if len(info) < 2:
            del freq_info[hz]
    print('====  =====  ======  ============')
    print('Note  Hz     Period  Period (hex)')
    print('====  =====  ======  ============')
    for hz, info in sorted(freq_info.items()):
        print('{:<4s}  {:<5d}  {:<6d}  {:04x}'.format(
            info['note'].name,
            hz,
            info['period'],
            info['period'],
        ))
    print('====  =====  ======  ============')
