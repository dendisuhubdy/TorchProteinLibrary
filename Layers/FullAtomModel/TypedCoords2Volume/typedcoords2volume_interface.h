void TypedCoords2Volume_forward(    THCudaDoubleTensor *input_coords,THCudaTensor *volume,THCudaIntTensor *num_atoms_of_type,THCudaIntTensor *offsets);
void TypedCoords2Volume_backward(   THCudaTensor *grad_volume,THCudaDoubleTensor *grad_coords,THCudaDoubleTensor *coords,THCudaIntTensor *num_atoms_of_type,THCudaIntTensor *offsets);