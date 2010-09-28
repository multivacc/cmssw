# /dev/CMSSW_3_8_1/GRun/V37

import FWCore.ParameterSet.Config as cms

# dump of the Stream A Datasets defined in the HLT table

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetBTau_selector
streamA_datasetBTau_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetBTau_selector.l1tResults = cms.InputTag('')
streamA_datasetBTau_selector.throw      = cms.bool(False)
streamA_datasetBTau_selector.triggerConditions = cms.vstring('HLT_BTagMu_DiJet10U', 
    'HLT_BTagMu_DiJet20U', 
    'HLT_BTagMu_DiJet20U_Mu5', 
    'HLT_BTagMu_Jet10U', 
    'HLT_BTagMu_Jet20U', 
    'HLT_DoubleIsoTau15_OneLeg_Trk5', 
    'HLT_DoubleIsoTau15_Trk5', 
    'HLT_SingleIsoTau20_Trk15_MET20', 
    'HLT_SingleIsoTau20_Trk5_MET20', 
    'HLT_SingleIsoTau30_Trk5_L120or30', 
    'HLT_SingleIsoTau30_Trk5_MET20')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetCommissioning_selector
streamA_datasetCommissioning_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetCommissioning_selector.l1tResults = cms.InputTag('')
streamA_datasetCommissioning_selector.throw      = cms.bool(False)
streamA_datasetCommissioning_selector.triggerConditions = cms.vstring('HLT_Activity_CSC', 
    'HLT_Activity_DT', 
    'HLT_Activity_DT_Tuned', 
    'HLT_IsoTrackHB', 
    'HLT_IsoTrackHE', 
    'HLT_L1_BptxXOR_BscMinBiasOR', 
    'HLT_MultiVertex6', 
    'HLT_MultiVertex8_L1ETT60')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetCosmics_selector
streamA_datasetCosmics_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetCosmics_selector.l1tResults = cms.InputTag('')
streamA_datasetCosmics_selector.throw      = cms.bool(False)
streamA_datasetCosmics_selector.triggerConditions = cms.vstring('HLT_L1MuOpen_AntiBPTX', 
    'HLT_L1Tech_BSC_halo', 
    'HLT_L2Mu0_NoVertex', 
    'HLT_RPCBarrelCosmics', 
    'HLT_TrackerCosmics')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetEGMonitor_selector
streamA_datasetEGMonitor_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetEGMonitor_selector.l1tResults = cms.InputTag('')
streamA_datasetEGMonitor_selector.throw      = cms.bool(False)
streamA_datasetEGMonitor_selector.triggerConditions = cms.vstring('HLT_Activity_Ecal_SC17', 
    'HLT_Activity_Ecal_SC7', 
    'HLT_DoubleEle4_SW_eeRes_L1R', 
    'HLT_Ele10_SW_L1R', 
    'HLT_Ele12_SW_TightEleId_L1R', 
    'HLT_Ele17_SW_L1R', 
    'HLT_L1SingleEG2', 
    'HLT_L1SingleEG8', 
    'HLT_Photon10_Cleaned_L1R', 
    'HLT_Photon15_Cleaned_L1R', 
    'HLT_Photon20_NoHE_L1R', 
    'HLT_Photon50_NoHE_L1R')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetElectron_selector
streamA_datasetElectron_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetElectron_selector.l1tResults = cms.InputTag('')
streamA_datasetElectron_selector.throw      = cms.bool(False)
streamA_datasetElectron_selector.triggerConditions = cms.vstring('HLT_DoubleEle15_SW_L1R', 
    'HLT_Ele12_SW_TighterEleIdIsol_L1R', 
    'HLT_Ele17_SW_TightCaloEleId_SC8HE_L1R', 
    'HLT_Ele17_SW_TightEleId_L1R', 
    'HLT_Ele27_SW_TightCaloEleIdTrack_L1R')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetHcalHPDNoise_selector
streamA_datasetHcalHPDNoise_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetHcalHPDNoise_selector.l1tResults = cms.InputTag('')
streamA_datasetHcalHPDNoise_selector.throw      = cms.bool(False)
streamA_datasetHcalHPDNoise_selector.triggerConditions = cms.vstring('HLT_GlobalRunHPDNoise', 
    'HLT_TechTrigHCALNoise')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetHcalNZS_selector
streamA_datasetHcalNZS_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetHcalNZS_selector.l1tResults = cms.InputTag('')
streamA_datasetHcalNZS_selector.throw      = cms.bool(False)
streamA_datasetHcalNZS_selector.triggerConditions = cms.vstring('HLT_HcalNZS', 
    'HLT_HcalPhiSym')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetJet_selector
streamA_datasetJet_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetJet_selector.l1tResults = cms.InputTag('')
streamA_datasetJet_selector.throw      = cms.bool(False)
streamA_datasetJet_selector.triggerConditions = cms.vstring('HLT_DiJetAve100U', 
    'HLT_DiJetAve15U', 
    'HLT_DiJetAve30U', 
    'HLT_DiJetAve50U', 
    'HLT_DiJetAve70U', 
    'HLT_EcalOnly_SumEt160', 
    'HLT_ExclDiJet30U', 
    'HLT_HT140U', 
    'HLT_Jet100U', 
    'HLT_Jet140U', 
    'HLT_Jet15U', 
    'HLT_Jet15U_HcalNoiseFiltered', 
    'HLT_Jet30U', 
    'HLT_Jet50U', 
    'HLT_Jet70U', 
    'HLT_QuadJet20U', 
    'HLT_QuadJet25U')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetJetMETTauMonitor_selector
