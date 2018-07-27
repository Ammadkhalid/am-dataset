from .dataset import dataset

def connect(url, **kwarg):

	return dataset.connect(url, **kwarg)