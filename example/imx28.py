"""DRAM registers' definition of i.MX28"""

from functools import reduce
from uint import Register


regs_range = [range(0, 8), range(16, 30), range(31, 59), range(66, 86), range(87, 95), range(162, 190)]
regs_range = reduce(lambda a, b: a + list(b), regs_range, [])
regs = {f'{k}': Register(f'hw_dram_ctl{k:02}') for k in regs_range}

# hw_dram_ctl00
regs["0"][31:3] = 'user_def_reg_0_1'
regs["0"][2] = 'cke_select'
regs["0"][1] = 'srefresh_enter'
regs["0"][0] = 'bresp_timing'

# hw_dram_ctl01: AXI monitor control
# hw_dram_ctl02 ~ 07: user-defined registers
# hw_dram_ctl08 ~ 15: AXI0,1,2 debug (RO)

# hw_dram_ctl16
regs["16"][24] = 'write_modereg'
regs["16"][16] = 'power_down'
regs["16"][0] = 'start'

# hw_dram_ctl17
regs["17"][24] = 'auto_refresh_mode'
regs["17"][16] = 'arefresh'
regs["17"][8] = 'enable_quick_srefresh'
regs["17"][0] = 'srefresh'

# hw_dram_ctl21
regs["21"][26:24] = 'cke_delay'
regs["21"][23:16] = 'dll_lock'
regs["21"][8] = 'dlllockreg'
regs["21"][0] = 'dll_bypass_mode'

# hw_dram_ctl22
regs["22"][19:16] = 'lowpower_refresh_enable'
regs["22"][12:8] = 'lowpower_control'
regs["22"][4:0] = 'lowpower_auto_enable'

# hw_dram_ctl23
regs["23"][31:16] = 'lowpower_internal_cnt'
regs["23"][15:0] = 'lowpower_external_cnt'

# hw_dram_ctl24
regs["24"][31:16] = 'lowpower_self_refresh_cnt'
regs["24"][15:0] = 'lowpower_refresh_hold'

# hw_dram_ctl25
regs["25"][15:0] = 'lowpower_power_down_cnt'

# hw_dram_ctl26
regs["26"][16] = 'priority_en'
regs["26"][8] = 'addr_cmp_en'
regs["26"][0] = 'placement_en'

# hw_dram_ctl27
regs["27"][24] = 'swap_port_rw_same_en'
regs["27"][16] = 'swap_en'
regs["27"][8] = 'bank_split_en'
regs["27"][0] = 'rw_same_en'

# hw_dram_ctl28
regs["28"][26:24] = 'q_fullness'
regs["28"][19:16] = 'age_count'
regs["28"][11:8] = 'command_age_count'
regs["28"][0] = 'active_aging'

# hw_dram_ctl29
regs["29"][27:24] = 'cs_map'
regs["29"][18:16] = 'column_size'
regs["29"][10:8] = 'addr_pins'
regs["29"][3:0] = 'aprebit'

# hw_dram_ctl30: RO

# hw_dram_ctl31
regs["31"][16] = 'eight_bank_mode'
regs["31"][8] = 'drive_dq_dqs'
regs["31"][0] = 'dqs_n_en'

# hw_dram_ctl32
regs["32"][8] = 'reduc'
regs["32"][0] = 'reg_dimm_enable'

# hw_dram_ctl33
regs["33"][8] = 'concurrentap'
regs["33"][0] = 'ap'

# hw_dram_ctl34
regs["34"][24] = 'writeinterp'
regs["34"][16] = 'intrptwritea'
regs["34"][8] = 'intrptreada'
regs["34"][0] = 'intrptapburst'

# hw_dram_ctl35
regs["35"][16] = 'pwrup_srefresh_exit'
regs["35"][8] = 'no_cmd_init'
regs["35"][3:0] = 'initaref'

# hw_dram_ctl36
regs["36"][24] = 'tref_enable'
regs["36"][16] = 'tras_lockout'
regs["36"][0] = 'fast_write'

