
class FetchImageFromS3:
    """
    Component for handling the images from S3
    """

    def get_image(self, bucket: str, name: str) -> str:
        """
        Will be fetching the AWS creds from environment variables
        """
        print('Fetching image from S3')
        # raise FileNotFoundError
        return 'S3 Image 140x140'
