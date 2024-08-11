from ProxyImage import ProxyImage
from FetchImageFromS3 import FetchImageFromS3

real_object = FetchImageFromS3()
proxy = ProxyImage(real_object)
img = proxy.get_image('Translations', 'Sprint 52')
print(img)
