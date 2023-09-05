# coding: utf-8

"""
ML models derived from the *SimpleDNN* class
"""


from hbt.ml.first_nn import SimpleDNN


processes = [
    "graviton_hh_ggf_bbtautau_m400",
    "hh_ggf_bbtautau",
    "graviton_hh_vbf_bbtautau_m400",
    "graviton_hh_ggf_bbtautau_m1250",
]

ml_process_weights = {
    "graviton_hh_ggf_bbtautau_m400": 1.5,
    "hh_ggf_bbtautau": 1,
    "graviton_hh_vbf_bbtautau_m400": 1,
    "graviton_hh_ggf_bbtautau_m1250": 1,
}

dataset_names = {
    "graviton_hh_ggf_bbtautau_m400_madgraph",
    "hh_ggf_bbtautau_madgraph",
    "graviton_hh_vbf_bbtautau_m400_madgraph",
    "graviton_hh_ggf_bbtautau_m1250_madgraph",
}

# feature_list = ["pt", "eta", "phi", "mass", "e", "btag", "hadronFlavour"]

# input_features = [
#     [f"{obj}_{var}"
#     for obj in [f"jet{i}" for i in range(1, 7, 1)]
#     for var in feature_list],
#     ["mjj", "mbjetbjet", "mtautau", "mHH"]]

input_features = [["Colljets_pt", "Colljets_e", "Colljets_mass", "Colljets_eta", "Colljets_phi", "Colljets_btag"],
                  ["mjj", "mbjetbjet", "mtautau", "mHH", "jets_max_d_eta", "jets_d_eta_inv_mass",
                   "ht", "n_jets"]]

norm_features = [["Colljets_pt", "Colljets_e", "Colljets_mass", "Colljets_eta", "Colljets_phi", "Colljets_btag"],
                  ["mjj", "mbjetbjet", "mtautau", "mHH", "jets_max_d_eta", "jets_d_eta_inv_mass",
                   "ht", "n_jets"]]
# Decide on dummy or proper btag of jets: If proper chosen coment out 4 lines below
# for i, name in enumerate(input_features[0]):
#     if name == 'jet1_btag' or name == 'jet2_btag':
#         name += "_dummy"
#         input_features[0][i] = name


# empty_overwrite options: "1": -1, "3sig": 3 sigma padding as replacement of EMPTY FLOAT values
# baseline_jets: max number of jets considered
# model_type: baseline-> baselie model used else deepsets
# quantity_weighting: weighting of the processes accroding to the amount of samples for each samples
default_cls_dict = {
    "folds": 3,
    # "max_events": 10**6,  # TODO
    "layers": [512, 512, 512],
    "activation": "relu",  # Options: elu, relu, prelu, selu, tanh, softmax
    "learningrate": 0.01,
    "batchsize": 256,
    "epochs": 150,
    "eqweight": True,
    "dropout": 0.50,
    "processes": processes,
    "ml_process_weights": ml_process_weights,
    "dataset_names": dataset_names,
    "input_features": input_features,
    "store_name": "inputs1",
    "n_features": len(input_features[0]),
    "n_output_nodes": len(processes),
    "batch_norm_deepSets": True,
    "batch_norm_ff": True,
    "aggregations": ["Sum", "Max", "Mean"],
    "L2": False,
    "norm_features": norm_features,
    "empty_overwrite": "1",
    "quantity_weighting": True,
    "jet_num_cut": 1,
    "baseline_jets": 4,
    "model_type": 'baseline',
}

nodes_deepSets_op = default_cls_dict["baseline_jets"] * default_cls_dict["n_features"]
nodes_deepSets = [256, 256, 256, 128, 128, nodes_deepSets_op]
nodes_ff = [256, 256, 256, 256, 256, 256]

# derived model, usable on command line
default_dnn = SimpleDNN.derive("default", cls_dict=default_cls_dict)

# test model settings
cls_dict = default_cls_dict
cls_dict["model_name"] = f"{len(processes)}classes_baseline"
cls_dict["nodes_deepSets"] = nodes_deepSets
cls_dict["nodes_ff"] = nodes_ff
cls_dict["activation_func_deepSets"] = ["selu" for i in range(len(nodes_deepSets))]
cls_dict["activation_func_ff"] = ["selu" for i in range(len(nodes_ff))]

test_dnn = SimpleDNN.derive("test", cls_dict=cls_dict)

# 2classes_vbfjets_dr_inv_mass
# 2classes_vbfjets
# 3classes_vbfjets
# 3classes_vbfjets_dr_inv_mass
# 3classes_no_vbf