# hw_dram_ctl37
regs["37"][27:24] = 'caslat_lin_gate'
regs["37"][19:16] = 'caslat_lin'
regs["37"][10:8] = 'caslat'
regs["37"][3:0] = 'wrlat'

# hw_dram_ctl38
regs["38"][28:24] = 'tdal'
regs["38"][23:8] = 'tcpd'
regs["38"][2:0] = 'tcke'

# hw_dram_ctl39
regs["39"][29:24] = 'tfaw'
regs["39"][15:0] = 'tdll'

# hw_dram_ctl40
regs["40"][28:24] = 'tmrd'
regs["40"][23:0] = 'tinit'

# hw_dram_ctl41
regs["41"][31:16] = 'tpdex'  # tPDEX = 2*tCK + tIS?
regs["41"][15:8] = 'trcd_int'
regs["41"][5:0] = 'trc'

# hw_dram_ctl42
regs["42"][23:8] = 'tras_max'
regs["42"][7:0] = 'tras_min'

# hw_dram_ctl43
regs["43"][27:24] = 'trp'
regs["43"][23:16] = 'trfc'
regs["43"][13:0] = 'tref'

# hw_dram_ctl44
regs["44"][27:24] = 'twtr'
regs["44"][20:16] = 'twr_int'
regs["44"][10:8] = 'trtp'
regs["44"][2:0] = 'trrd'

# hw_dram_ctl45
regs["45"][31:16] = 'txsr'
regs["45"][15:0] = 'txsnr'

# hw_dram_ctl48
regs["48"][16] = 'axi0_bdw_ovflow'
regs["48"][14:8] = 'axi0_bdw'
regs["48"][1:0] = 'axi0_fifo_type_reg'

# hw_dram_ctl49
regs["49"][31:16] = 'axi0_en_size_lt_width_instr'
regs["49"][10:8] = 'axi0_w_priority'
regs["49"][2:0] = 'axi0_r_priority'

# hw_dram_ctl50
regs["50"][16] = 'axi1_bdw_ovflow'
regs["50"][14:8] = 'axi1_bdw'
regs["50"][1:0] = 'axi1_fifo_type_reg'

# hw_dram_ctl51
regs["51"][31:16] = 'axi1_en_size_lt_width_instr'
regs["51"][10:8] = 'axi1_w_priority'
regs["51"][2:0] = 'axi1_r_priority'

# hw_dram_ctl52
regs["52"][16] = 'axi2_bdw_ovflow'
regs["52"][14:8] = 'axi2_bdw'
regs["52"][1:0] = 'axi2_fifo_type_reg'

# hw_dram_ctl53
regs["53"][31:16] = 'axi2_en_size_lt_width_instr'
regs["53"][10:8] = 'axi2_w_priority'
regs["53"][2:0] = 'axi2_r_priority'

# hw_dram_ctl54
regs["54"][16] = 'axi3_bdw_ovflow'
regs["54"][14:8] = 'axi3_bdw'
regs["52"][1:0] = 'axi3_fifo_type_reg'

# hw_dram_ctl55
regs["55"][31:16] = 'axi3_en_size_lt_width_instr'
regs["55"][10:8] = 'axi3_w_priority'
regs["55"][2:0] = 'axi3_r_priority'

# hw_dram_ctl56
regs["56"][2:0] = 'arb_cmd_q_threshold'

# hw_dram_ctl58
regs["58"][10:0] = 'int_mask'

# hw_dram_ctl59 ~ 65: RO

# hw_dram_ctl66
regs["66"][19:16] = 'tdfi_ctrlupd_min'
regs["66"][13:0] = 'tdfi_ctrlupd_max'

# hw_dram_ctl67
regs["67"][27:24] = 'tdfi_dram_clk_enable'
regs["67"][18:16] = 'tdfi_dram_clk_disable'
regs["67"][11:8] = 'dram_clk_enable'
regs["67"][3:0] = 'tdfi_ctrl_delay'

# hw_dram_ctl68
regs["68"][29:16] = 'tdfi_phyupd_type0'
regs["68"][13:0] = 'tdfi_phyupd_resp'

# hw_dram_ctl69
regs["69"][11:8] = 'tdfi_phy_wrlat_base'

