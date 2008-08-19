import FWCore.ParameterSet.Config as cms

source = cms.Source("PythiaSource",
                    pythiaHepMCVerbosity = cms.untracked.bool(False),
                    pythiaPylistVerbosity = cms.untracked.int32(0),
                    
                    ParticleID = cms.untracked.int32(443),
                    DoubleParticle = cms.untracked.bool(False),
                    kinematicsFile = cms.untracked.string('HeavyIonsAnalysis/Configuration/data/jpsipbpb.root'),
                    
                    ptBinning = cms.untracked.int32(100000),
                    Ptmin = cms.untracked.double(0.0),
                    Ptmax = cms.untracked.double(100.0),
                    yBinning = cms.untracked.int32(500),
                    ymin = cms.untracked.double(-10.0),
                    ymax = cms.untracked.double(10.0),
                    
                    PythiaParameters = cms.PSet(parameterSets = cms.vstring('pythiaDefault','jpsiDecay'),
                                                pythiaDefault=cms.vstring('PMAS(5,1)=4.8 ! b quark mass',
                                                                          'PMAS(6,1)=172.3 ! t quark mass'),
                                                jpsiDecay = cms.vstring('BRAT(858) = 0 ! switch off',
                                                                        'BRAT(859) = 1 ! switch on',
                                                                        'BRAT(860) = 0 ! switch off',
                                                                        'MDME(858,1) = 0 ! switch off',
                                                                        'MDME(859,1) = 1 ! switch on',
                                                                        'MDME(860,1) = 0 ! switch off'),
                                                upsilonDecay = cms.vstring('BRAT(1034) = 0 ! switch off',
                                                                           'BRAT(1035) = 1 ! switch on',
                                                                           'BRAT(1036) = 0 ! switch off',
                                                                           'BRAT(1037) = 0 ! switch off',
                                                                           'BRAT(1038) = 0 ! switch off',
                                                                           'BRAT(1039) = 0 ! switch off',
                                                                           'BRAT(1040) = 0 ! switch off',
                                                                           'BRAT(1041) = 0 ! switch off',
                                                                           'BRAT(1042) = 0 ! switch off',
                                                                           'MDME(1034,1) = 0 ! switch off',
                                                                           'MDME(1035,1) = 1 ! switch on',
                                                                           'MDME(1036,1) = 0 ! switch off',
                                                                           'MDME(1037,1) = 0 ! switch off',
                                                                           'MDME(1038,1) = 0 ! switch off',
                                                                           'MDME(1039,1) = 0 ! switch off',
                                                                           'MDME(1040,1) = 0 ! switch off',
                                                                           'MDME(1041,1) = 0 ! switch off',
                                                                           'MDME(1042,1) = 0 ! switch off')
                                                )
                    )

                    




