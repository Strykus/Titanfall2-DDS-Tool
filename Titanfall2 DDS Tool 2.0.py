# -*- coding: utf-8 -*-
"""
Titanfall 2 DDS skin apply tool
"""
import os
import sys

"""
Constants
"""

# OFFSETS

rspn101_2048_col              = int('0000000219121000',16)
rspn101_2048_nml              = int('0000000219471000',16)
rspn101_2048_gls              = int('0000000219911000',16)
rspn101_2048_spc              = int('0000000219BB1000',16)
rspn101_2048_ilm              = int('0000000219E51000',16)
rspn101_2048_ao               = int('000000021A0F1000',16)
rspn101_2048_cav              = int('000000021A391000',16)
rspn101_1024_col              = int('00000002190A1000',16)
rspn101_1024_nml              = int('0000000219371000',16)
rspn101_1024_gls              = int('0000000219891000',16)
rspn101_1024_spc              = int('0000000219B31000',16)
rspn101_1024_ilm              = int('0000000219DD1000',16)
rspn101_1024_ao               = int('000000021A071000',16)
rspn101_1024_cav              = int('000000021A311000',16)
rspn101_512_col               = int('0000000219081000',16)
rspn101_512_nml               = int('0000000219331000',16)
rspn101_512_gls               = int('0000000219871000',16)
rspn101_512_spc               = int('0000000219B11000',16)
rspn101_512_ilm               = int('0000000219DB1000',16)
rspn101_512_ao                = int('000000021A051000',16)
rspn101_512_cav               = int('000000021A2F1000',16)

rspn101_offsets = [rspn101_2048_col,
                   rspn101_2048_nml,
                   rspn101_2048_gls,
                   rspn101_2048_spc,
                   rspn101_2048_ilm,
                   rspn101_2048_ao,
                   rspn101_2048_cav,
                   rspn101_1024_col,
                   rspn101_1024_nml,
                   rspn101_1024_gls,
                   rspn101_1024_spc,
                   rspn101_1024_ilm,
                   rspn101_1024_ao,
                   rspn101_1024_cav,
                   rspn101_512_col,
                   rspn101_512_nml,
                   rspn101_512_gls,
                   rspn101_512_spc,
                   rspn101_512_spc,
                   rspn101_512_ao,
                   rspn101_512_cav]

"""
Have not found offsets for r101_sfp

r101_sfp_2048_col             = int('',16)
r101_sfp_2048_nml             = int('',16)
r101_sfp_2048_gls             = int('',16)
r101_sfp_2048_spc             = int('',16)
r101_sfp_2048_ao              = int('',16)
r101_sfp_1024_col             = int('',16)
r101_sfp_1024_nml             = int('',16)
r101_sfp_1024_gls             = int('',16)
r101_sfp_1024_spc             = int('',16)
r101_sfp_1024_ao              = int('',16)
r101_sfp_512_col              = int('',16)
r101_sfp_512_nml              = int('',16)
r101_sfp_512_gls              = int('',16)
r101_sfp_512_spc              = int('',16)
r101_sfp_512_ao               = int('',16)

rspn101_sfp_offsets = [rspn101_sfp_2048_col,
                       rspn101_sfp_2048_nml,
                       rspn101_sfp_2048_gls,
                       rspn101_sfp_2048_spc,
                       rspn101_sfp_2048_ao,
                       rspn101_sfp_1024_col,
                       rspn101_sfp_1024_nml,
                       rspn101_sfp_1024_gls,
                       rspn101_sfp_1024_spc,
                       rspn101_sfp1024_ao,
                       rspn101_sfp_512_col,
                       rspn101_sfp_512_nml,
                       rspn101_sfp_512_gls,
                       rspn101_sfp_512_spc,
                       rspn101_sfp_512_ao]
"""
hcog2_1024_col        = int('000000022F2E1000',16)
hcog2_1024_nml        = int('000000022F3B1000',16)
hcog2_1024_gls        = int('000000022F4D1000',16)
hcog2_1024_spc        = int('000000022F571000',16)
hcog2_1024_ilm        = int('000000022F611000',16)
hcog2_1024_ao         = int('000000022F6B1000',16)
hcog2_1024_cav        = int('000000022F751000',16)
hcog2_512_col         = int('000000022F2C1000',16)
hcog2_512_nml         = int('000000022F371000',16)
hcog2_512_gls         = int('000000022F4B1000',16)
hcog2_512_spc         = int('000000022F551000',16)
hcog2_512_ilm         = int('000000022F5F1000',16)
hcog2_512_ao          = int('000000022F691000',16)
hcog2_512_cav         = int('000000022F731000',16)

hcog2_offsets = [hcog2_1024_col,
                         hcog2_1024_nml,
                         hcog2_1024_gls,
                         hcog2_1024_spc,
                         hcog2_1024_ilm,
                         hcog2_1024_ao,
                         hcog2_1024_cav,
                         hcog2_512_col,
                         hcog2_512_nml,
                         hcog2_512_gls,
                         hcog2_512_spc,
                         hcog2_512_ilm,
                         hcog2_512_ao,
                         hcog2_512_cav]

threat_scope_sniper_1024_col        = int('000000022FC11000',16)
threat_scope_sniper_1024_nml        = int('000000022FCE1000',16)
threat_scope_sniper_1024_gls        = int('000000022FE01000',16)
threat_scope_sniper_1024_spc        = int('000000022FEA1000',16)
threat_scope_sniper_1024_ao         = int('000000022FF41000',16)
threat_scope_sniper_1024_cav        = int('000000022FFE1000',16)
threat_scope_sniper_512_col         = int('000000022FBF1000',16)
threat_scope_sniper_512_nml         = int('000000022FCA1000',16)
threat_scope_sniper_512_gls         = int('000000022FDE1000',16)
threat_scope_sniper_512_spc         = int('000000022FE81000',16)
threat_scope_sniper_512_ao          = int('000000022FF21000',16)
threat_scope_sniper_512_cav         = int('000000022FFC1000',16)

threat_scope_sniper_offsets = [threat_scope_sniper_1024_col,
                         threat_scope_sniper_1024_nml,
                         threat_scope_sniper_1024_gls,
                         threat_scope_sniper_1024_spc,
                         threat_scope_sniper_1024_ao,
                         threat_scope_sniper_1024_cav,
                         threat_scope_sniper_512_col,
                         threat_scope_sniper_512_nml,
                         threat_scope_sniper_512_gls,
                         threat_scope_sniper_512_spc,
                         threat_scope_sniper_512_ao,
                         threat_scope_sniper_512_cav]

threat_w_scope_1024_col        = int('000000022E961000',16)
threat_w_scope_1024_nml        = int('000000022EA31000',16)
threat_w_scope_1024_gls        = int('000000022EB51000',16)
threat_w_scope_1024_spc        = int('000000022EBF1000',16)
threat_w_scope_1024_ilm        = int('000000022EC91000',16)
threat_w_scope_1024_ao         = int('000000022ED31000',16)
threat_w_scope_1024_cav        = int('000000022EDD1000',16)
threat_w_scope_512_col         = int('000000022E941000',16)
threat_w_scope_512_nml         = int('000000022E9F1000',16)
threat_w_scope_512_gls         = int('000000022EB31000',16)
threat_w_scope_512_spc         = int('000000022EBD1000',16)
threat_w_scope_512_ilm         = int('000000022EC71000',16)
threat_w_scope_512_ao          = int('000000022ED11000',16)
threat_w_scope_512_cav         = int('000000022EDB1000',16)

threat_w_scope_offsets = [threat_w_scope_1024_col,
                         threat_w_scope_1024_nml,
                         threat_w_scope_1024_gls,
                         threat_w_scope_1024_spc,
                         threat_w_scope_1024_ilm,
                         threat_w_scope_1024_ao,
                         threat_w_scope_1024_cav,
                         threat_w_scope_512_col,
                         threat_w_scope_512_nml,
                         threat_w_scope_512_gls,
                         threat_w_scope_512_spc,
                         threat_w_scope_512_ilm,
                         threat_w_scope_512_ao,
                         threat_w_scope_512_cav]
						 
aog_sight_1024_col        = int('000000020BA41000',16)
aog_sight_1024_nml        = int('000000020BB11000',16)
aog_sight_1024_gls        = int('000000020BC31000',16)
aog_sight_1024_spc        = int('000000020BCD1000',16)
aog_sight_1024_ao         = int('000000020BD71000',16)
aog_sight_1024_cav        = int('000000020BE11000',16)
aog_sight_512_col         = int('000000020BA21000',16)
aog_sight_512_nml         = int('000000020BAD1000',16)
aog_sight_512_gls         = int('000000020BC11000',16)
aog_sight_512_spc         = int('000000020BCB1000',16)
aog_sight_512_ao          = int('000000020BD51000',16)
aog_sight_512_cav         = int('000000020BDF1000',16)

aog_sight_offsets = [aog_sight_1024_col,
                         aog_sight_1024_nml,
                         aog_sight_1024_gls,
                         aog_sight_1024_spc,
                         aog_sight_1024_ao,
                         aog_sight_1024_cav,
                         aog_sight_512_col,
                         aog_sight_512_nml,
                         aog_sight_512_gls,
                         aog_sight_512_spc,
                         aog_sight_512_ao,
                         aog_sight_512_cav] 

holo_reflex_sight_magnifier_1024_col        = int('000000022F7F1000',16)
holo_reflex_sight_magnifier_1024_nml        = int('000000022F8C1000',16)
holo_reflex_sight_magnifier_1024_gls        = int('000000022F9E1000',16)
holo_reflex_sight_magnifier_1024_spc        = int('000000022FA81000',16)
holo_reflex_sight_magnifier_512_col         = int('000000022F7D1000',16)
holo_reflex_sight_magnifier_512_nml         = int('000000022F881000',16)
holo_reflex_sight_magnifier_512_gls         = int('000000022F9C1000',16)
holo_reflex_sight_magnifier_512_spc         = int('000000022FA61000',16)

holo_reflex_sight_magnifier_offsets = [holo_reflex_sight_magnifier_1024_col,
                         holo_reflex_sight_magnifier_1024_nml,
                         holo_reflex_sight_magnifier_1024_gls,
                         holo_reflex_sight_magnifier_1024_spc,
                         holo_reflex_sight_magnifier_512_col,
                         holo_reflex_sight_magnifier_512_nml,
                         holo_reflex_sight_magnifier_512_gls,
                         holo_reflex_sight_magnifier_512_spc]
						 
acgs_sight_1024_col        = int('000000020B5C1000',16)
acgs_sight_1024_nml        = int('000000020B691000',16)
acgs_sight_1024_gls        = int('000000020B7B1000',16)
acgs_sight_1024_spc        = int('000000020B851000',16)
acgs_sight_1024_ao         = int('000000020B8F1000',16)
acgs_sight_1024_cav        = int('000000020B991000',16)
acgs_sight_512_col         = int('000000020B5A1000',16)
acgs_sight_512_nml         = int('000000020B651000',16)
acgs_sight_512_gls         = int('000000020B791000',16)
acgs_sight_512_spc         = int('000000020B831000',16)
acgs_sight_512_ao          = int('000000020B8D1000',16)
acgs_sight_512_cav         = int('000000020B971000',16)

acgs_sight_offsets = [acgs_sight_1024_col,
                         acgs_sight_1024_nml,
                         acgs_sight_1024_gls,
                         acgs_sight_1024_spc,
                         acgs_sight_1024_ao,
                         acgs_sight_1024_cav,
                         acgs_sight_512_col,
                         acgs_sight_512_nml,
                         acgs_sight_512_gls,
                         acgs_sight_512_spc,
                         acgs_sight_512_ao,
                         acgs_sight_512_cav]
						 