# hw_dram_ctl70
regs["70"][19:16] = 'tdfi_rddata_en_base'
regs["70"][3:0] = 'tdfi_phy_rdlat'

# hw_dram_ctl71
regs["71"][31] = 'dyn_term_sel'
regs["71"][29] = 'term_en'
regs["71"][28] = 'echo_gate_ctrl'
regs["71"][27] = 'gather_fifo_en'
regs["71"][26:24] = 'rd_data_delay'
regs["71"][20] = 'pad_output_en_pol'
regs["71"][16] = 'sub_dqs_gate_val'
regs["71"][15:12] = 'adj_dqs_out_en_window_start'
regs["71"][11:8] = 'adj_dqs_out_en_window_end'
regs["71"][6:4] = 'adj_dq_out_en_window_start'
regs["71"][2:0] = 'adj_dq_out_en_window_end'

# hw_dram_ctl72
regs["72"][31] = 'dyn_term_sel'
regs["72"][29] = 'term_en'
regs["72"][28] = 'echo_gate_ctrl'
regs["72"][27] = 'gather_fifo_en'
regs["72"][26:24] = 'rd_data_delay'
regs["72"][20] = 'pad_output_en_pol'
regs["72"][16] = 'sub_dqs_gate_val'
regs["72"][15:12] = 'adj_dqs_out_en_window_start'
regs["72"][11:8] = 'adj_dqs_out_en_window_end'
regs["72"][6:4] = 'adj_dq_out_en_window_start'
regs["72"][2:0] = 'adj_dq_out_en_window_end'

# hw_dram_ctl73
regs["73"][31] = 'dyn_term_sel'
regs["73"][29] = 'term_en'
regs["73"][28] = 'echo_gate_ctrl'
regs["73"][27] = 'gather_fifo_en'
regs["73"][26:24] = 'rd_data_delay'
regs["73"][20] = 'pad_output_en_pol'
regs["73"][16] = 'sub_dqs_gate_val'
regs["73"][15:12] = 'adj_dqs_out_en_window_start'
regs["73"][11:8] = 'adj_dqs_out_en_window_end'
regs["73"][6:4] = 'adj_dq_out_en_window_start'
regs["73"][2:0] = 'adj_dq_out_en_window_end'

# hw_dram_ctl74
regs["74"][31] = 'dyn_term_sel'
regs["74"][29] = 'term_en'
regs["74"][28] = 'echo_gate_ctrl'
regs["74"][27] = 'gather_fifo_en'
regs["74"][26:24] = 'rd_data_delay'
regs["74"][20] = 'pad_output_en_pol'
regs["74"][16] = 'sub_dqs_gate_val'
regs["74"][15:12] = 'adj_dqs_out_en_window_start'
regs["74"][11:8] = 'adj_dqs_out_en_window_end'
regs["74"][6:4] = 'adj_dq_out_en_window_start'
regs["74"][2:0] = 'adj_dq_out_en_window_end'

# hw_dram_ctl75
regs["75"][31:28] = 'dyn_term_sel_en_t'
regs["75"][27:24] = 'dyn_term_sel_di_t'
regs["75"][23] = 'en_dyn_term_sel'
regs["75"][22] = 'tsel_pol'
regs["75"][21] = 'trig_d_ret'
regs["75"][20] = 'sel_data_out_type'
regs["75"][19:18] = 'loopback_ctrl'
regs["75"][17] = 'loop_rd_mux'
regs["75"][16] = 'wr_mux'
regs["75"][14:12] = 'cyc_delay'
regs["75"][10:8] = 'gate_err_delay'
regs["75"][5:4] = 'gate_close'
regs["75"][2:0] = 'gate_open_t_adj'

# hw_dram_ctl76
regs["76"][31:28] = 'dyn_term_sel_en_t'
regs["76"][27:24] = 'dyn_term_sel_di_t'
regs["76"][23] = 'en_dyn_term_sel'
regs["76"][22] = 'tsel_pol'
regs["76"][21] = 'trig_d_ret'
regs["76"][20] = 'sel_data_out_type'
regs["76"][19:18] = 'loopback_ctrl'
regs["76"][17] = 'loop_rd_mux'
regs["76"][16] = 'wr_mux'
regs["76"][14:12] = 'cyc_delay'
regs["76"][10:8] = 'gate_err_delay'
regs["76"][5:4] = 'gate_close'
regs["76"][2:0] = 'gate_open_t_adj'

