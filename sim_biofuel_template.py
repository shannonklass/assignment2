#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""	
%
% Purpose:  The aim of this file is to simulate the biofuel model 
% 
% Inputs:
%   data_set_to_use     (integer) Set id for system constants needed for simulation
%   array_time              (array) An array of uniformly distributed time
%                           instances 
%   init_bacteria_amount    The initial amount of bacteria
%   alpha_b                 Value of the parameter alpha_b which is the
%                           production rate of biofuel 
%   alpha_p                 Value of the parameter alpha_p whihc is the
%                           production rate of efflux pumps
% 
% Outputs:
%   array_bateriaAmount     (array) Amount of Bacteria
%   array_sensor            (array) Sensor output
%   array_pump              (array) Number of efflux pumps
%   array_biofuelInt        (array) Amount of biofuel inside bacteria
%   array_biofuelExt        (array) Amount of biofuel outsie of bacteria 

"""

import biofuel_system_parameter_sets as bsps


def sim_biofuel(data_set_to_use, time_array, init_bacteria_amount, alpha_b, alpha_p) : 

    # BEGIN - DO NOT REMOVE 
    # Note: Please do not remove this
    sys_para = bsps.biofuel_system_parameter_sets(data_set_to_use)
    ALPHA_N = sys_para['ALPHA_N' ]  # Growth rate (1/h)
    ALPHA_R = sys_para['ALPHA_R' ]  # Basal repressor production rate (1/h)
    BETA_R =  sys_para['BETA_R']    # Repressor degradation rate (1/h)
    BETA_P =  sys_para['BETA_P']    # Pump degradation rate (1/h) 
    DELTA_N = sys_para['DELTA_N']   # Biofuel toxicity coefficient (1/(Mh))
    DELTA_B = sys_para['DELTA_B']   # Biofuel export rate per pump (1/(Mh))
    GAMMA_P = sys_para['GAMMA_P']   # Pump toxicity threshold 
    GAMMA_I = sys_para['GAMMA_I']   # Inducer saturation threshold (M)
    GAMMA_R = sys_para['GAMMA_R']   # Repressor saturation threshold 
    K_R  =    sys_para['K_R']       # Repressor activation constant (h)
    K_P  =    sys_para['K_P']       # Pump activation constant (1/h)
    K_B  =    sys_para['K_B']       # Repressor deactivation constant (1/M)
    V    =    sys_para['V']         # Ratio of intra to extracellular volume 
    I    =    sys_para['I']         # Amount of inducer             
    # The above lines set the following constants: 
    # ALPHA_N ALPHA_R BETA_R  BETA_P  DELTA_N DELTA_B GAMMA_P GAMMA_I 
    # GAMMA_R K_R K_P K_B V I       
    # END - DO NOT REMOVE    

    
    # determine time increment
    dt = time_array[2]-time_array[1]    
    
    # You should put your work below this line 

    # Simulation output variables



    # Assign initial values
    
    
    
    # and more ... 
    
    