dcom_1024_col        = int('000000022EE71000',16)
dcom_1024_nml        = int('000000022EF41000',16)
dcom_1024_gls        = int('000000022F061000',16)
dcom_1024_spc        = int('000000022F101000',16)
dcom_1024_ao         = int('000000022F1A1000',16)
dcom_1024_cav        = int('000000022F241000',16)
dcom_512_col         = int('000000022EE51000',16)
dcom_512_nml         = int('000000022EF01000',16)
dcom_512_gls         = int('000000022F041000',16)
dcom_512_spc         = int('000000022F0E1000',16)
dcom_512_ao          = int('000000022F181000',16)
dcom_512_cav         = int('000000022F221000',16)

dcom_offsets = [dcom_1024_col,
                         dcom_1024_nml,
                         dcom_1024_gls,
                         dcom_1024_spc,
                         dcom_1024_ao,
                         dcom_1024_cav,
                         dcom_512_col,
                         dcom_512_nml,
                         dcom_512_gls,
                         dcom_512_spc,
                         dcom_512_ao,
                         dcom_512_cav]
						 
talon_optic_1024_col        = int('0000000233AA1000',16)
talon_optic_1024_nml        = int('0000000233B71000',16)
talon_optic_1024_gls        = int('0000000233C91000',16)
talon_optic_1024_spc        = int('0000000233D31000',16)
talon_optic_1024_ao         = int('0000000233DD1000',16)
talon_optic_1024_cav        = int('0000000233E71000',16)
talon_optic_512_col         = int('0000000233A81000',16)
talon_optic_512_nml         = int('0000000233B31000',16)
talon_optic_512_gls         = int('0000000233C71000',16)
talon_optic_512_spc         = int('0000000233D11000',16)
talon_optic_512_ao          = int('0000000233DB1000',16)
talon_optic_512_cav         = int('0000000233E51000',16)

talon_optic_offsets = [talon_optic_1024_col,
                         talon_optic_1024_nml,
                         talon_optic_1024_gls,
                         talon_optic_1024_spc,
                         talon_optic_1024_ao,
                         talon_optic_1024_cav,
                         talon_optic_512_col,
                         talon_optic_512_nml,
                         talon_optic_512_gls,
                         talon_optic_512_spc,
                         talon_optic_512_ao,
                         talon_optic_512_cav] 
						 
suppressors_1024_col        = int('000000020C931000',16)
suppressors_1024_nml        = int('000000020CA01000',16)
suppressors_1024_gls        = int('000000020CB21000',16)
suppressors_1024_spc        = int('000000020CBC1000',16)
suppressors_1024_ao         = int('000000020CC61000',16)
suppressors_512_col         = int('000000020C911000',16)
suppressors_512_nml         = int('000000020C9C1000',16)
suppressors_512_gls         = int('000000020CB01000',16)
suppressors_512_spc         = int('000000020CBA1000',16)
suppressors_512_ao          = int('000000020CC41000',16)

suppressors_offsets = [suppressors_1024_col,
                         suppressors_1024_nml,
                         suppressors_1024_gls,
                         suppressors_1024_spc,
                         suppressors_1024_ao,
                         suppressors_512_col,
                         suppressors_512_nml,
                         suppressors_512_gls,
                         suppressors_512_spc,
                         suppressors_512_ao]
						 
pro_screen_512_col         = int('0000000230061000',16)
pro_screen_512_nml         = int('0000000230091000',16)
pro_screen_512_gls         = int('00000002300D1000',16)
pro_screen_512_spc         = int('00000002300F1000',16)
pro_screen_512_ilm         = int('0000000230111000',16)
pro_screen_512_ao          = int('0000000230131000',16)
pro_screen_512_cav         = int('0000000230151000',16)

pro_screen_offsets = [pro_screen_512_col,
                         pro_screen_512_nml,
                         pro_screen_512_gls,
                         pro_screen_512_spc,
                         pro_screen_512_ilm,
                         pro_screen_512_ao,
                         pro_screen_512_cav]

m1a1_hemlok_2048_col          = int('0000000242B71000',16)
m1a1_hemlok_2048_nml          = int('0000000242EC1000',16)
m1a1_hemlok_2048_gls          = int('0000000243361000',16)
m1a1_hemlok_2048_spc          = int('0000000243601000',16)
m1a1_hemlok_2048_ilm          = int('00000002438A1000',16)
m1a1_hemlok_2048_ao           = int('0000000243B41000',16)
m1a1_hemlok_2048_cav          = int('0000000243DE1000',16)
m1a1_hemlok_1024_col          = int('0000000242AF1000',16)
m1a1_hemlok_1024_nml          = int('0000000242DC1000',16)
m1a1_hemlok_1024_gls          = int('00000002432E1000',16)
m1a1_hemlok_1024_spc          = int('0000000243581000',16)
m1a1_hemlok_1024_ilm          = int('0000000243821000',16)
m1a1_hemlok_1024_ao           = int('0000000243AC1000',16)
m1a1_hemlok_1024_cav          = int('0000000243D61000',16)
m1a1_hemlok_512_col           = int('0000000242AD1000',16)
m1a1_hemlok_512_nml           = int('0000000242D81000',16)
m1a1_hemlok_512_gls           = int('00000002432C1000',16)
m1a1_hemlok_512_spc           = int('0000000243561000',16)
m1a1_hemlok_512_ilm           = int('0000000243801000',16)
m1a1_hemlok_512_ao            = int('0000000243AA1000',16)
m1a1_hemlok_512_cav           = int('0000000243D41000',16)

m1a1_hemlok_offsets = [m1a1_hemlok_2048_col,
                       m1a1_hemlok_2048_nml,
                       m1a1_hemlok_2048_gls,
                       m1a1_hemlok_2048_spc,
                       m1a1_hemlok_2048_ilm,
                       m1a1_hemlok_2048_ao,
                       m1a1_hemlok_2048_cav,
                       m1a1_hemlok_1024_col,
                       m1a1_hemlok_1024_nml,
                       m1a1_hemlok_1024_gls,
                       m1a1_hemlok_1024_spc,
                       m1a1_hemlok_1024_ilm,
                       m1a1_hemlok_1024_ao,
                       m1a1_hemlok_1024_cav,
                       m1a1_hemlok_512_col,
                       m1a1_hemlok_512_nml,
                       m1a1_hemlok_512_gls,
                       m1a1_hemlok_512_spc,
                       m1a1_hemlok_512_ilm,
                       m1a1_hemlok_512_ao,
                       m1a1_hemlok_512_cav]

vinson_2048_col               = int('0000000223B11000',16)
vinson_2048_nml               = int('0000000223E61000',16)
vinson_2048_gls               = int('0000000224301000',16)
vinson_2048_spc               = int('00000002245A1000',16)
vinson_2048_ilm               = int('0000000224841000',16)
vinson_2048_ao                = int('0000000224AE1000',16)
vinson_2048_cav               = int('0000000224D81000',16)
vinson_1024_col               = int('0000000223A91000',16)
vinson_1024_nml               = int('0000000223D61000',16)
vinson_1024_gls               = int('0000000224281000',16)
vinson_1024_spc               = int('0000000224521000',16)
vinson_1024_ilm               = int('00000002247C1000',16)
vinson_1024_ao                = int('0000000224A61000',16)
vinson_1024_cav               = int('0000000224D01000',16)
vinson_512_col                = int('0000000223A71000',16)
vinson_512_nml                = int('0000000223D21000',16)
vinson_512_gls                = int('0000000224261000',16)
vinson_512_spc                = int('0000000224501000',16)
vinson_512_ilm                = int('00000002247A1000',16)
vinson_512_ao                 = int('0000000224A41000',16)
vinson_512_cav                = int('0000000224CE1000',16)

vinson_offsets = [vinson_2048_col,
                  vinson_2048_nml,
                  vinson_2048_gls,
                  vinson_2048_spc,
                  vinson_2048_ilm,
                  vinson_2048_ao,
                  vinson_2048_cav,
                  vinson_1024_col,
                  vinson_1024_nml,
                  vinson_1024_gls,
                  vinson_1024_spc,
                  vinson_1024_ilm,
                  vinson_1024_ao,
                  vinson_1024_cav,
                  vinson_512_col,
                  vinson_512_nml,
                  vinson_512_gls,
                  vinson_512_spc,
                  vinson_512_ilm,
                  vinson_512_ao,
                  vinson_512_cav]

g2_2048_col                   = int('0000000240E81000',16)
g2_2048_nml                   = int('00000002411D1000',16)
g2_2048_gls                   = int('0000000241671000',16)
g2_2048_spc                   = int('0000000241911000',16)
g2_2048_ilm                   = int('0000000241BB1000',16)
g2_2048_ao                    = int('0000000241E51000',16)
g2_2048_cav                   = int('00000002420F1000',16)
g2_1024_col                   = int('0000000240E01000',16)
g2_1024_nml                   = int('00000002410D1000',16)
g2_1024_gls                   = int('00000002415F1000',16)
g2_1024_spc                   = int('0000000241891000',16)
g2_1024_ilm                   = int('0000000241B31000',16)
g2_1024_ao                    = int('0000000241DD1000',16)
g2_1024_cav                   = int('0000000242071000',16)
g2_512_col                    = int('0000000240DE1000',16)
g2_512_nml                    = int('0000000241091000',16)
g2_512_gls                    = int('00000002415D1000',16)
g2_512_spc                    = int('0000000241871000',16)
g2_512_ilm                    = int('0000000241B11000',16)
g2_512_ao                     = int('0000000241DB1000',16)
g2_512_cav                    = int('0000000242051000',16)

g2_offsets = [g2_2048_col,
              g2_2048_nml,
              g2_2048_gls,
              g2_2048_spc,
              g2_2048_ilm,
              g2_2048_ao,
              g2_2048_cav,
              g2_1024_col,
              g2_1024_nml,
              g2_1024_gls,
              g2_1024_spc,
              g2_1024_ilm,
              g2_1024_ao,
              g2_1024_cav,
              g2_512_col,
              g2_512_nml,
              g2_512_gls,
              g2_512_spc,
              g2_512_ilm,
              g2_512_ao,
              g2_512_cav]

alternator_smg_2048_col       = int('0000000226671000',16)
alternator_smg_2048_nml       = int('00000002269C1000',16)
alternator_smg_2048_gls       = int('0000000226E61000',16)
alternator_smg_2048_spc       = int('0000000227101000',16)
alternator_smg_2048_ao        = int('00000002273A1000',16)
alternator_smg_2048_cav       = int('0000000227641000',16)
alternator_smg_1024_col       = int('00000002265F1000',16)
alternator_smg_1024_nml       = int('00000002268C1000',16)
alternator_smg_1024_gls       = int('0000000226DE1000',16)
alternator_smg_1024_spc       = int('0000000227081000',16)
alternator_smg_1024_ao        = int('0000000227321000',16)
alternator_smg_1024_cav       = int('00000002275C1000',16)
alternator_smg_512_col        = int('00000002265D1000',16)
alternator_smg_512_nml        = int('0000000226881000',16)
alternator_smg_512_gls        = int('0000000226DC1000',16)
alternator_smg_512_spc        = int('0000000227061000',16)
alternator_smg_512_ao         = int('0000000227301000',16)
alternator_smg_512_cav        = int('00000002275A1000',16)