# hw_dram_ctl77
regs["77"][31:28] = 'dyn_term_sel_en_t'
regs["77"][27:24] = 'dyn_term_sel_di_t'
regs["77"][23] = 'en_dyn_term_sel'
regs["77"][22] = 'tsel_pol'
regs["77"][21] = 'trig_d_ret'
regs["77"][20] = 'sel_data_out_type'
regs["77"][19:18] = 'loopback_ctrl'
regs["77"][17] = 'loop_rd_mux'
regs["77"][16] = 'wr_mux'
regs["77"][14:12] = 'cyc_delay'
regs["77"][10:8] = 'gate_err_delay'
regs["77"][5:4] = 'gate_close'
regs["77"][2:0] = 'gate_open_t_adj'

# hw_dram_ctl78
regs["78"][31:28] = 'dyn_term_sel_en_t'
regs["78"][27:24] = 'dyn_term_sel_di_t'
regs["78"][23] = 'en_dyn_term_sel'
regs["78"][22] = 'tsel_pol'
regs["78"][21] = 'trig_d_ret'
regs["78"][20] = 'sel_data_out_type'
regs["78"][19:18] = 'loopback_ctrl'
regs["78"][17] = 'loop_rd_mux'
regs["78"][16] = 'wr_mux'
regs["78"][14:12] = 'cyc_delay'
regs["78"][10:8] = 'gate_err_delay'
regs["78"][5:4] = 'gate_close'
regs["78"][2:0] = 'gate_open_t_adj'

# hw_dram_ctl79
regs["79"][25] = 'addr_cmd_path'
regs["79"][24] = 'wr_latency_path'
regs["79"][23] = 'dfi_ctrl_mobile_mc'
regs["79"][5] = 'en_pad_in'
regs["79"][4] = 'en_pad_out'
regs["79"][3:0] = 'dfi_rddata_valid_delay'

# hw_dram_ctl80
regs["80"][2:1] = 'en_phy_test'

# hw_dram_ctl81
regs["81"][12:8] = 'ocd_adjust_pup_cs_0'
regs["81"][4:0] = 'ocd_adjust_pdn_cs_0'

# hw_dram_ctl82
regs["82"][24] = 'odt_alt_en'

# hw_dram_ctl83
regs["83"][27:24] = 'odt_rd_map_cs3'
regs["83"][19:16] = 'odt_rd_map_cs2'
regs["83"][11:8] = 'odt_rd_map_cs1'
regs["83"][3:0] = 'odt_rd_map_cs0'

# hw_dram_ctl84
regs["84"][27:24] = 'odt_wr_map_cs3'
regs["84"][19:16] = 'odt_wr_map_cs2'
regs["84"][11:8] = 'odt_wr_map_cs1'
regs["84"][3:0] = 'odt_wr_map_cs0'

# hw_dram_ctl85
regs["85"][12] = 'pad_impedance_par'
regs["85"][8] = 'pad_type'
regs["85"][5] = 'iddq_rx_sig'
regs["85"][4] = 'iddq_tx_sig'
regs["85"][1] = 'iddq_rx_clk'
regs["85"][0] = 'iddq_tx_clk'

# hw_dram_ctl86: RO

# hw_dram_ctl87
regs["87"][28] = 'dll_bypass_ctrl'
regs["87"][23:15] = 'read_dqs_delay_bypass'
regs["87"][14:8] = 'read_dqs_delay_normal'
regs["87"][7:0] = 'dll_start_point_ctrl'

# hw_dram_ctl88
regs["88"][28] = 'dll_bypass_ctrl'
regs["88"][23:15] = 'read_dqs_delay_bypass'
regs["88"][14:8] = 'read_dqs_delay_normal'
regs["88"][7:0] = 'dll_start_point_ctrl'

