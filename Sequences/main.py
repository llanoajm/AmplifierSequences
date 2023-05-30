from nupack import Domain, TargetStrand, TargetComplex, TargetTube, SetSpec

hcj = Domain('N', name='hcj');
hck = Domain('N', name='hck');
hbr = Domain('N', name='hbr');
sb = Domain('N', name='sb');
sc = Domain('N', name='sc');
fc = Domain('N', name='fc');
fb = Domain('N', name='fb');
mb = Domain('N', name='mb');
mc = Domain('N', name='mc');

Cj = TargetStrand([sc, mc, fc, hcj], name='Cj');
BackCB = TargetStrand([fb,sc,mc], name = 'BackCB');
FluxBCj = TargetStrand([hcj, sb, mb], name='FluxBCj');
sweeplineReact = TargetStrand([~fc,~mc,~sc,~fb,~mb,~sb], name = 'sweeplineReact');
ReactIntCBCj = TargetComplex([Cj, sweeplineReact, FluxBCj ], "(((.+))).((+.))", name = 'ReactIntCBCj')
ReactCBCj = TargetComplex([BackCB, sweeplineReact, FluxBCj], "(((+.)))((+.))", name = 'ReactCBCj')
Br = TargetStrand([sb, mb, fb, hbr], name = 'Br');
WasteCjBr = TargetComplex([Cj, sweeplineReact, Br], "(((.+)))(((+))).", name = 'WasteCjBr');

# produce step species
Ck = TargetStrand([sc,mc,fc,hck], name = 'Ck');
sweeplineProduce = TargetStrand([~sb, ~hcj, ~fc, ~hck, ~fc], name = 'sweeplineProduce');
ProduceBCjCk = TargetComplex([Cj, sweeplineProduce, Ck], "..((+.))((+..))", name = 'ProduceBCjCk');
ProduceIntBCjCk = TargetComplex([FluxBCj, sweeplineProduce, Ck], "((.+)).((+..))", name = 'ProducetIntBCjCk');
HelperCCk = TargetStrand([fc,hck,fc], name = 'HelperCCk');
WasteBCjCk = TargetComplex([FluxBCj, sweeplineProduce, HelperCCk], "((.+))(((+)))", name = 'WasteBCjCk');

LeakedReactCBr = TargetComplex([BackCB, sweeplineReact, Br], "(((+.)))((+))..", name = 'LeakedReactCBr');
LeakedProduceBCjCk = TargetComplex([Cj, sweeplineProduce, HelperCCk], "...(+.)(((+)))", name = 'LeakedProduceBCjCk');
# LeakedReactCBCjProduceBCjCk = TargetComplex([BackCB, sweeplineReact, sweeplineProduce, Ck, FluxBCj], "(((+((+(+.)))).+)).((+..))", name = 'LeakedReactCBCjProduceBCjCk');

t1 = TargetTube(on_targets={WasteBCjCk: 1e-8, WasteCjBr: 1e-8, ReactCBCj: 1e-8, ReactIntCBCj: 1e-8, ProduceBCjCk: 1e-8, ProduceIntBCjCk: 1e-8}, name='t1',
    off_targets=SetSpec(max_size=3, include=[LeakedReactCBr, LeakedProduceBCjCk], exclude=[ReactCBCj, ReactIntCBCj, ProduceBCjCk, ProduceIntBCjCk]))

print("success")