alternator_smg_offsets = [alternator_smg_2048_col,
                          alternator_smg_2048_nml,
                          alternator_smg_2048_gls,
                          alternator_smg_2048_spc,
                          alternator_smg_2048_ao,
                          alternator_smg_2048_cav,
                          alternator_smg_1024_col,
                          alternator_smg_1024_nml,
                          alternator_smg_1024_gls,
                          alternator_smg_1024_spc,
                          alternator_smg_1024_ao,
                          alternator_smg_1024_cav,
                          alternator_smg_512_col,
                          alternator_smg_512_nml,
                          alternator_smg_512_gls,
                          alternator_smg_512_spc,
                          alternator_smg_512_ao,
                          alternator_smg_512_cav]

car101_2048_col               = int('0000000236EE1000',16)
car101_2048_nml               = int('0000000237231000',16)
car101_2048_gls               = int('00000002376D1000',16)
car101_2048_spc               = int('0000000237971000',16)
car101_2048_ilm               = int('0000000237C11000',16)
car101_2048_ao                = int('0000000237EB1000',16)
car101_2048_cav               = int('0000000238151000',16)
car101_1024_col               = int('0000000236E61000',16)
car101_1024_nml               = int('0000000237131000',16)
car101_1024_gls               = int('0000000237651000',16)
car101_1024_spc               = int('00000002378F1000',16)
car101_1024_ilm               = int('0000000237B91000',16)
car101_1024_ao                = int('0000000237E31000',16)
car101_1024_cav               = int('00000002380D1000',16)
car101_512_col                = int('0000000236E41000',16)
car101_512_nml                = int('00000002370F1000',16)
car101_512_gls                = int('0000000237631000',16)
car101_512_spc                = int('00000002378D1000',16)
car101_512_ilm                = int('0000000237B71000',16)
car101_512_ao                 = int('0000000237E11000',16)
car101_512_cav                = int('00000002380B1000',16)

car101_offsets = [car101_2048_col,
                  car101_2048_nml,
                  car101_2048_gls,
                  car101_2048_spc,
                  car101_2048_ilm,
                  car101_2048_ao,
                  car101_2048_cav,
                  car101_1024_col,
                  car101_1024_nml,
                  car101_1024_gls,
                  car101_1024_spc,
                  car101_1024_ilm,
                  car101_1024_ao,
                  car101_1024_cav,
                  car101_512_col,
                  car101_512_nml,
                  car101_512_gls,
                  car101_512_spc,
                  car101_512_ilm,
                  car101_512_ao,
                  car101_512_cav]

r97_2048_col                  = int('000000024E091000',16)
r97_2048_nml                  = int('000000024E3E1000',16)
r97_2048_gls                  = int('000000024E881000',16)
r97_2048_spc                  = int('000000024EB21000',16)
r97_2048_ilm                  = int('000000024EDC1000',16)
r97_2048_ao                   = int('000000024F061000',16)
r97_2048_cav                  = int('000000024F301000',16)
r97_1024_col                  = int('000000024E011000',16)
r97_1024_nml                  = int('000000024E2E1000',16)
r97_1024_gls                  = int('000000024E801000',16)
r97_1024_spc                  = int('000000024EAA1000',16)
r97_1024_ilm                  = int('000000024ED41000',16)
r97_1024_ao                   = int('000000024EFE1000',16)
r97_1024_cav                  = int('000000024F281000',16)
r97_512_col                   = int('000000024DFF1000',16)
r97_512_nml                   = int('000000024E2A1000',16)
r97_512_gls                   = int('000000024E7E1000',16)
r97_512_spc                   = int('000000024EA81000',16)
r97_512_ilm                   = int('000000024ED21000',16)
r97_512_ao                    = int('000000024EFC1000',16)
r97_512_cav                   = int('000000024F261000',16)

r97_offsets = [r97_2048_col,
               r97_2048_nml,
               r97_2048_gls,
               r97_2048_spc,
               r97_2048_ilm,
               r97_2048_ao,
               r97_2048_cav,
               r97_1024_col,
               r97_1024_nml,
               r97_1024_gls,
               r97_1024_spc,
               r97_1024_ilm,
               r97_1024_ao,
               r97_1024_cav,
               r97_512_col,
               r97_512_nml,
               r97_512_gls,
               r97_512_spc,
               r97_512_ilm,
               r97_512_ao,
               r97_512_cav]

hemlok_smg_2048_col           = int('000000020FFA1000',16)
hemlok_smg_2048_nml           = int('00000002104F1000',16)
hemlok_smg_2048_gls           = int('0000000210991000',16)
hemlok_smg_2048_spc           = int('0000000210CE1000',16)
hemlok_smg_2048_ilm           = int('0000000211181000',16)
hemlok_smg_2048_ao            = int('0000000211421000',16)
hemlok_smg_2048_cav           = int('00000002116C1000',16)
hemlok_smg_1024_col           = int('000000020FEA1000',16)
hemlok_smg_1024_nml           = int('00000002103F1000',16)
hemlok_smg_1024_gls           = int('0000000210911000',16)
hemlok_smg_1024_spc           = int('0000000210BE1000',16)
hemlok_smg_1024_ilm           = int('0000000211101000',16)
hemlok_smg_1024_ao            = int('00000002113A1000',16)
hemlok_smg_1024_cav           = int('0000000211641000',16)
hemlok_smg_512_col            = int('000000020FE61000',16)
hemlok_smg_512_nml            = int('00000002103B1000',16)
hemlok_smg_512_gls            = int('00000002108F1000',16)
hemlok_smg_512_spc            = int('0000000210BA1000',16)
hemlok_smg_512_ilm            = int('00000002110E1000',16)
hemlok_smg_512_ao             = int('0000000211381000',16)
hemlok_smg_512_cav            = int('0000000211621000',16)
hemlok_smg_256_col            = int('000000020FE51000',16)
hemlok_smg_256_nml            = int('00000002103A1000',16)
hemlok_smg_256_spc            = int('0000000210B91000',16)

hemlok_smg_offsets = [hemlok_smg_2048_col,
                      hemlok_smg_2048_nml,
                      hemlok_smg_2048_gls,
                      hemlok_smg_2048_spc,
                      hemlok_smg_2048_ilm,
                      hemlok_smg_2048_ao,
                      hemlok_smg_2048_cav,
                      hemlok_smg_1024_col,
                      hemlok_smg_1024_nml,
                      hemlok_smg_1024_gls,
                      hemlok_smg_1024_spc,
                      hemlok_smg_1024_ilm,
                      hemlok_smg_1024_ao,
                      hemlok_smg_1024_cav,
                      hemlok_smg_512_col,
                      hemlok_smg_512_nml,
                      hemlok_smg_512_gls,
                      hemlok_smg_512_spc,
                      hemlok_smg_512_ilm,
                      hemlok_smg_512_ao,
                      hemlok_smg_512_cav]

hemlok_br_2048_col           = int('000000020E741000',16)
hemlok_br_2048_nml           = int('000000020EA91000',16)
hemlok_br_2048_gls           = int('000000020EF31000',16)
hemlok_br_2048_spc           = int('000000020F1D1000',16)
hemlok_br_2048_ilm           = int('000000020F471000',16)
hemlok_br_2048_ao            = int('000000020F711000',16)
hemlok_br_1024_col           = int('000000020E6C1000',16)
hemlok_br_1024_nml           = int('000000020E991000',16)
hemlok_br_1024_gls           = int('000000020EEB1000',16)
hemlok_br_1024_spc           = int('000000020F151000',16)
hemlok_br_1024_ilm           = int('000000020F3F1000',16)
hemlok_br_1024_ao            = int('000000020F691000',16)
hemlok_br_512_col            = int('000000020E6A1000',16)
hemlok_br_512_nml            = int('000000020E951000',16)
hemlok_br_512_gls            = int('000000020EE91000',16)
hemlok_br_512_spc            = int('000000020F131000',16)
hemlok_br_512_ilm            = int('000000020F3D1000',16)
hemlok_br_512_ao             = int('000000020F671000',16)

hemlok_br_offsets = [hemlok_br_2048_col,
                     hemlok_br_2048_nml,
                     hemlok_br_2048_gls,
                     hemlok_br_2048_spc,
                     hemlok_br_2048_ilm,
                     hemlok_br_2048_ao,
                     hemlok_br_1024_col,
                     hemlok_br_1024_nml,
                     hemlok_br_1024_gls,
                     hemlok_br_1024_spc,
                     hemlok_br_1024_ilm,
                     hemlok_br_1024_ao,
                     hemlok_br_512_col,
                     hemlok_br_512_nml,
                     hemlok_br_512_gls,
                     hemlok_br_512_spc,
                     hemlok_br_512_ilm,
                     hemlok_br_512_ao]

lstar_2048_col                = int('0000000211EA1000',16)
lstar_2048_nml                = int('00000002121F1000',16)
lstar_2048_gls                = int('0000000212691000',16)
lstar_2048_spc                = int('0000000212931000',16)
lstar_2048_ilm                = int('0000000212BD1000',16)
lstar_2048_ao                 = int('0000000212E71000',16)
lstar_2048_cav                = int('0000000213111000',16)
lstar_1024_col                = int('0000000211E21000',16)
lstar_1024_nml                = int('00000002120F1000',16)
lstar_1024_gls                = int('0000000212611000',16)
lstar_1024_spc                = int('00000002128B1000',16)
lstar_1024_ilm                = int('0000000212B51000',16)
lstar_1024_ao                 = int('0000000212DF1000',16)
lstar_1024_cav                = int('0000000213091000',16)
lstar_512_col                 = int('0000000211E01000',16)
lstar_512_nml                 = int('00000002120B1000',16)
lstar_512_gls                 = int('00000002125F1000',16)
lstar_512_spc                 = int('0000000212891000',16)
lstar_512_ilm                 = int('0000000212B31000',16)
lstar_512_ao                  = int('0000000212DD1000',16)
lstar_512_cav                 = int('0000000213071000',16)

lstar_offsets = [lstar_2048_col,
                 lstar_2048_nml,
                 lstar_2048_gls,
                 lstar_2048_spc,
                 lstar_2048_ilm,
                 lstar_2048_ao,
                 lstar_2048_cav,
                 lstar_1024_col,
                 lstar_1024_nml,
                 lstar_1024_gls,
                 lstar_1024_spc,
                 lstar_1024_ilm,
                 lstar_1024_ao,
                 lstar_1024_cav,
                 lstar_512_col,
                 lstar_512_nml,
                 lstar_512_gls,
                 lstar_512_spc,
                 lstar_512_ilm,
                 lstar_512_ao,
                 lstar_512_cav]

lmg_hemlok_2048_col           = int('0000000253471000',16)
lmg_hemlok_2048_nml           = int('00000002537C1000',16)
lmg_hemlok_2048_gls           = int('0000000253C61000',16)
lmg_hemlok_2048_spc           = int('0000000253F01000',16)
lmg_hemlok_2048_ilm           = int('00000002541A1000',16)
lmg_hemlok_2048_ao            = int('0000000254441000',16)
lmg_hemlok_2048_cav           = int('00000002546E1000',16)
lmg_hemlok_1024_col           = int('00000002533F1000',16)
lmg_hemlok_1024_nml           = int('00000002536C1000',16)
lmg_hemlok_1024_gls           = int('0000000253BE1000',16)
lmg_hemlok_1024_spc           = int('0000000253E81000',16)
lmg_hemlok_1024_ilm           = int('0000000254121000',16)
lmg_hemlok_1024_ao            = int('00000002543C1000',16)
lmg_hemlok_1024_cav           = int('0000000254661000',16)
lmg_hemlok_512_col            = int('00000002533D1000',16)
lmg_hemlok_512_nml            = int('0000000253681000',16)
lmg_hemlok_512_gls            = int('0000000253BC1000',16)
lmg_hemlok_512_spc            = int('0000000253E61000',16)
lmg_hemlok_512_ilm            = int('0000000254101000',16)
lmg_hemlok_512_ao             = int('00000002543A1000',16)
lmg_hemlok_512_cav            = int('0000000254641000',16)