# hw_dram_ctl89
regs["89"][28] = 'dll_bypass_ctrl'
regs["89"][23:15] = 'read_dqs_delay_bypass'
regs["89"][14:8] = 'read_dqs_delay_normal'
regs["89"][7:0] = 'dll_start_point_ctrl'

# hw_dram_ctl90
regs["90"][28] = 'dll_bypass_ctrl'
regs["90"][23:15] = 'read_dqs_delay_bypass'
regs["90"][14:8] = 'read_dqs_delay_normal'
regs["90"][7:0] = 'dll_start_point_ctrl'

# hw_dram_ctl91
regs["91"][23:15] = 'clk_wr_delay_bypass'
regs["91"][14:8] = 'clk_wr_delay_normal'
regs["91"][7:0] = 'dll_incr_val'

# hw_dram_ctl92
regs["92"][23:15] = 'clk_wr_delay_bypass'
regs["92"][14:8] = 'clk_wr_delay_normal'
regs["92"][7:0] = 'dll_incr_val'

# hw_dram_ctl93
regs["93"][23:15] = 'clk_wr_delay_bypass'
regs["93"][14:8] = 'clk_wr_delay_normal'
regs["93"][7:0] = 'dll_incr_val'

# hw_dram_ctl94
regs["94"][23:15] = 'clk_wr_delay_bypass'
regs["94"][14:8] = 'clk_wr_delay_normal'
regs["94"][7:0] = 'dll_incr_val'

# hw_dram_ctl95 ~ 161: RO

# hw_dram_ctl162
regs["162"][26:24] = 'w2r_samecs_dly'
regs["162"][18:16] = 'w2r_diffcs_dly'
regs["162"][8:0] = 'dll_obs_reg_3_3'

# hw_dram_ctl163
regs["163"][31:24] = 'dll_rst_adj_dly'
regs["163"][19:16] = 'wrlat_adj'
regs["163"][11:8] = 'rdlat_adj'
regs["163"][3:0] = 'dram_class'

# hw_dram_ctl164
regs["164"][17:8] = 'int_ack'
regs["164"][7:0] = 'tmod'

# hw_dram_ctl171
regs["171"][24] = 'axi5_bdw_ovflow'
regs["171"][16] = 'axi4_bdw_ovflow'
regs["171"][15:0] = 'dll_rst_delay'

# hw_dram_ctl172
regs["172"][24] = 'resync_dll_per_aref_en'
regs["172"][16] = 'resync_dll'
regs["172"][8] = 'concurrentap_wr_only'

# hw_dram_ctl173
regs["173"][26:24] = 'axi4_w_priority'
regs["173"][18:16] = 'axi4_r_priority'
regs["173"][9:8] = 'axi5_fifo_type_reg'
regs["173"][1:0] = 'axi4_fifo_type_reg'

# hw_dram_ctl174
regs["174"][26:24] = 'r2r_samecs_dly'
regs["174"][18:16] = 'r2r_diffcs_dly'
regs["174"][10:8] = 'axi5_w_priority'
regs["174"][2:0] = 'axi5_r_priority'

# hw_dram_ctl175
regs["175"][26:24] = 'w2w_diffcs_dly'
regs["175"][18:16] = 'tbst_int_interval'
regs["175"][10:8] = 'r2w_samecs_dly'
regs["175"][2:0] = 'r2w_diffcs_dly'

# hw_dram_ctl176
regs["176"][27:24] = 'add_odt_clk_sametype_diffcs'
regs["176"][19:16] = 'add_odt_clk_difftype_samecs'
regs["176"][11:8] = 'add_odt_clk_difftype_diffcs'
regs["176"][2:0] = 'w2w_samecs_dly'

# hw_dram_ctl177
regs["177"][28:24] = 'tccd'
regs["177"][19:16] = 'trp_ab'
regs["177"][11:8] = 'cksrx'
regs["177"][3:0] = 'cksre'

# hw_dram_ctl178
regs["178"][30:24] = 'axi5_bdw'
regs["178"][22:16] = 'axi4_current_bdw'
regs["178"][14:8] = 'axi4_bdw'
regs["178"][4:0] = 'tckesr'

