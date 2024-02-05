## I have these 2 images, can you make a flag out of them? **scrambled1.png** **scrambled2.png**

We need to combine the two picture somehow. Luckily, we can make a python script for this:

```python 

import numpy as np
from PIL import Image

# Prepare the images

img1 = Image.open("scrambled1.png");
img2 = Image.open("scrambled2.png");

# Combine the images

result = np.array(img1) + np.array(img2)

# Save the combined image

Image.fromarray(result).save('result.png')

```

picoCTF{71888***}