lmg_hemlok_offsets = [lmg_hemlok_2048_col,
                      lmg_hemlok_2048_nml,
                      lmg_hemlok_2048_gls,
                      lmg_hemlok_2048_spc,
                      lmg_hemlok_2048_ilm,
                      lmg_hemlok_2048_ao,
                      lmg_hemlok_2048_cav,
                      lmg_hemlok_1024_col,
                      lmg_hemlok_1024_nml,
                      lmg_hemlok_1024_gls,
                      lmg_hemlok_1024_spc,
                      lmg_hemlok_1024_ilm,
                      lmg_hemlok_1024_ao,
                      lmg_hemlok_1024_cav,
                      lmg_hemlok_512_col,
                      lmg_hemlok_512_nml,
                      lmg_hemlok_512_gls,
                      lmg_hemlok_512_spc,
                      lmg_hemlok_512_ilm,
                      lmg_hemlok_512_ao,
                      lmg_hemlok_512_cav]

doubletake_2048_col           = int('000000023B1F1000',16)
doubletake_2048_nml           = int('000000023B741000',16)
doubletake_2048_gls           = int('000000023BBE1000',16)
doubletake_2048_spc           = int('000000023BF31000',16)
doubletake_2048_ao            = int('000000023C3D1000',16)
doubletake_2048_cav           = int('000000023C671000',16)
doubletake_1024_col           = int('000000023B0F1000',16)
doubletake_1024_nml           = int('000000023B641000',16)
doubletake_1024_gls           = int('000000023BB61000',16)
doubletake_1024_spc           = int('000000023BE31000',16)
doubletake_1024_ao            = int('000000023C351000',16)
doubletake_1024_cav           = int('000000023C5F1000',16)
doubletake_512_col            = int('000000023B0B1000',16)
doubletake_512_nml            = int('000000023B601000',16)
doubletake_512_gls            = int('000000023BB41000',16)
doubletake_512_spc            = int('000000023BDF1000',16)
doubletake_512_ao             = int('000000023C331000',16)
doubletake_512_cav           = int('000000023C5D1000',16)

doubletake_offsets = [doubletake_2048_col,
                      doubletake_2048_nml,
                      doubletake_2048_gls,
                      doubletake_2048_spc,
                      doubletake_2048_ao,
                      doubletake_2048_cav,
                      doubletake_1024_col,
                      doubletake_1024_nml,
                      doubletake_1024_gls,
                      doubletake_1024_spc,
                      doubletake_1024_ao,
                      doubletake_1024_cav,
                      doubletake_512_col,
                      doubletake_512_nml,
                      doubletake_512_gls,
                      doubletake_512_spc,
                      doubletake_512_ao,
                      doubletake_512_cav]

at_rifle_2048_col             = int('0000000244BD1000',16)
at_rifle_2048_nml             = int('0000000244F21000',16)
at_rifle_2048_gls             = int('00000002453C1000',16)
at_rifle_2048_spc             = int('0000000245661000',16)
at_rifle_2048_ilm             = int('0000000245901000',16)
at_rifle_2048_ao              = int('0000000245BA1000',16)
at_rifle_2048_cav             = int('0000000245E41000',16)
at_rifle_1024_col             = int('0000000244B51000',16)
at_rifle_1024_nml             = int('0000000244E21000',16)
at_rifle_1024_gls             = int('0000000245341000',16)
at_rifle_1024_spc             = int('00000002455E1000',16)
at_rifle_1024_ilm             = int('0000000245881000',16)
at_rifle_1024_ao              = int('0000000245B21000',16)
at_rifle_1024_cav             = int('0000000245DC1000',16)
at_rifle_512_col              = int('0000000244B31000',16)
at_rifle_512_nml              = int('0000000244DE1000',16)
at_rifle_512_gls              = int('0000000245321000',16)
at_rifle_512_spc              = int('00000002455C1000',16)
at_rifle_512_ilm              = int('0000000245861000',16)
at_rifle_512_ao               = int('0000000245B01000',16)
at_rifle_512_cav              = int('0000000245DA1000',16)

at_rifle_offsets = [at_rifle_2048_col,
                    at_rifle_2048_nml,
                    at_rifle_2048_gls,
                    at_rifle_2048_spc,
                    at_rifle_2048_ilm,
                    at_rifle_2048_ao,
                    at_rifle_2048_cav,
                    at_rifle_1024_col,
                    at_rifle_1024_nml,
                    at_rifle_1024_gls,
                    at_rifle_1024_spc,
                    at_rifle_1024_ilm,
                    at_rifle_1024_ao,
                    at_rifle_1024_cav,
                    at_rifle_512_col,
                    at_rifle_512_nml,
                    at_rifle_512_gls,
                    at_rifle_512_spc,
                    at_rifle_512_ilm,
                    at_rifle_512_ao,
                    at_rifle_512_cav]

rspn101_dmr_2048_col          = int('0000000246B61000',16)
rspn101_dmr_2048_nml          = int('0000000246EB1000',16)
rspn101_dmr_2048_gls          = int('0000000247351000',16)
rspn101_dmr_2048_spc          = int('00000002475F1000',16)
rspn101_dmr_2048_ao           = int('0000000247891000',16)
rspn101_dmr_2048_cav          = int('0000000247B31000',16)
rspn101_dmr_1024_col          = int('0000000246AE1000',16)
rspn101_dmr_1024_nml          = int('0000000246DB1000',16)
rspn101_dmr_1024_gls          = int('00000002472D1000',16)
rspn101_dmr_1024_spc          = int('0000000247571000',16)
rspn101_dmr_1024_ao           = int('0000000247811000',16)
rspn101_dmr_1024_cav          = int('0000000247AB1000',16)
rspn101_dmr_512_col           = int('0000000246AC1000',16)
rspn101_dmr_512_nml           = int('0000000246D71000',16)
rspn101_dmr_512_gls           = int('00000002472B1000',16)
rspn101_dmr_512_spc           = int('0000000247551000',16)
rspn101_dmr_512_ao            = int('00000002477F1000',16)
rspn101_dmr_512_cav           = int('0000000247A91000',16)

rspn101_dmr_offsets = [rspn101_dmr_2048_col,
                       rspn101_dmr_2048_nml,
                       rspn101_dmr_2048_gls,
                       rspn101_dmr_2048_spc,
                       rspn101_dmr_2048_ao,
                       rspn101_dmr_2048_cav,
                       rspn101_dmr_1024_col,
                       rspn101_dmr_1024_nml,
                       rspn101_dmr_1024_gls,
                       rspn101_dmr_1024_spc,
                       rspn101_dmr_1024_ao,
                       rspn101_dmr_1024_cav,
                       rspn101_dmr_512_col,
                       rspn101_dmr_512_nml,
                       rspn101_dmr_512_gls,
                       rspn101_dmr_512_spc,
                       rspn101_dmr_512_ao,
                       rspn101_dmr_512_cav,]

w1128_2048_col                = int('000000023F191000',16)
w1128_2048_nml                = int('000000023F4E1000',16)
w1128_2048_gls                = int('000000023F981000',16)
w1128_2048_spc                = int('000000023FC21000',16)
w1128_2048_ilm                = int('000000023FEC1000',16)
w1128_2048_ao                 = int('0000000240161000',16)
w1128_2048_cav                = int('0000000240401000',16)
w1128_1024_col                = int('000000023F111000',16)
w1128_1024_nml                = int('000000023F3E1000',16)
w1128_1024_gls                = int('000000023F901000',16)
w1128_1024_spc                = int('000000023FBA1000',16)
w1128_1024_ilm                = int('000000023FE41000',16)
w1128_1024_ao                 = int('00000002400E1000',16)
w1128_1024_cav                = int('0000000240381000',16)
w1128_512_col                 = int('000000023F0F1000',16)
w1128_512_nml                 = int('000000023F3A1000',16)
w1128_512_gls                 = int('000000023F8E1000',16)
w1128_512_spc                 = int('000000023FB81000',16)
w1128_512_ilm                 = int('000000023FE21000',16)
w1128_512_ao                  = int('00000002400C1000',16)
w1128_512_cav                 = int('0000000240361000',16)

w1128_offsets = [w1128_2048_col,
                 w1128_2048_nml,
                 w1128_2048_gls,
                 w1128_2048_spc,
                 w1128_2048_ilm,
                 w1128_2048_ao,
                 w1128_2048_cav,
                 w1128_1024_col,
                 w1128_1024_nml,
                 w1128_1024_gls,
                 w1128_1024_spc,
                 w1128_1024_ilm,
                 w1128_1024_ao,
                 w1128_1024_cav,
                 w1128_512_col,
                 w1128_512_nml,
                 w1128_512_gls,
                 w1128_512_spc,
                 w1128_512_ilm,
                 w1128_512_ao,
                 w1128_512_cav]

mastiff_stgn_2048_col         = int('0000000213ED1000',16)
mastiff_stgn_2048_nml         = int('0000000214221000',16)
mastiff_stgn_2048_gls         = int('00000002146C1000',16)
mastiff_stgn_2048_spc         = int('0000000214961000',16)
mastiff_stgn_2048_ilm         = int('0000000214C01000',16)
mastiff_stgn_2048_ao          = int('0000000214EA1000',16)
mastiff_stgn_2048_cav         = int('0000000215141000',16)
mastiff_stgn_1024_col         = int('0000000213E51000',16)
mastiff_stgn_1024_nml         = int('0000000214121000',16)
mastiff_stgn_1024_gls         = int('0000000214641000',16)
mastiff_stgn_1024_spc         = int('00000002148E1000',16)
mastiff_stgn_1024_ilm         = int('0000000214B81000',16)
mastiff_stgn_1024_ao          = int('0000000214E21000',16)
mastiff_stgn_1024_cav         = int('00000002150C1000',16)
mastiff_stgn_512_col          = int('0000000213E31000',16)
mastiff_stgn_512_nml          = int('00000002140E1000',16)
mastiff_stgn_512_gls          = int('0000000214621000',16)
mastiff_stgn_512_spc          = int('00000002148C1000',16)
mastiff_stgn_512_ilm          = int('0000000214B61000',16)
mastiff_stgn_512_ao           = int('0000000214E01000',16)
mastiff_stgn_512_cav          = int('00000002150A1000',16)

mastiff_stgn_offsets = [mastiff_stgn_2048_col,
                        mastiff_stgn_2048_nml,
                        mastiff_stgn_2048_gls,
                        mastiff_stgn_2048_spc,
                        mastiff_stgn_2048_ilm,
                        mastiff_stgn_2048_ao,
                        mastiff_stgn_2048_cav,
                        mastiff_stgn_1024_col,
                        mastiff_stgn_1024_nml,
                        mastiff_stgn_1024_gls,
                        mastiff_stgn_1024_spc,
                        mastiff_stgn_1024_ilm,
                        mastiff_stgn_1024_ao,
                        mastiff_stgn_1024_cav,
                        mastiff_stgn_512_col,
                        mastiff_stgn_512_nml,
                        mastiff_stgn_512_gls,
                        mastiff_stgn_512_spc,
                        mastiff_stgn_512_ilm,
                        mastiff_stgn_512_ao,
                        mastiff_stgn_512_cav]