# hw_dram_ctl179
regs["179"][21:8] = 'tdfi_phyupd_type1'
regs["179"][6:0] = 'axi5_current_bdw'

# hw_dram_ctl180
regs["180"][29:16] = 'tdfi_phyupd_type3'
regs["180"][13:0] = 'tdfi_phyupd_type2'

# hw_dram_ctl181
regs["181"][22:20] = 'mr0_cs1_cas_latency'
regs["181"][19] = 'mr0_cs1_burst_type'
regs["181"][18:16] = 'mr0_cs1_burst_length'
regs["181"][6:4] = 'mr0_cs0_cas_latency'
regs["181"][3] = 'mr0_cs0_burst_type'
regs["181"][2:0] = 'mr0_cs0_burst_length'

# hw_dram_ctl182
regs["182"][22:20] = 'mr0_cs3_cas_latency'
regs["182"][19] = 'mr0_cs3_burst_type'
regs["182"][18:16] = 'mr0_cs3_burst_length'
regs["182"][6:4] = 'mr0_cs2_cas_latency'
regs["182"][3] = 'mr0_cs2_burst_type'
regs["182"][2:0] = 'mr0_cs2_burst_length'

# hw_dram_ctl183: for DDR1
regs["183"][23:21] = 'mr1_cs1_drive_strength'
regs["183"][20:19] = 'mr1_cs1_tcsr'
regs["183"][18:16] = 'mr1_cs1_partial_array_self_refresh_coverage'
regs["183"][7:5] = 'mr1_cs0_drive_strength'
regs["183"][4:3] = 'mr1_cs0_tcsr'
regs["183"][2:0] = 'mr1_cs0_partial_array_self_refresh_coverage'

# hw_dram_ctl184: for DDR1
regs["184"][23:21] = 'mr1_cs3_drive_strength'
regs["184"][20:19] = 'mr1_cs3_tcsr'
regs["184"][18:16] = 'mr1_cs3_partial_array_self_refresh_coverage'
regs["184"][7:5] = 'mr1_cs2_drive_strength'
regs["184"][4:3] = 'mr1_cs2_tcsr'
regs["184"][2:0] = 'mr1_cs2_partial_array_self_refresh_coverage'

# hw_dram_ctl185 ~ 188: not used for DDR1

# hw_dram_ctl189
regs["189"][31:16] = 'axi5_en_size_lt_width_instr'
regs["189"][15:0] = 'axi4_en_size_lt_width_instr'