streamA_datasetJetMETTauMonitor_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetJetMETTauMonitor_selector.l1tResults = cms.InputTag('')
streamA_datasetJetMETTauMonitor_selector.throw      = cms.bool(False)
streamA_datasetJetMETTauMonitor_selector.triggerConditions = cms.vstring('HLT_HT100U', 
    'HLT_HT120U', 
    'HLT_HT50U', 
    'HLT_L1ETT100', 
    'HLT_L1Jet10U', 
    'HLT_L1Jet6U', 
    'HLT_L1MET20', 
    'HLT_QuadJet15U')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetMETFwd_selector
streamA_datasetMETFwd_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetMETFwd_selector.l1tResults = cms.InputTag('')
streamA_datasetMETFwd_selector.throw      = cms.bool(False)
streamA_datasetMETFwd_selector.triggerConditions = cms.vstring('HLT_DoubleJet15U_ForwardBackward', 
    'HLT_DoubleJet25U_ForwardBackward', 
    'HLT_Ele10_MET45', 
    'HLT_MET100', 
    'HLT_MET45', 
    'HLT_MET45_HT100U', 
    'HLT_MET65', 
    'HLT_MET80', 
    'HLT_Mu5_MET45')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetMinimumBias_selector
streamA_datasetMinimumBias_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetMinimumBias_selector.l1tResults = cms.InputTag('')
streamA_datasetMinimumBias_selector.throw      = cms.bool(False)
streamA_datasetMinimumBias_selector.triggerConditions = cms.vstring('HLT_L1Tech_BSC_HighMultiplicity', 
    'HLT_L1Tech_BSC_halo_forPhysicsBackground', 
    'HLT_L1Tech_BSC_minBias', 
    'HLT_L1Tech_BSC_minBias_OR', 
    'HLT_L1Tech_HCAL_HF', 
    'HLT_L1Tech_RPC_TTU_RBst1_collisions', 
    'HLT_L1_BPTX', 
    'HLT_L1_BPTX_MinusOnly', 
    'HLT_L1_BPTX_PlusOnly', 
    'HLT_MinBiasPixel_SingleTrack', 
    'HLT_PixelTracks_Multiplicity100', 
    'HLT_PixelTracks_Multiplicity70', 
    'HLT_PixelTracks_Multiplicity85', 
    'HLT_StoppedHSCP', 
    'HLT_ZeroBias', 
    'HLT_ZeroBiasPixel_SingleTrack')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetMu_selector
streamA_datasetMu_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetMu_selector.l1tResults = cms.InputTag('')
streamA_datasetMu_selector.throw      = cms.bool(False)
streamA_datasetMu_selector.triggerConditions = cms.vstring('HLT_DoubleMu3', 
    'HLT_DoubleMu5', 
    'HLT_IsoMu9', 
    'HLT_L2DoubleMu20_NoVertex', 
    'HLT_Mu11', 
    'HLT_Mu13', 
    'HLT_Mu15', 
    'HLT_Mu20_NoVertex', 
    'HLT_Mu5_Ele5', 
    'HLT_Mu5_Ele9', 
    'HLT_Mu5_HT50U', 
    'HLT_Mu5_Jet35U', 
    'HLT_Mu5_Photon9_Cleaned_L1R')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetMuMonitor_selector
streamA_datasetMuMonitor_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetMuMonitor_selector.l1tResults = cms.InputTag('')
streamA_datasetMuMonitor_selector.throw      = cms.bool(False)
streamA_datasetMuMonitor_selector.triggerConditions = cms.vstring('HLT_L1DoubleMuOpen', 
    'HLT_L1Mu20', 
    'HLT_L1Mu7', 
    'HLT_L1MuOpen', 
    'HLT_L1MuOpen_DT', 
    'HLT_L2DoubleMu0', 
    'HLT_L2Mu30', 
    'HLT_L2Mu7', 
    'HLT_Mu3', 
    'HLT_Mu5', 
    'HLT_Mu7', 
    'HLT_Mu9')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetMuOnia_selector
streamA_datasetMuOnia_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetMuOnia_selector.l1tResults = cms.InputTag('')
streamA_datasetMuOnia_selector.throw      = cms.bool(False)
streamA_datasetMuOnia_selector.triggerConditions = cms.vstring('HLT_DoubleMu0_Quarkonium', 
    'HLT_DoubleMu0_Quarkonium_LS', 
    'HLT_Mu0_TkMu0_OST_Jpsi', 
    'HLT_Mu0_TkMu0_OST_Jpsi_Tight', 
    'HLT_Mu3_TkMu0_OST_Jpsi', 
    'HLT_Mu3_Track3_Jpsi', 
    'HLT_Mu3_Track5_Jpsi', 
    'HLT_Mu5_L2Mu0', 
    'HLT_Mu5_TkMu0_OST_Jpsi', 
    'HLT_Mu5_Track0_Jpsi')

from HLTrigger.HLTfilters.triggerResultsFilter_cfi import triggerResultsFilter as streamA_datasetPhoton_selector
streamA_datasetPhoton_selector.hltResults = cms.InputTag('TriggerResults', '', 'HLT')
streamA_datasetPhoton_selector.l1tResults = cms.InputTag('')
streamA_datasetPhoton_selector.throw      = cms.bool(False)
streamA_datasetPhoton_selector.triggerConditions = cms.vstring('HLT_DoublePhoton17_L1R', 
    'HLT_DoublePhoton5_CEP_L1R', 
    'HLT_Photon17_SC17HE_L1R', 
    'HLT_Photon20_Cleaned_L1R', 
    'HLT_Photon30_Cleaned_L1R', 
    'HLT_Photon30_Isol_EBOnly_Cleaned_L1R', 
    'HLT_Photon35_Isol_Cleaned_L1R', 
    'HLT_Photon50_Cleaned_L1R', 
    'HLT_Photon70_NoHE_Cleaned_L1R')