pulse_lmg_2048_col            = int('000000024C101000',16)
pulse_lmg_2048_nml            = int('000000024C451000',16)
pulse_lmg_2048_gls            = int('000000024C8F1000',16)
pulse_lmg_2048_spc            = int('000000024CB91000',16)
pulse_lmg_2048_ilm            = int('000000024CE31000',16)
pulse_lmg_2048_ao             = int('000000024D0D1000',16)
pulse_lmg_2048_cav            = int('000000024D371000',16)
pulse_lmg_1024_col            = int('000000024C081000',16)
pulse_lmg_1024_nml            = int('000000024C351000',16)
pulse_lmg_1024_gls            = int('000000024C871000',16)
pulse_lmg_1024_spc            = int('000000024CB11000',16)
pulse_lmg_1024_ilm            = int('000000024CDB1000',16)
pulse_lmg_1024_ao             = int('000000024D051000',16)
pulse_lmg_1024_cav            = int('000000024D2F1000',16)
pulse_lmg_512_col             = int('000000024C061000',16)
pulse_lmg_512_nml             = int('000000024C311000',16)
pulse_lmg_512_gls             = int('000000024C851000',16)
pulse_lmg_512_spc             = int('000000024CAF1000',16)
pulse_lmg_512_ilm             = int('000000024CD91000',16)
pulse_lmg_512_ao              = int('000000024D031000',16)
pulse_lmg_512_cav             = int('000000024D2D1000',16)

pulse_lmg_offsets = [pulse_lmg_2048_col,
                     pulse_lmg_2048_nml,
                     pulse_lmg_2048_gls,
                     pulse_lmg_2048_spc,
                     pulse_lmg_2048_ilm,
                     pulse_lmg_2048_ao,
                     pulse_lmg_2048_cav,
                     pulse_lmg_1024_col,
                     pulse_lmg_1024_nml,
                     pulse_lmg_1024_gls,
                     pulse_lmg_1024_spc,
                     pulse_lmg_1024_ilm,
                     pulse_lmg_1024_ao,
                     pulse_lmg_1024_cav,
                     pulse_lmg_512_col,
                     pulse_lmg_512_nml,
                     pulse_lmg_512_gls,
                     pulse_lmg_512_spc,
                     pulse_lmg_512_ilm,
                     pulse_lmg_512_ao,
                     pulse_lmg_512_cav]

epg_2048_col                  = int('000000023D0F1000',16)
epg_2048_nml                  = int('000000023D441000',16)
epg_2048_gls                  = int('000000023D8E1000',16)
epg_2048_spc                  = int('000000023DB81000',16)
epg_2048_ilm                  = int('000000023DE21000',16)
epg_2048_ao                   = int('000000023E0C1000',16)
epg_2048_cav                  = int('000000023E361000',16)
epg_1024_col                  = int('000000023D071000',16)
epg_1024_nml                  = int('000000023D341000',16)
epg_1024_gls                  = int('000000023D861000',16)
epg_1024_spc                  = int('000000023DB01000',16)
epg_1024_ilm                  = int('000000023DDA1000',16)
epg_1024_ao                   = int('000000023E041000',16)
epg_1024_cav                  = int('000000023E2E1000',16)
epg_512_col                   = int('000000023D051000',16)
epg_512_nml                   = int('000000023D301000',16)
epg_512_gls                   = int('000000023D841000',16)
epg_512_spc                   = int('000000023DAE1000',16)
epg_512_ilm                   = int('000000023DD81000',16)
epg_512_ao                    = int('000000023E021000',16)
epg_512_cav                   = int('000000023E2C1000',16)

epg_offsets = [epg_2048_col,
               epg_2048_nml,
               epg_2048_gls,
               epg_2048_spc,
               epg_2048_ilm,
               epg_2048_ao,
               epg_2048_cav,
               epg_1024_col,
               epg_1024_nml,
               epg_1024_gls,
               epg_1024_spc,
               epg_2048_ilm,
               epg_1024_ao,
               epg_2048_cav,
               epg_512_col,
               epg_512_nml,
               epg_512_gls,
               epg_512_spc,
               epg_512_ilm,
               epg_512_ao,
               epg_512_cav]

auto_rocket_launcher_2048_col = int('0000000251511000',16)
auto_rocket_launcher_2048_nml = int('0000000251A61000',16)
auto_rocket_launcher_2048_gls = int('0000000251F01000',16)
auto_rocket_launcher_2048_spc = int('00000002521A1000',16)
auto_rocket_launcher_2048_ao  = int('0000000252441000',16)
auto_rocket_launcher_2048_cav = int('00000002526E1000',16)
auto_rocket_launcher_1024_col = int('0000000251411000',16)
auto_rocket_launcher_1024_nml = int('0000000251961000',16)
auto_rocket_launcher_1024_gls = int('0000000251E81000',16)
auto_rocket_launcher_1024_spc = int('0000000252121000',16)
auto_rocket_launcher_1024_ao  = int('00000002523C1000',16)
auto_rocket_launcher_1024_cav = int('0000000252661000',16)
auto_rocket_launcher_512_col  = int('00000002513D1000',16)
auto_rocket_launcher_512_nml  = int('0000000251921000',16)
auto_rocket_launcher_512_gls  = int('0000000251E61000',16)
auto_rocket_launcher_512_spc  = int('0000000252101000',16)
auto_rocket_launcher_512_ao   = int('00000002523A1000',16)
auto_rocket_launcher_512_cav  = int('0000000252641000',16)
auto_rocket_launcher_256_col  = int('00000002513C1000',16)
auto_rocket_launcher_256_nml  = int('0000000251911000',16)

auto_rocket_launcher_offsets = [auto_rocket_launcher_2048_col,
                                auto_rocket_launcher_2048_nml,
                                auto_rocket_launcher_2048_gls,
                                auto_rocket_launcher_2048_spc,
                                auto_rocket_launcher_2048_ao,
                                auto_rocket_launcher_2048_cav,
                                auto_rocket_launcher_1024_col,
                                auto_rocket_launcher_1024_nml,
                                auto_rocket_launcher_1024_gls,
                                auto_rocket_launcher_1024_spc,
                                auto_rocket_launcher_1024_ao,
                                auto_rocket_launcher_1024_cav,
                                auto_rocket_launcher_512_col,
                                auto_rocket_launcher_512_nml,
                                auto_rocket_launcher_512_gls,
                                auto_rocket_launcher_512_spc,
                                auto_rocket_launcher_512_ao,
                                auto_rocket_launcher_512_cav]

softball_at_2048_col          = int('000000021C1F1000',16)
softball_at_2048_nml          = int('000000021C541000',16)
softball_at_2048_gls          = int('000000021C9E1000',16)
softball_at_2048_spc          = int('000000021CC81000',16)
softball_at_2048_ao           = int('000000021CF21000',16)
softball_at_2048_cav          = int('000000021D1C1000',16)
softball_at_1024_col          = int('000000021C171000',16)
softball_at_1024_nml          = int('000000021C441000',16)
softball_at_1024_gls          = int('000000021C961000',16)
softball_at_1024_spc          = int('000000021CC01000',16)
softball_at_1024_ao           = int('000000021CEA1000',16)
softball_at_1024_cav          = int('000000021D141000',16)
softball_at_512_col           = int('000000021C151000',16)
softball_at_512_nml           = int('000000021C401000',16)
softball_at_512_gls           = int('000000021C941000',16)
softball_at_512_spc           = int('000000021CBE1000',16)
softball_at_512_ao            = int('000000021CE81000',16)
softball_at_512_cav           = int('000000021D121000',16)
 
softball_at_offsets = [softball_at_2048_col,
                       softball_at_2048_nml,
                       softball_at_2048_gls,
                       softball_at_2048_spc,
                       softball_at_2048_ao,
                       softball_at_2048_cav,
                       softball_at_1024_col,
                       softball_at_1024_nml,
                       softball_at_1024_gls,
                       softball_at_1024_spc,
                       softball_at_1024_ao,
                       softball_at_512_cav,
                       softball_at_512_col,
                       softball_at_512_nml,
                       softball_at_512_gls,
                       softball_at_512_spc,
                       softball_at_512_ao,
                       softball_at_512_cav]

pstl_sa3_1024_col             = int('000000024BA31000',16)
pstl_sa3_1024_nml             = int('000000024BB01000',16)
pstl_sa3_1024_gls             = int('000000024BC21000',16)
pstl_sa3_1024_spc             = int('000000024BCC1000',16)
pstl_sa3_1024_ao              = int('000000024BD61000',16)
pstl_sa3_1024_cav             = int('000000024BE01000',16)
pstl_sa3_512_col              = int('000000024BA11000',16)
pstl_sa3_512_nml              = int('000000024BAC1000',16)
pstl_sa3_512_gls              = int('000000024BC01000',16)
pstl_sa3_512_spc              = int('000000024BD61000',16)
pstl_sa3_512_ao               = int('000000024BD41000',16)
pstl_sa3_512_cav              = int('000000024BDE1000',16)

pstl_sa3_offsets = [pstl_sa3_1024_col,
                    pstl_sa3_1024_nml,
                    pstl_sa3_1024_gls,
                    pstl_sa3_1024_spc,
                    pstl_sa3_1024_ao,
                    pstl_sa3_1024_cav,
                    pstl_sa3_512_col,
                    pstl_sa3_512_nml,
                    pstl_sa3_512_gls,
                    pstl_sa3_512_spc,
                    pstl_sa3_512_ao,
                    pstl_sa3_512_cav]

p2011_1024_col                = int('00000002487D1000',16)
p2011_1024_nml                = int('00000002488A1000',16)
p2011_1024_gls                = int('00000002489C1000',16)
p2011_1024_spc                = int('0000000248A61000',16)
p2011_1024_ilm                = int('0000000248B01000',16)
p2011_1024_ao                 = int('0000000248BA1000',16)
p2011_1024_cav                = int('0000000248C41000',16)
p2011_512_col                 = int('0000000248861000',16)
p2011_512_nml                 = int('0000000248851000',16)
p2011_512_gls                 = int('00000002489A1000',16)
p2011_512_spc                 = int('0000000248A41000',16)
p2011_512_ilm                 = int('0000000248AE1000',16)
p2011_512_ao                  = int('0000000248B81000',16)
p2011_512_cav                 = int('0000000248C21000',16)

p2011_offsets = [p2011_1024_col,
                 p2011_1024_nml,
                 p2011_1024_gls,
                 p2011_1024_spc,
                 p2011_1024_ilm,
                 p2011_1024_ao,
                 p2011_1024_cav,
                 p2011_512_col,
                 p2011_512_nml,
                 p2011_512_gls,
                 p2011_512_spc,
                 p2011_512_ilm,
                 p2011_512_ao,
                 p2011_512_cav]

p2011_auto_1024_col           = int('000000024FD01000',16)
p2011_auto_1024_nml           = int('000000024FDD1000',16)
p2011_auto_1024_gls           = int('000000024FEF1000',16)
p2011_auto_1024_spc           = int('000000024FF91000',16)
p2011_auto_1024_ao            = int('0000000250051000',16)
p2011_auto_1024_cav           = int('00000002500F1000',16)
p2011_auto_512_col            = int('000000024FCE1000',16)
p2011_auto_512_nml            = int('000000024FD91000',16)
p2011_auto_512_gls            = int('000000024FED1000',16)
p2011_auto_512_spc            = int('000000024FF71000',16)
p2011_auto_512_ilm            = int('0000000250011000',16)
p2011_auto_512_ao             = int('0000000250031000',16)
p2011_auto_512_cav            = int('00000002500D1000',16)

p2011_auto_offsets = [p2011_auto_1024_col,
                      p2011_auto_1024_nml,
                      p2011_auto_1024_gls,
                      p2011_auto_1024_spc,
                      p2011_auto_1024_ao,
                      p2011_auto_1024_cav,
                      p2011_auto_512_col,
                      p2011_auto_512_nml,
                      p2011_auto_512_gls,
                      p2011_auto_512_spc,
                      p2011_auto_512_ao,
                      p2011_auto_512_cav]

