import numpy as np
import matplotlib.pyplot as plt
import curvelops as cl

# Random test image
x = np.random.randn(100, 50)

# Curvelet transform
FDCT = cl.FDCT2D(dims=x.shape)
c = FDCT @ x
xinv = FDCT.H @ c

# Take real part (or abs() for magnitude)
xinv_real = np.real(xinv)

# Plot
plt.figure(figsize=(10,4))
plt.subplot(1,2,1)
plt.imshow(x, cmap='gray')
plt.title('Original')
plt.colorbar()

plt.subplot(1,2,2)
plt.imshow(xinv_real, cmap='gray')
plt.title('Reconstructed (real part)')
plt.colorbar()
plt.tight_layout()
plt.show()
