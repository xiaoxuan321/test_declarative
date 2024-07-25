import gzip
import shutil
import os
import pm4py
import time
import sys

if __name__ == "__main__":

    BPIC12_output_file = '/app/data/BPIC12.xes'
    BPIC13_cp_output_file = '/app/data/BPIC13_cp.xes'
    BPIC13_i_output_file = '/app/data/BPIC13_i.xes'
    BPIC14_f_output_file = '/app/data/BPIC14_f.xes'
    BPIC15_1f_output_file = '/app/data/BPIC15_1f.xes'
    BPIC15_2f_output_file = '/app/data/BPIC15_2f.xes'
    BPIC15_3f_output_file = '/app/data/BPIC15_3f.xes'
    BPIC15_4f_output_file = '/app/data/BPIC15_4f.xes'
    BPIC15_5f_output_file = '/app/data/BPIC15_5f.xes'
    BPIC17_f_output_file = '/app/data/BPIC17_f.xes'
    RTFMP_output_file = '/app/data/RTFMP.xes'
    SEPSIS_output_file = '/app/data/SEPSIS.xes'
    # 加载解压后的 .xes 文件
    BPIC12 = pm4py.read_xes(BPIC12_output_file)
    BPIC13_cp = pm4py.read_xes(BPIC13_cp_output_file)
    BPIC13_i = pm4py.read_xes(BPIC13_i_output_file)
    BPIC14_f = pm4py.read_xes(BPIC14_f_output_file)
    BPIC15_1f = pm4py.read_xes(BPIC15_1f_output_file)
    BPIC15_2f = pm4py.read_xes(BPIC15_2f_output_file)
    BPIC15_3f = pm4py.read_xes(BPIC15_3f_output_file)
    BPIC15_4f = pm4py.read_xes(BPIC15_4f_output_file)
    BPIC15_5f = pm4py.read_xes(BPIC15_5f_output_file)
    BPIC17_f = pm4py.read_xes(BPIC17_f_output_file)
    RTFMP = pm4py.read_xes(RTFMP_output_file)
    SEPSIS = pm4py.read_xes(SEPSIS_output_file)

    if len(sys.argv) > 1:
        # 获取第一个命令行参数
        param = sys.argv[1]
        print(f"第一个命令行参数是: {param}")
        if param == "inductive_petri":
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC12, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC13_cp, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC13_i, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC14_f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_1f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_2f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_3f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_4f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC15_5f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            net, im, fm = pm4py.discover_petri_net_inductive(BPIC17_f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            net, im, fm = pm4py.discover_petri_net_inductive(RTFMP, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            net, im, fm = pm4py.discover_petri_net_inductive(SEPSIS, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

        elif param == "inductive_process_tree":
            process_tree = pm4py.discover_process_tree_inductive(BPIC12, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC13_cp, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC13_i, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC14_f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC15_1f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC15_2f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC15_3f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC15_4f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC15_5f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(BPIC17_f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(RTFMP, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            process_tree = pm4py.discover_process_tree_inductive(SEPSIS, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')


        elif param == "inductive_bpmn":
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC12, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC13_cp, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC13_i, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC14_f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC15_1f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC15_2f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC15_3f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC15_4f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC15_5f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(BPIC17_f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(RTFMP, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            bpmn_graph = pm4py.discover_bpmn_inductive(SEPSIS, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

        elif param == "temporal_profile":
            # discovers a temporal profile
            temporal_profile = pm4py.discover_temporal_profile(BPIC12, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC13_cp, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC13_i, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC14_f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC15_1f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC15_2f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC15_3f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC15_4f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC15_5f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(BPIC17_f, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(RTFMP, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')
            temporal_profile = pm4py.discover_temporal_profile(SEPSIS, activity_key='concept:name', case_id_key='case:concept:name', timestamp_key='time:timestamp')

        elif param == "log_skeleton":
            # discovers a temporal profile
            log_skeleton = pm4py.discover_log_skeleton(BPIC12, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC13_cp, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC13_i, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC14_f, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_1f, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_2f, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_3f, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_4f, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC15_5f, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(BPIC17_f, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(RTFMP, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
            log_skeleton = pm4py.discover_log_skeleton(SEPSIS, noise_threshold=0.1, activity_key='concept:name',
                                                       case_id_key='case:concept:name', timestamp_key='time:timestamp')
        elif param == "declare":
            # discovers a temporal profile
            declare_model = pm4py.discover_declare(BPIC12)
            declare_model = pm4py.discover_declare(BPIC13_cp)
            declare_model = pm4py.discover_declare(BPIC13_i)
            declare_model = pm4py.discover_declare(BPIC14_f)
            declare_model = pm4py.discover_declare(BPIC15_1f)
            declare_model = pm4py.discover_declare(BPIC15_2f)
            declare_model = pm4py.discover_declare(BPIC15_3f)
            declare_model = pm4py.discover_declare(BPIC15_4f)
            declare_model = pm4py.discover_declare(BPIC15_5f)
            declare_model = pm4py.discover_declare(BPIC17_f)
            declare_model = pm4py.discover_declare(RTFMP)
            declare_model = pm4py.discover_declare(SEPSIS)








    else:
        print("没有提供任何命令行参数")