p2011sp_1024_col              = int('0000000252E41000',16)
p2011sp_1024_nml              = int('0000000252F11000',16)
p2011sp_1024_gls              = int('0000000253031000',16)
p2011sp_1024_spc              = int('00000002530D1000',16)
p2011sp_1024_ilm              = int('0000000253171000',16)
p2011sp_1024_ao               = int('0000000253211000',16)
p2011sp_1024_cav              = int('00000002532B1000',16)
p2011sp_512_col               = int('0000000252E21000',16)
p2011sp_512_nml               = int('0000000252ED1000',16)
p2011sp_512_gls               = int('0000000253011000',16)
p2011sp_512_spc               = int('00000002530B1000',16)
p2011sp_512_ilm               = int('0000000253151000',16)
p2011sp_512_ao                = int('00000002531F1000',16)
p2011sp_512_cav               = int('0000000253291000',16)

p2011sp_offsets = [p2011sp_1024_col,
                   p2011sp_1024_nml,
                   p2011sp_1024_gls,
                   p2011sp_1024_spc,
                   p2011sp_1024_ilm,
                   p2011sp_1024_ao,
                   p2011sp_1024_cav,
                   p2011sp_512_col,
                   p2011sp_512_nml,
                   p2011sp_512_gls,
                   p2011sp_512_spc,
                   p2011sp_512_ilm,
                   p2011sp_512_ao,
                   p2011sp_512_cav]

b3wing_1024_col               = int('00000002618A1000',16)
b3wing_1024_nml               = int('0000000261971000',16)
b3wing_1024_gls               = int('0000000261A91000',16)
b3wing_1024_spc               = int('0000000261B31000',16)
b3wing_1024_ilm               = int('0000000261BD1000',16)
b3wing_1024_ao                = int('0000000261C71000',16)
b3wing_1024_cav               = int('0000000261D11000',16)
b3wing_512_col                = int('0000000261881000',16)
b3wing_512_nml                = int('0000000261931000',16)
b3wing_512_gls                = int('0000000261A71000',16)
b3wing_512_spc                = int('0000000261B11000',16)
b3wing_512_ilm                = int('0000000261BB1000',16)
b3wing_512_ao                 = int('0000000261C51000',16)
b3wing_512_cav                = int('0000000261CF1000',16)

b3wing_offsets = [b3wing_1024_col,
                  b3wing_1024_nml,
                  b3wing_1024_gls,
                  b3wing_1024_spc,
                  b3wing_1024_ilm,
                  b3wing_1024_ao,
                  b3wing_1024_cav,
                  b3wing_512_col,
                  b3wing_512_nml,
                  b3wing_512_gls,
                  b3wing_512_spc,
                  b3wing_512_ilm,
                  b3wing_512_ao,
                  b3wing_512_cav]



wingman_elite_1024_col        = int('00000002618A1000',16)
wingman_elite_1024_nml        = int('0000000261971000',16)
wingman_elite_1024_gls        = int('0000000261A91000',16)
wingman_elite_1024_spc        = int('0000000261B31000',16)
wingman_elite_1024_ilm        = int('0000000261BD1000',16)
wingman_elite_1024_ao         = int('0000000261C71000',16)
wingman_elite_1024_cav        = int('0000000261D11000',16)
wingman_elite_512_col         = int('0000000261881000',16)
wingman_elite_512_nml         = int('0000000261931000',16)
wingman_elite_512_gls         = int('0000000261A71000',16)
wingman_elite_512_spc         = int('0000000261B11000',16)
wingman_elite_512_ilm         = int('0000000261BB1000',16)
wingman_elite_512_ao          = int('0000000261C51000',16)
wingman_elite_512_cav         = int('0000000261CF1000',16)

wingman_elite_offsets = [wingman_elite_1024_col,
                         wingman_elite_1024_nml,
                         wingman_elite_1024_gls,
                         wingman_elite_1024_spc,
                         wingman_elite_1024_ilm,
                         wingman_elite_1024_ao,
                         wingman_elite_1024_cav,
                         wingman_elite_512_col,
                         wingman_elite_512_nml,
                         wingman_elite_512_gls,
                         wingman_elite_512_spc,
                         wingman_elite_512_ilm,
                         wingman_elite_512_ao,
                         wingman_elite_512_cav]


shoulder_rocket_sram_2048_col = int('000000022B0D1000',16)
shoulder_rocket_sram_2048_nml = int('000000022B621000',16)
shoulder_rocket_sram_2048_gls = int('000000022BAC1000',16)
shoulder_rocket_sram_2048_spc = int('000000022BD61000',16)
shoulder_rocket_sram_2048_ilm = int('000000022C001000',16)
shoulder_rocket_sram_2048_ao  = int('000000022C2A1000',16)
shoulder_rocket_sram_2048_cav = int('000000022C541000',16)
shoulder_rocket_sram_1024_col = int('000000022AFD1000',16)
shoulder_rocket_sram_1024_nml = int('000000022B521000',16)
shoulder_rocket_sram_1024_gls = int('000000022BA41000',16)
shoulder_rocket_sram_1024_spc = int('000000022BCE1000',16)
shoulder_rocket_sram_1024_ilm = int('000000022BF81000',16)
shoulder_rocket_sram_1024_ao  = int('000000022C221000',16)
shoulder_rocket_sram_1024_cav = int('000000022C4C1000',16)
shoulder_rocket_sram_512_col  = int('000000022AF91000',16)
shoulder_rocket_sram_512_nml  = int('000000022B4E1000',16)
shoulder_rocket_sram_512_gls  = int('000000022BA21000',16)
shoulder_rocket_sram_512_spc  = int('000000022BCC1000',16)
shoulder_rocket_sram_512_ilm  = int('000000022BF61000',16)
shoulder_rocket_sram_512_ao   = int('000000022C201000',16)
shoulder_rocket_sram_512_cav  = int('000000022C4A1000',16)
shoulder_rocket_sram_256_col  = int('000000022AF81000',16)
shoulder_rocket_sram_256_nml  = int('000000022B4D1000',16)

shoulder_rocket_sram_offsets = [shoulder_rocket_sram_2048_col,
                                shoulder_rocket_sram_2048_nml,
                                shoulder_rocket_sram_2048_gls,
                                shoulder_rocket_sram_2048_spc,
                                shoulder_rocket_sram_2048_ilm,
                                shoulder_rocket_sram_2048_ao,
                                shoulder_rocket_sram_2048_cav,
                                shoulder_rocket_sram_1024_col,
                                shoulder_rocket_sram_1024_nml,
                                shoulder_rocket_sram_1024_gls,
                                shoulder_rocket_sram_1024_spc,
                                shoulder_rocket_sram_1024_ilm,
                                shoulder_rocket_sram_1024_ao,
                                shoulder_rocket_sram_1024_cav,
                                shoulder_rocket_sram_512_col,
                                shoulder_rocket_sram_512_nml,
                                shoulder_rocket_sram_512_gls,
                                shoulder_rocket_sram_512_spc,
                                shoulder_rocket_sram_512_ilm,
                                shoulder_rocket_sram_512_ao,
                                shoulder_rocket_sram_512_cav]

defender_2048_col             = int('0000000238E71000',16)
defender_2048_nml             = int('00000002391C1000',16)
defender_2048_gls             = int('0000000239661000',16)
defender_2048_spc             = int('0000000239901000',16)
defender_2048_ilm             = int('0000000239BA1000',16)
defender_2048_ao              = int('0000000239E41000',16)
defender_2048_cav             = int('000000023A0E1000',16)
defender_1024_col             = int('0000000238DF1000',16)
defender_1024_nml             = int('00000002390C1000',16)
defender_1024_gls             = int('00000002395E1000',16)
defender_1024_spc             = int('0000000239881000',16)
defender_1024_ilm             = int('0000000239B21000',16)
defender_1024_ao              = int('0000000239DC1000',16)
defender_1024_cav             = int('000000023A061000',16)
defender_512_col              = int('0000000238DD1000',16)
defender_512_nml              = int('0000000239081000',16)
defender_512_gls              = int('00000002395C1000',16)
defender_512_spc              = int('0000000239861000',16)
defender_512_ilm              = int('0000000239B01000',16)
defender_512_ao               = int('0000000239DA1000',16)
defender_512_cav              = int('000000023A041000',16)

defender_offsets = [defender_2048_col,
                    defender_2048_nml,
                    defender_2048_gls,
                    defender_2048_spc,
                    defender_2048_ilm,
                    defender_2048_ao,
                    defender_2048_cav,
                    defender_1024_col,
                    defender_1024_nml,
                    defender_1024_gls,
                    defender_1024_spc,
                    defender_1024_ilm,
                    defender_1024_ao,
                    defender_1024_cav,
                    defender_512_col,
                    defender_512_nml,
                    defender_512_gls,
                    defender_512_spc,
                    defender_512_ilm,
                    defender_512_ao,
                    defender_512_cav]

mgl_at_2048_col               = int('0000000215E61000',16)
mgl_at_2048_nml               = int('00000002161B1000',16)
mgl_at_2048_gls               = int('0000000216651000',16)
mgl_at_2048_spc               = int('00000002168F1000',16)
mgl_at_2048_ao                = int('0000000216B91000',16)
mgl_at_2048_cav               = int('0000000216E31000',16)
mgl_at_1024_col               = int('0000000215DE1000',16)
mgl_at_1024_nml               = int('00000002160B1000',16)
mgl_at_1024_gls               = int('00000002165D1000',16)
mgl_at_1024_spc               = int('0000000216871000',16)
mgl_at_1024_ao                = int('0000000216B11000',16)
mgl_at_1024_cav               = int('0000000216DB1000',16)
mgl_at_512_col                = int('0000000215DC1000',16)
mgl_at_512_nml                = int('0000000216071000',16)
mgl_at_512_gls                = int('00000002165B1000',16)
mgl_at_512_spc                = int('0000000216851000',16)
mgl_at_512_ao                 = int('0000000216AF1000',16)
mgl_at_512_cav               = int('0000000216D91000',16)

mgl_at_offsets = [mgl_at_2048_col,
                  mgl_at_2048_nml,
                  mgl_at_2048_gls,
                  mgl_at_2048_spc,
                  mgl_at_2048_ao,
                  mgl_at_2048_cav,
                  mgl_at_1024_col,
                  mgl_at_1024_nml,
                  mgl_at_1024_gls,
                  mgl_at_1024_spc,
                  mgl_at_1024_ao,
                  mgl_at_1024_cav,
                  mgl_at_512_col,
                  mgl_at_512_nml,
                  mgl_at_512_gls,
                  mgl_at_512_spc,
                  mgl_at_512_ao,
                  mgl_at_512_cav]

arc_launcher_2048_col         = int('0000000227E21000',16)
arc_launcher_2048_nml         = int('0000000228171000',16)
arc_launcher_2048_gls         = int('0000000228611000',16)
arc_launcher_2048_spc         = int('00000002288B1000',16)
arc_launcher_2048_ilm         = int('0000000228B51000',16)
arc_launcher_2048_ao          = int('0000000228DF1000',16)
arc_launcher_2048_cav         = int('0000000229091000',16)
arc_launcher_1024_col         = int('0000000227DA1000',16)
arc_launcher_1024_nml         = int('0000000228071000',16)
arc_launcher_1024_gls         = int('0000000228591000',16)
arc_launcher_1024_spc         = int('0000000228831000',16)
arc_launcher_1024_ilm         = int('0000000228AD1000',16)
arc_launcher_1024_ao          = int('0000000228D71000',16)
arc_launcher_1024_cav         = int('0000000229011000',16)
arc_launcher_512_col          = int('0000000227D81000',16)
arc_launcher_512_nml          = int('0000000228031000',16)
arc_launcher_512_gls          = int('0000000228571000',16)
arc_launcher_512_spc          = int('0000000228811000',16)
arc_launcher_512_ilm          = int('0000000228AB1000',16)
arc_launcher_512_ao           = int('0000000228D51000',16)
arc_launcher_512_cav          = int('0000000228FF1000',16)