"""
# cast default value in U-Boot
regs["17"].decode(0x00000100)
regs["26"].decode(0x00010101)
regs["27"].decode(0x01010101)
regs["28"].decode(0x000f0f01)
regs["29"].decode(0x0f02020a)
regs["31"].decode(0x00010101)
regs["32"].decode(0x00000100)
regs["33"].decode(0x00000100)
regs["35"].decode(0x00000002)
regs["36"].decode(0x01010000)
regs["37"].decode(0x07080403)
regs["38"].decode(0x06005003)
regs["39"].decode(0x0a0000c8)
regs["40"].decode(0x02009c40)
regs["41"].decode(0x0002030c)
regs["42"].decode(0x0036a609)
regs["43"].decode(0x031a0612)
regs["44"].decode(0x02030202)
regs["45"].decode(0x00c8001c)
regs["48"].decode(0x00012100)
regs["49"].decode(0xffff0303)
regs["50"].decode(0x00012100)
regs["51"].decode(0xffff0303)
regs["52"].decode(0x00012100)
regs["53"].decode(0xffff0303)
regs["54"].decode(0x00012100)
regs["55"].decode(0xffff0303)
regs["56"].decode(0x00000003)
regs["66"].decode(0x00000612)
regs["67"].decode(0x01000f02)
regs["68"].decode(0x06120612)
regs["69"].decode(0x00000200)
regs["70"].decode(0x00020007)
regs["71"].decode(0xf4004a27)
regs["72"].decode(0xf4004a27)
regs["73"].decode(0xf4004a27)
regs["74"].decode(0xf4004a27)
regs["75"].decode(0x07000300)
regs["76"].decode(0x07000300)
regs["77"].decode(0x07400300)
regs["78"].decode(0x07400300)
regs["79"].decode(0x00000005)
regs["82"].decode(0x01000000)
regs["83"].decode(0x01020408)
regs["84"].decode(0x08040201)
regs["85"].decode(0x00001133)
regs["87"].decode(0x00001f04)
regs["88"].decode(0x00001f04)
regs["89"].decode(0x00001f04)
regs["90"].decode(0x00001f04)
regs["91"].decode(0x00001f04)
regs["92"].decode(0x00001f04)
regs["93"].decode(0x00001f04)
regs["94"].decode(0x00001f04)
regs["162"].decode(0x00010000)
regs["163"].decode(0x00030404)
regs["164"].decode(0x00000003)
regs["171"].decode(0x01010000)
regs["172"].decode(0x01000000)
regs["173"].decode(0x03030000)
regs["174"].decode(0x00010303)
regs["175"].decode(0x01020202)
regs["177"].decode(0x02040303)
regs["178"].decode(0x21002103)
regs["179"].decode(0x00061200)
regs["180"].decode(0x06120612)
regs["181"].decode(0x04420442)
regs["182"].decode(0x04420442)
regs["183"].decode(0x00040004)
regs["184"].decode(0x00040004)
regs["189"].decode(0xffffffff)

regs["29"]["cs_map"] = 0b0001  # CS mask
regs["29"]["column_size"] = 2  # difference between 12 and actual width
regs["29"]["addr_pins"] = 1
regs["29"]["aprebit"] = 10  # auto precharge bit in address

regs["31"]["eight_bank_mode"] = 0
regs["31"]["dqs_n_en"] = 0  # DQS is single-ended

regs["32"]["reduc"] = 0  # TODO: is it effective?: half datapath
regs["32"]["reg_dimm_enable"] = 0

regs["33"]["concurrentap"] = 1  # concurrent operation of different banks is supported

# regs["34"] TODO: interrupting commands is effective?

regs["35"]["initaref"] = 2  # no. of auto-refresh command in initialization

regs["36"]["tras_lockout"] = 1
regs["36"]["fast_write"] = 0  # TODO: is it effective?

regs["37"]["caslat_lin_gate"] = 8  # TODO: adjust
regs["37"]["caslat_lin"] = 9  # TODO: adjust
regs["37"]["caslat"] = 3
regs["37"]["wrlat"] = 2

regs["38"]["tdal"] = 5  # = (t_wr/t_ck) + (t_rp/t_ck)
regs["38"]["tcpd"] = 80  # TODO: adjust
regs["38"]["tcke"] = 1

regs["39"]["tfaw"] = 10  # TODO: adjust, four active window delay
regs["39"]["tdll"] = 200  # TODO: maybe unnecessary?

regs["40"]["tmrd"] = 4
regs["40"]["tinit"] = 40000

regs["41"]["tpdex"] = 2
regs["41"]["trcd_int"] = 2
regs["41"]["trc"] = 12

regs["42"]["tras_max"] = 13990
regs["42"]["tras_min"] = 9

regs["43"]["trp"] = 4
regs["43"]["trfc"] = 15  # TODO: adjust
regs["43"]["tref"] = 3120  # TODO: adjust

regs["44"]["twtr"] = 4  # TODO: adjust
regs["44"]["twr_int"] = 3
regs["44"]["trtp"] = 3  # TODO: inferred
regs["44"]["trrd"] = 3

regs["45"]["txsr"] = 23  # TODO: adjust
regs["45"]["txsnr"] = 23  # TODO: adjust

#regs["67"]["dram_clk_enable"] = 0b0001

# regs["83"]  # TODO: adjust, not effective for LPDDR1?

regs["85"]["pad_type"] = 0  # DDR1

regs["163"]["dram_class"] = 0b0001  # DDR1 with Mobile

regs["175"]["tbst_int_interval"] = 2  # TODO: adjust

regs["177"]["tccd"] = 2  # TODO: adjust

regs["178"]["tckesr"] = 4
regs["181"]["mr0_cs0_cas_latency"] = 0b010
regs["181"]["mr0_cs0_burst_type"] = 0b0
regs["181"]["mr0_cs0_burst_length"] = 0b010

regs["183"]["mr1_cs0_drive_strength"] = 0b000
regs["183"]["mr1_cs0_partial_array_self_refresh_coverage"] = 0b000
"""

