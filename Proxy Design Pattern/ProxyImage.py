from FetchImageFromS3 import FetchImageFromS3


class ProxyImage:

    def __init__(self, fetch_image):
        self.fetch_image: FetchImageFromS3 = fetch_image

    def get_image(self, bucket: str, name: str) -> str:
        """
        Handling extra changes on the default get image
        """
        try:
            img = self.fetch_image.get_image(bucket, name)
        except:
            img = 'Default Image 100x100'
        # If image is not proper pixels, converting into the right pixels
        if not img.endswith('135x135'):
            img = img[0:-8]
            img += ' 135x135'
        return img