arc_launcher_offsets = [arc_launcher_2048_col,
                        arc_launcher_2048_nml,
                        arc_launcher_2048_gls,
                        arc_launcher_2048_spc,
                        arc_launcher_2048_ilm,
                        arc_launcher_2048_ao,
                        arc_launcher_2048_cav,
                        arc_launcher_1024_col,
                        arc_launcher_1024_nml,
                        arc_launcher_1024_gls,
                        arc_launcher_1024_spc,
                        arc_launcher_1024_ilm,
                        arc_launcher_1024_ao,
                        arc_launcher_1024_cav,
                        arc_launcher_512_col,
                        arc_launcher_512_nml,
                        arc_launcher_512_gls,
                        arc_launcher_512_spc,
                        arc_launcher_512_ilm,
                        arc_launcher_512_ao,
                        arc_launcher_512_cav]

#HEADER LENGTH

header_length = 128

"""
File Indentification
"""

pc_stream = 'pc_stream.starpak'

path_2048 = 'dds_2048/'
path_1024 = 'dds_1024/'
path_512  = 'dds_512/'

dds_2048_col = ['not found']
dds_2048_nml = ['not found']
dds_2048_gls = ['not found']
dds_2048_spc = ['not found']
dds_2048_ilm = ['not found']
dds_2048_ao  = ['not found']
dds_2048_cav = ['not found']

dds_1024_col = ['not found']
dds_1024_nml = ['not found']
dds_1024_gls = ['not found']
dds_1024_spc = ['not found']
dds_1024_ilm = ['not found']
dds_1024_ao  = ['not found']
dds_1024_cav = ['not found']

dds_512_col = ['not found']
dds_512_nml = ['not found']
dds_512_gls = ['not found']
dds_512_spc = ['not found']
dds_512_ilm = ['not found']
dds_512_ao  = ['not found']
dds_512_cav = ['not found']


# 2048
for file in os.listdir(path_2048):
    if   file[-7:-4] == 'col' in file:
         dds_2048_col = [path_2048 + file]
    elif file[-7:-4] == 'nml' in file:
         dds_2048_nml = [path_2048 + file]
    elif file[-7:-4] == 'gls' in file:
         dds_2048_gls = [path_2048 + file]
    elif file[-7:-4] == 'spc' in file:
         dds_2048_spc = [path_2048 + file]
    elif file[-7:-4] == 'ilm' in file:
         dds_2048_ilm = [path_2048 + file]
    elif file[-6:-4] == 'ao' in file:
         dds_2048_ao = [path_2048 + file]
    elif file[-7:-4] == 'cav' in file:
         dds_2048_cav = [path_2048 + file]
    else:
        pass

#1024    
for file in os.listdir(path_1024):
    if   file[-7:-4] == 'col' in file:
         dds_1024_col = [path_1024 + file]
    elif file[-7:-4] == 'nml' in file:
         dds_1024_nml = [path_1024 + file]
    elif file[-7:-4] == 'gls' in file:
         dds_1024_gls = [path_1024 + file]
    elif file[-7:-4] == 'spc' in file:
         dds_1024_spc = [path_1024 + file]
    elif file[-7:-4] == 'ilm' in file:
         dds_1024_ilm = [path_1024 + file]         
    elif file[-6:-4] == 'ao' in file:
         dds_1024_ao = [path_1024 + file]
    elif file[-7:-4] == 'cav' in file:
         dds_1024_cav = [path_1024 + file]         
    else:
        pass

#512    
for file in os.listdir(path_512):
    if   file[-7:-4] == 'col' in file:
         dds_512_col = [path_512 + file]
    elif file[-7:-4] == 'nml' in file:
         dds_512_nml = [path_512 + file]
    elif file[-7:-4] == 'gls' in file:
         dds_512_gls = [path_512 + file]
    elif file[-7:-4] == 'spc' in file:
         dds_512_spc = [path_512 + file]
    elif file[-7:-4] == 'ilm' in file:
         dds_512_ilm = [path_512 + file]         
    elif file[-6:-4] == 'ao' in file:
         dds_512_ao = [path_512 + file]
    elif file[-7:-4] == 'cav' in file:
         dds_512_cav = [path_512 + file]         
    else:
        pass

# FILE LISTS

files_2048 = dds_2048_col + dds_2048_nml + dds_2048_gls + dds_2048_spc +\
             dds_2048_ilm + dds_2048_ao  + dds_2048_cav
files_1024 = dds_1024_col + dds_1024_nml + dds_1024_gls + dds_1024_spc +\
             dds_1024_ilm + dds_1024_ao  + dds_1024_cav
files_512  = dds_512_col + dds_512_nml + dds_512_gls + dds_512_spc +\
             dds_512_ilm + dds_512_ao  + dds_512_cav

files_2048_no_ilm = dds_2048_col + dds_2048_nml + dds_2048_gls +\
                    dds_2048_spc + dds_2048_ao  + dds_2048_cav
files_1024_no_ilm = dds_1024_col + dds_1024_nml + dds_1024_gls +\
                    dds_1024_spc + dds_1024_ao  + dds_1024_cav
files_512_no_ilm  = dds_512_col + dds_512_nml + dds_512_gls +\
                    dds_512_spc + dds_512_ao  + dds_512_cav
files_2048_no_cav = dds_2048_col + dds_2048_nml + dds_2048_gls +\
                    dds_2048_spc + dds_2048_ilm + dds_2048_ao
files_1024_no_cav = dds_1024_col + dds_1024_nml + dds_1024_gls +\
                    dds_1024_spc + dds_1024_ilm + dds_1024_ao
files_512_no_cav  = dds_512_col + dds_512_nml + dds_512_gls +\
                    dds_512_spc + dds_512_ilm + dds_512_ao
             
files_list_full   = files_2048 + files_1024 + files_512
files_list_pstl   = files_1024 + files_512

files_full_ilm = files_2048_no_ilm + files_1024_no_ilm + files_512_no_ilm
files_pstl_ilm = files_1024_no_ilm + files_512_no_ilm
files_full_cav = files_2048_no_cav + files_1024_no_cav + files_512_no_cav

files_pro = files_512

"""
Item Data
"""

rspn101                       = {'name' : 'R-201 Carbine',
                                 'offsets' : rspn101_offsets,
                                 'file_type' : files_list_full}
#r101_sfp                     = {'name' : 'R-101 Carbine',
#                                'offsets' : rspn101_sfp_offsets,
#                                'file_type' : files_list_full}
m1a1_hemlok                   = {'name' : 'Hemlock BF-R',
                                 'offsets' : m1a1_hemlok_offsets,
                                 'file_type' : files_list_full}
vinson                        = {'name' : 'V-47 Flatline',
                                 'offsets' : vinson_offsets,
                                 'file_type' : files_list_full}
g2                            = {'name' : 'G2A5',
                                 'offsets' : g2_offsets,
                                 'file_type' : files_list_full}
alternator_smg                = {'name' : 'Alternator',
                                 'offsets' : alternator_smg_offsets,
                                 'file_type' : files_full_ilm}
car101                        = {'name' : 'CAR',
                                 'offsets' : car101_offsets,
                                 'file_type' : files_list_full}
r97                           = {'name' : 'R-97',
                                 'offsets' : r97_offsets,
                                 'file_type' : files_list_full}
hemlok_smg                    = {'name' : 'Volt',
                                 'offsets' : hemlok_smg_offsets,
                                 'file_type' : files_list_full}
hemlok_br                     = {'name' : 'Devotion',
                                 'offsets' : hemlok_br_offsets,
                                 'file_type' : files_full_cav}
lstar                         = {'name' : 'L-STAR',
                                 'offsets' : lstar_offsets,
                                 'file_type' : files_list_full}
lmg_hemlok                    = {'name' : 'Spitfire',
                                 'offsets' : lmg_hemlok_offsets,
                                 'file_type' : files_list_full}
doubletake                    = {'name' : 'Double Take',
                                 'offsets' : doubletake_offsets,
                                 'file_type' : files_full_ilm}
at_rifle                      = {'name' : 'Kraber',
                                 'offsets' : at_rifle_offsets,
                                 'file_type' : files_list_full}
rspn101_dmr                   = {'name' : 'Longbow DMR',
                                 'offsets' : rspn101_dmr_offsets,
                                 'file_type' : files_full_ilm}
w1128                         = {'name' : 'EVA-8 Auto',
                                 'offsets' : w1128_offsets,
                                 'file_type' : files_list_full}
mastiff_stgn                  = {'name' : 'Mastiff',
                                 'offsets' : mastiff_stgn_offsets,
                                 'file_type' : files_list_full}
pulse_lmg                     = {'name' : 'Cold War EM-4',
                                 'offsets' : pulse_lmg_offsets,
                                 'file_type' : files_list_full}
epg                           = {'name' : 'EPG',
                                 'offsets' : epg_offsets,
                                 'file_type' : files_list_full}
auto_rocket_launcher_ar       = {'name' : 'Sidewinder SMR',
                                 'offsets' : auto_rocket_launcher_offsets,
                                 'file_type' : files_full_ilm}
softball_at                   = {'name' : 'Softball',
                                 'offsets' : softball_at_offsets,
                                 'file_type' : files_full_ilm}
pstl_sa3                      = {'name' : 'Mozambique',
                                 'offsets' : pstl_sa3_offsets,
                                 'file_type' : files_pstl_ilm}
p2011                         = {'name' : 'P2016',
                                 'offsets' : p2011_offsets,
                                 'file_type' : files_list_pstl}
p2011_auto                    = {'name' : 'RE-45 Auto',
                                 'offsets' : p2011_auto_offsets,
                                 'file_type' : files_pstl_ilm}
p2011sp                       = {'name' : 'Smart Pistol',
                                 'offsets' : p2011sp_offsets,
                                 'file_type' : files_list_pstl}
b3wing                        = {'name' : 'Wingman B3',
                                 'offsets' : b3wing_offsets,
                                 'file_type' : files_list_pstl}
wingman_elite                = {'name' : 'Wingman Elite',
                                'offsets' : wingman_elite_offsets,
                                'file_type' : files_list_pstl}
shoulder_rocket_sram          = {'name' : 'Archer',
                                 'offsets' : shoulder_rocket_sram_offsets,
                                 'file_type' : files_list_full}
defender                      = {'name' : 'Charge Rifle',
                                 'offsets' : defender_offsets,
                                 'file_type' : files_list_full}
mgl_at                        = {'name' : 'MGL',
                                 'offsets' : mgl_at_offsets,
                                 'file_type' : files_full_ilm}
arc_launcher                  = {'name' : 'Thunderbolt LG-97',
                                 'offsets' : arc_launcher_offsets,
                                 'file_type' : files_list_full}
hcog2                        = {'name' : 'Hcog',
                                 'offsets' : hcog2_offsets,
                                 'file_type' : files_list_pstl}
threat_w_scope               = {'name' : 'Threat Scope',
                                 'offsets' : threat_w_scope_offsets,
                                 'file_type' : files_list_pstl}
aog_sight                    = {'name' : 'Aog Sight',
                                 'offsets' : aog_sight_offsets,
                                 'file_type' : files_list_pstl}
holo_reflex_sight            = {'name' : 'Holo Reflex Sight',
                                 'offsets' : holo_reflex_sight_magnifier_offsets,
                                 'file_type' : files_list_pstl}