regs["0"].decode(0x00000000)
regs["16"].decode(0x00000000)
regs["21"].decode(0x00000000)
regs["22"].decode(0x00000000)
regs["23"].decode(0x00000000)
regs["24"].decode(0x00000000)
regs["25"].decode(0x00000000)
regs["26"].decode(0x00010101)
regs["27"].decode(0x01010101)
regs["28"].decode(0x000f0f01)
regs["29"].decode(0x0f02010a)
regs["31"].decode(0x00000101)
regs["32"].decode(0x00000100)
regs["33"].decode(0x00000100)
regs["34"].decode(0x01000000)
regs["35"].decode(0x00000002)
regs["36"].decode(0x01010000)
regs["37"].decode(0x08060301)
regs["38"].decode(0x06000001)
regs["39"].decode(0x0a000000)
regs["40"].decode(0x02009c40)
regs["41"].decode(0x0002030b)
regs["42"].decode(0x0036a608)
regs["43"].decode(0x03160305)
regs["44"].decode(0x03030002)
regs["45"].decode(0x001f001c)
regs["48"].decode(0x00012100)
regs["49"].decode(0xffff0303)
regs["50"].decode(0x00012100)
regs["51"].decode(0xffff0303)
regs["52"].decode(0x00012100)
regs["53"].decode(0xffff0303)
regs["54"].decode(0x00012100)
regs["55"].decode(0xffff0303)
regs["56"].decode(0x00000003)
regs["58"].decode(0x00000000)
regs["66"].decode(0x00000305)
regs["67"].decode(0x01000f02)
regs["69"].decode(0x00000200)
regs["70"].decode(0x00020007)
regs["71"].decode(0xf3004a27)
regs["72"].decode(0xf3004a27)
regs["75"].decode(0x07000310)
regs["76"].decode(0x07000310)
regs["79"].decode(0x00800004)
regs["80"].decode(0x00000000)
regs["81"].decode(0x00000000)
regs["82"].decode(0x01000000)
regs["83"].decode(0x01020408)
regs["84"].decode(0x08040201)
regs["85"].decode(0x000f1133)
regs["87"].decode(0x00001f08)
regs["88"].decode(0x00001f08)
regs["91"].decode(0x00001f01)
regs["92"].decode(0x00001f01)
regs["162"].decode(0x00000000)
regs["163"].decode(0x00010301)
regs["164"].decode(0x00000002)
regs["171"].decode(0x01010000)
regs["172"].decode(0x01000100)
regs["173"].decode(0x03030000)
regs["174"].decode(0x00020303)
regs["175"].decode(0x01010202)
regs["176"].decode(0x00000000)
regs["177"].decode(0x01030101)
regs["178"].decode(0x21002101)
regs["179"].decode(0x00030500)
regs["180"].decode(0x03050305)
regs["181"].decode(0x00320032)
regs["182"].decode(0x00320032)
regs["183"].decode(0x00000000)
regs["184"].decode(0x00000000)
regs["185"].decode(0x00000000)
regs["186"].decode(0x00000000)
regs["187"].decode(0x00000000)
regs["188"].decode(0x00000000)
regs["189"].decode(0xffffffff)

regsenc = []
for i in range(190):
    si = str(i)
    if si in regs:
        regsenc.append(f'{regs[si].encode():#010x}')
    else:
        regsenc.append('0x00000000')

with open('out.c', 'w') as f:
    for i, j in zip(range(0, 190, 4), range(4, 194, 4)):
        if j >= 190:
            f.write(', '.join(regsenc[i:j]) + '\n')
        else:
            f.write(', '.join(regsenc[i:j]) + ',\n')
