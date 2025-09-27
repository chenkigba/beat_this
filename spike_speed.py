from tests.test_inference import test_File2Beat
import time

t1 = time.time()
test_File2Beat()
t2 = time.time()
print(t2 - t1)