acgs_sight                   = {'name' : 'Acog Sight',
                                 'offsets' : acgs_sight_offsets,
                                 'file_type' : files_list_pstl}
threat_scope_sniper          = {'name' : 'Threat Scope Sniper',
                                 'offsets' : threat_scope_sniper_offsets,
                                 'file_type' : files_list_pstl}
dcom                         = {'name' : 'Sniper Scope',
                                 'offsets' : dcom_offsets,
                                 'file_type' : files_list_pstl}
talon_optic                  = {'name' : 'Sniper Scope x4',
                                 'offsets' : talon_optic_offsets,
                                 'file_type' : files_list_pstl}
suppressor                   = {'name' : 'Supressor',
                                 'offsets' : suppressors_offsets,
                                 'file_type' : files_list_pstl}
pro_screen                   = {'name' : 'Pro Screen',
                                 'offsets' : pro_screen_offsets,
                                 'file_type' : files_pro}
   
# MESSEGES

completion_message = "COMPLETE."
invalid_messege = 'Invalid selection, try again ->'

"""
Functions
"""
  
def read_dds(filename):
    """
    

    Parameters
    ----------
    filename : String
        path to the file.

    Returns
    -------
    Memoryview
    memoryview of a DDS file (header removed).

    """
    with open(filename,'rb') as ddsfile:
        dds_data = memoryview(bytearray(ddsfile.read()))[header_length:]
    return dds_data

def write_starpak(starpak_data, start_index):
    """
    

    Parameters
    ----------
    starpak_data : Memoryview
        memoryview of a starpak file.

    Returns
    -------
    String
        completion messege.

    """
    with open(pc_stream,'r+b') as output:
        output.seek(start_index)
        output.write(starpak_data)
    


def main_function(lof, loo):
    """
    

    Parameters
    ----------
    lof : List
        list of DDS file names.
    loo : TYPE
        list of offsets for a specific item.

    Returns
    -------
    String
        completion messege.

    """
    if lof == []:
        print('Complete')
        sys.exit()
    elif lof[0] == 'not found':
        main_function(lof[1:], loo[1:])
    else:
        write_starpak(read_dds(lof[0]), loo[0])
        main_function(lof[1:], loo[1:])

"""
Menu
"""

def clear(): os.system('cls')

def confirm_selection(selected):
    """
    

    Parameters
    ----------
    selected : String
        name of item DDS files will modify.

    Returns
    -------
    None.

    """
    print("You selected " + selected['name'])
    print("")
    print("DDS_2048 files found:")
    if not dds_2048_col == []:
        print("col - " + str(dds_2048_col)[2:-2])
    if not dds_2048_nml == []:
        print("nml - " + str(dds_2048_nml)[2:-2])
    if not dds_2048_gls == []:
        print("gls - " + str(dds_2048_gls)[2:-2])
    if not dds_2048_spc == []:
        print("spc - " + str(dds_2048_spc)[2:-2])
    if not dds_2048_ilm == []:
        print("ilm - " + str(dds_2048_ilm)[2:-2])        
    if not dds_2048_ao  == []:
        print("ao - " + str(dds_2048_ao)[2:-2])
    if not dds_2048_cav == []:
        print("cav - " + str(dds_2048_cav)[2:-2])        
    print("")
    print("DDS_1024 files found:")
    if not dds_1024_col == []:
        print("col - " + str(dds_1024_col)[2:-2])
    if not dds_1024_nml == []:
        print("nml - " + str(dds_1024_nml)[2:-2])
    if not dds_1024_gls == []:
        print("gls - " + str(dds_1024_gls)[2:-2])
    if not dds_1024_spc == []:
        print("spc - " + str(dds_1024_spc)[2:-2])
    if not dds_1024_ilm == []:
        print("ilm - " + str(dds_1024_ilm)[2:-2])       
    if not dds_1024_ao  == []:
        print("ao - " + str(dds_1024_ao)[2:-2])
    if not dds_1024_cav == []:
        print("cav - " + str(dds_1024_cav)[2:-2])        
    print("")
    print("DDS_512 files found:")
    if not dds_512_col == []:
        print("col - " + str(dds_512_col)[2:-2])
    if not dds_512_nml == []:
        print("nml - " + str(dds_512_nml)[2:-2])
    if not dds_512_gls == []:
        print("gls - " + str(dds_512_gls)[2:-2])
    if not dds_512_spc == []:
        print("spc - " + str(dds_512_spc)[2:-2])
    if not dds_512_ilm == []:
        print("ilm - " + str(dds_512_ilm)[2:-2])        
    if not dds_512_ao  == []:
        print("ao - " + str(dds_512_ao)[2:-2])
    if not dds_512_cav == []:
        print("cav - " + str(dds_512_cav)[2:-2])        
    print("")
    
    option = str(input("Proceed to apply DDS files [y/n] -> "))

    while option != 0:
        if option == 'y':
            clear()
            main_function(selected['file_type'], selected['offsets'])
        elif option == 'n':
            clear()
            menu("Enter a number to select -> ")
            option = 0
        else:
            clear()
            option = 0
            confirm_selection(selected)

def menu(message):
    """
    

    Parameters
    ----------
    message : String
        the enter message of the menu.

    Returns
    -------
    None.

    """
    print("|---------------------- |Assault| -----------------------|")
    print("  [01] " + rspn101['name']+"                [02] " +\
         m1a1_hemlok['name'])
    print("  [03] " + vinson['name']+"                [04] " +\
         g2['name'])
    print("|----------------------- |SMG| --------------------------|")
    print("  [05] " + alternator_smg['name']+"                   [06] " +\
         car101['name']) 
    print("  [07] " + r97['name']+"                         [08] " +\
         hemlok_smg['name'])
    print("|----------------------- |LMG| --------------------------|")
    print("  [09] " + hemlok_br['name']+"                     [10] " +\
         lstar['name'])
    print("  [11] " + lmg_hemlok['name'])
    print("|---------------------- |Sniper| ------------------------|")
    print("  [12] " + doubletake['name']+"                  [13] " +\
         at_rifle['name'])
    print("  [14] " + rspn101_dmr['name'])
    print("|-------------------- |Shotguns| ------------------------|")
    print("  [15] " + w1128['name']+"                   [16] " +\
         mastiff_stgn['name'])
    print("|-------------------- |Granadier| -----------------------|")
    print("  [17] " + pulse_lmg['name']+"                [18] " +\
         epg['name'])
    print("  [19] " + auto_rocket_launcher_ar['name']+"               [20] " +\
         softball_at['name'])
    print("|--------------------- |Pisotls| ------------------------|")
    print("  [21] " + pstl_sa3['name']+"                   [22] " +\
         p2011['name'])
    print("  [23] " + p2011_auto['name']+"                   [24] " +\
         p2011sp['name'])
    print("  [25] " + b3wing['name']+"                   [30] " +\
         wingman_elite['name'])
    print("|-------------------- |AntiTitan| -----------------------|")
    print("  [26] " + shoulder_rocket_sram['name']+"                       [27] " +\
         defender['name'])
    print("  [28] " + mgl_at['name']+"                          [29] " +\
         arc_launcher['name'])
    print("|--------------------- |Scopes| -------------------------|")
    print("  [31] " + hcog2['name']+"                         [32] " +\
         threat_w_scope['name'])
    print("  [33] " + aog_sight['name']+"                    [34] " +\
         holo_reflex_sight['name'])
    print("  [35] " + acgs_sight['name'])
    print("|------------------ |Sniper Scopes| ---------------------|")
    print("  [36] " + threat_scope_sniper['name']+"          [37] " +\
         dcom['name'])
    print("  [38] " + talon_optic['name'])
    print("|------------------- |Attachments| ----------------------|")
    print("  [39] " + suppressor['name']+"                    [40] " +\
         pro_screen['name'])
    print("[00] EXIT")
    
    try:
        option = int(input(message))
    except ValueError:
        clear()
        menu(invalid_messege)
        option = 0
    
    while option != 0:
        if option == 1:
            clear()
            confirm_selection(rspn101)
            option = 0
        elif option == 2:
            clear()
            confirm_selection(m1a1_hemlok)
            option = 0
        elif option == 3:
            clear()
            confirm_selection(vinson)
            option = 0
        elif option == 4:
            clear()
            confirm_selection(g2)
            option = 0
        elif option == 5:
            clear()
            confirm_selection(alternator_smg)
            option = 0
        elif option == 6:
            clear()
            confirm_selection(car101)
            option = 0
        elif option == 7:
            clear()
            confirm_selection(r97)
            option = 0
        elif option == 8:
            clear()
            confirm_selection(hemlok_smg)
            option = 0
        elif option == 9:
            clear()
            confirm_selection(hemlok_br)
            option = 0
        elif option == 10:
            clear()
            confirm_selection(lstar)
            option = 0
        elif option == 11:
            clear()
            confirm_selection(lmg_hemlok)
            option = 0
        elif option == 12:
            clear()
            confirm_selection(doubletake)
            option = 0
        elif option == 13:
            clear()
            confirm_selection(at_rifle)
            option = 0
        elif option == 14:
            clear()
            confirm_selection(rspn101_dmr)
            option = 0
        elif option == 15:
            clear()
            confirm_selection(w1128)
            option = 0
        elif option == 16:
            clear()
            confirm_selection(mastiff_stgn)
            option = 0
        elif option == 17:
            clear()
            confirm_selection(pulse_lmg)
            option = 0
        elif option == 18:
            clear()
            confirm_selection(epg)
            option = 0
        elif option == 19:
            clear()
            confirm_selection(auto_rocket_launcher_ar)
            option = 0
        elif option == 20:
            clear()
            confirm_selection(softball_at)
            option = 0
        elif option == 21:
            clear()
            confirm_selection(pstl_sa3)
            option = 0
        elif option == 22:
            clear()
            confirm_selection(p2011)
            option = 0
        elif option == 23:
            clear()
            confirm_selection(p2011_auto)
            option = 0
        elif option == 24:
            clear()
            confirm_selection(p2011sp)
            option = 0
        elif option == 25:
            clear()
            confirm_selection(b3wing)
            option = 0
        elif option == 26:
            clear()
            confirm_selection(shoulder_rocket_sram)
            option = 0
        elif option == 27:
            clear()
            confirm_selection(defender)
            option = 0
        elif option == 28:
            clear()
            confirm_selection(mgl_at)
            option = 0
        elif option == 29:
            clear()
            confirm_selection(arc_launcher)
            option = 0
        elif option == 30:
            clear()
            confirm_selection(wingman_elite)
            option = 0
        elif option == 31:
            clear()
            confirm_selection(hcog2)
            option = 0
        elif option == 32:
            clear()
            confirm_selection(threat_w_scope)
            option = 0
        elif option == 33:
            clear()
            confirm_selection(aog_sight)
            option = 0
        elif option == 34:
            clear()
            confirm_selection(holo_reflex_sight)
            option = 0
        elif option == 35:
            clear()
            confirm_selection(acgs_sight)
            option = 0
        elif option == 36:
            clear()
            confirm_selection(threat_scope_sniper)
            option = 0
        elif option == 37:
            clear()
            confirm_selection(dcom)
            option = 0
        elif option == 38:
            clear()
            confirm_selection(talon_optic)
            option = 0
        elif option == 39:
            clear()
            confirm_selection(suppressor)
            option = 0
        elif option == 40:
            clear()
            confirm_selection(pro_screen)
            option = 0
#        elif option == 37:
#            clear()
#            confirm_selection(hcog2)
#            option = 0
        else:
            clear()
            menu(invalid_messege)
            option = 0

menu("Enter a number to select -> ")