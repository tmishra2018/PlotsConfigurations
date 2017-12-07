
#RAndKff  = {}

RAndKff['DYmva0p8'] = {
                      'RFile'   : 'rootFile/plots_BG_DY_NOHR_MVA080.root' ,
                      'KffFile' : 'rootFile/plots_BG_DY_NOHR_MVA060.root' ,             
                      'Regions' : { 
                                    '2jVBFee' : {
                                               'kNum' : '2j_VBF_ee_in/events/histo_DY' ,
                                               'kDen' : '2j_VBF_uu_in/events/histo_DY' ,
                                               'RNum' : '2j_VBF_ee_out/events/histo_DY' ,
                                               'RDen' : '2j_VBF_ee_in/events/histo_DY' ,
                                             } ,
                                    '2jVBFmm' : {
                                               'kNum' : '2j_VBF_uu_in/events/histo_DY' ,
                                               'kDen' : '2j_VBF_ee_in/events/histo_DY' ,
                                               'RNum' : '2j_VBF_uu_out/events/histo_DY' ,
                                               'RDen' : '2j_VBF_uu_in/events/histo_DY' ,
                                             } ,
                                   } , 
                     }
 
#DYestim = {}

  
DYestim['hww2l2v_13TeV_2jee_vbf'] = {
                                   'rinout'  : 'DYmva0p8' ,
                                   'rsyst'   : 0.05 ,
                                   'ksyst'   : 0.01 ,
                                   'njet'    : '2jVBF' ,
                                   'flavour' : 'ee' ,
                                   'DYProc'  : 'DY' ,
                                   'SFin'    : 'hww2l2v_13TeV_DYin_2jee_vbf' ,
                                   'SFinDa'  : 'DATA',
                                   'SFinMC'  : ['VZ','Vg','WZgS_L','WZgS_H'],
                                   'DFin'    : 'hww2l2v_13TeV_DYin_2jdf' ,
                                   'DFinDa'  : 'DATA' ,
                                   'DFinMC'  : ['VZ','Vg','WZgS_L','WZgS_H'],
                                   'NPname'  : 'DYeenorm2jVBF' ,
                                   'AccNum'  : 'hww2l2v_13TeV_2jee_vbf_HAccNum/events/histo_DY',
                                   'AccDen'  : 'hww2l2v_13TeV_2jee_vbf_AccDen/events/histo_DY',
                                   'asyst'   : 0.06 ,
                                  }
 
DYestim['hww2l2v_13TeV_2jmm_vbf'] = {
                                   'rinout'  : 'DYmva0p8' ,
                                   'rsyst'   : 0.10 ,
                                   'ksyst'   : 0.05 ,
                                   'njet'    : '2jVBF'    ,
                                   'flavour' : 'mm' ,
                                   'DYProc'  : 'DY' ,
                                   'SFin'    : 'hww2l2v_13TeV_DYin_2jmm_vbf' ,
                                   'SFinDa'  : 'DATA' ,
                                   'SFinMC'  : ['VZ','Vg','WZgS_L','WZgS_H'],
                                   'DFin'    : 'hww2l2v_13TeV_DYin_2jdf' ,
                                   'DFinDa'  : 'DATA' ,
                                   'DFinMC'  : ['VZ','Vg','WZgS_L','WZgS_H'],
                                   'NPname'  : 'DYmmnorm2jVBF' ,
                                   'AccNum'  : 'hww2l2v_13TeV_2jmm_vbf_HAccNum/events/histo_DY',
                                   'AccDen'  : 'hww2l2v_13TeV_2jmm_vbf_AccDen/events/histo_DY',
                                   'asyst'   : 0.04 ,
                                  }

DYestim['hww2l2v_13TeV_WW_2jee_vbf'] = {
                                   'rinout'  : 'DYmva0p8' ,
                                   'njet'    : '2jVBF'    ,
                                   'flavour' : 'ee' ,
                                   'DYProc'  : 'DY' ,
                                   'SFin'    : 'hww2l2v_13TeV_DYin_2jee_vbf' ,
                                   'SFinDa'  : 'DATA',
                                   'SFinMC'  : ['VZ','Vg','WZgS_L','WZgS_H'],
                                   'DFin'    : 'hww2l2v_13TeV_DYin_2jdf' ,
                                   'DFinDa'  : 'DATA' ,
                                   'DFinMC'  : ['VZ','Vg','WZgS_L','WZgS_H'],
                                   'NPname'  : 'DYeenorm2jVBF' ,
                                   'AccNum'  : 'hww2l2v_13TeV_WW_2jee_vbf_WWAccNum/events/histo_DY',
                                   'AccDen'  : 'hww2l2v_13TeV_2jee_vbf_AccDen/events/histo_DY',
                                   'asyst'   : 0.03 ,
                                     }
 
DYestim['hww2l2v_13TeV_WW_2jmm_vbf'] = {
                                   'rinout'  : 'DYmva0p8' ,
                                   'njet'    : '2jVBF'    ,
                                   'flavour' : 'mm' ,
                                   'DYProc'  : 'DY' ,
                                   'SFin'    : 'hww2l2v_13TeV_DYin_2jmm_vbf' ,
                                   'SFinDa'  : 'DATA',
                                   'SFinMC'  : ['VZ','Vg','WZgS_L','WZgS_H'],
                                   'DFin'    : 'hww2l2v_13TeV_DYin_2jdf' ,
                                   'DFinDa'  : 'DATA' ,
                                   'DFinMC'  : ['VZ','Vg','WZgS_L','WZgS_H'],
                                   'NPname'  : 'DYmmnorm2jVBF' ,
                                   'AccNum'  : 'hww2l2v_13TeV_WW_2jmm_vbf_WWAccNum/events/histo_DY',
                                   'AccDen'  : 'hww2l2v_13TeV_2jmm_vbf_AccDen/events/histo_DY',
                                   'asyst'   : 0.02 ,
                                     }

