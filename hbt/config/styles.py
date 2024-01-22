# coding: utf-8

"""
Style definitions.
"""

import order as od


def stylize_processes(config: od.Config) -> None:
    """
    Adds process colors and adjust labels.
    """
    if config.has_process("hh_ggf_bbtautau"):
        config.processes.n.hh_ggf_bbtautau.color1 = (67, 118, 201)

    if config.has_process("h"):
        config.processes.n.h.color1 = (65, 180, 219)

    if config.has_process("tt"):
        config.processes.n.tt.color1 = (244, 182, 66)

    if config.has_process("st"):
        config.processes.n.st.color1 = (244, 93, 66)

    if config.has_process("dy"):
        config.processes.n.dy.color1 = (68, 186, 104)

    if config.has_process("vv"):
        config.processes.n.vv.color1 = (2, 24, 140)

    if config.has_process("qcd"):
        config.processes.n.qcd.color1 = (242, 149, 99)

    if config.has_process("graviton_hh_vbf_bbtautau_m400"):
        config.processes.n.graviton_hh_vbf_bbtautau_m400.label = r"Graviton $\rightarrow HH_{vbf,m400}$ $\rightarrow bb\tau\tau$"

    if config.has_process("graviton_hh_ggf_bbtautau_m400"):
        config.processes.n.graviton_hh_ggf_bbtautau_m400.label = r"Graviton $\rightarrow HH_{ggf,m400}$ $\rightarrow bb\tau\tau$"

    if config.has_process("graviton_hh_ggf_bbtautau_m1250"):
        config.processes.n.graviton_hh_ggf_bbtautau_m1250.label = r"Graviton $\rightarrow HH_{ggf,m1250}$ $\rightarrow bb\tau\tau$"

    config.cms_label = "Private work in progress"
