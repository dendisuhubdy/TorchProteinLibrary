import os
import torch
import glob
from torch.utils.ffi import create_extension

this_file = os.path.dirname(__file__)


here = os.path.normpath(os.path.dirname(__file__))
lib_dir = os.path.abspath(os.path.join(here, '../'))
sources = [ os.path.join(lib_dir,'Layers/PDB2Coords/pdb2coords_interface.cpp'),
			os.path.join(lib_dir,'Layers/Coords2Volume/coords2volume_interface.cpp')]
headers = [	os.path.join(lib_dir,'Layers/PDB2Coords/pdb2coords_interface.h'),
			os.path.join(lib_dir,'Layers/Coords2Volume/coords2volume_interface.h')]

include_dirs = [
	os.path.join(lib_dir, 'Math'),
]
library_dirs=[	os.path.join(lib_dir, 'build/Layers/PDB2Coords'),
				os.path.join(lib_dir, 'build/Layers/Coords2Volume'),
				os.path.join(lib_dir, 'build/Layers/Coords2Volume'),
				os.path.join(lib_dir, 'build/Math')]

defines = []
with_cuda = True

ffi = create_extension(
	'CppLayers',
	headers=headers,
	sources=sources,
	define_macros=defines,
	relative_to=__file__,
	with_cuda=with_cuda,
	include_dirs = include_dirs,
	extra_compile_args=["-fopenmp"],
	extra_link_args = [],
	libraries = [ "PROTEINLOADER", "COORDS2VOLUME", "COORDS2VOLUME_CU", "TH_MATH"],
    library_dirs = library_dirs
)

if __name__ == '__main__':
	ffi.build()
	import CppLayers
	print CppLayers.__dict__.keys()