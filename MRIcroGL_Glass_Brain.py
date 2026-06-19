# This script loads a transparent/glass brain template with optimal settings
# Open scripting in MRIcroGL and paste the commands below
# gl.overlayload() is for loading a mask with the glass brain, 
# 'corrp_tfce_neg' is my result file from the meta-analysis published in Dietze et al., 2023 [PMID: 36960197]
# This glass brain template was also used for the ENIGMA-BD study Dietze et al., 2025 [PMID: 39501059]

import gl
import sys
print(sys.version)
print(gl.version())
gl.resetdefaults()
gl.overlayload('corrp_tfce_neg')
gl.minmax(1, 4, 4)
gl.shadername('Shell')
gl.shaderadjust('boundThresh', 0.35)
gl.shaderadjust('edgeThresh', 0.85)
gl.shaderadjust('edgeBoundMix',0.05)
gl.shaderadjust('colorTemp', 0.8)
gl.backcolor(255, 255,255)
