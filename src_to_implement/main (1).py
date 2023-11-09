from NumpyTests import TestGen
from generator import ImageGenerator

gen = ImageGenerator(
    label_path='./Labels.json',
    file_path='./exercise_data/',
    batch_size=20,
    image_size=(32, 32, 3),
    rotation=True,
    mirroring=True,
    shuffle=True,
)

gen.show()

test_gen = TestGen()
test_gen.setUp()
test_gen.testInit()
test_gen.testDuplicate()
test_gen.testResetIndex()
test_gen.testShuffle()
test_gen.testShuffleEpoch()
test_gen.testEpoch()
test_gen.testRotation()
test_gen.testMirroring()
test_gen.testResize()
test_gen.testLabels()
