class Config:
    def __init__(self,
                 max_retries=3):
        """
        Initializes a new instance of the Config class.

        Args:
            max_retries (int): The maximum number of retries for a retryable HTTP operation (500) (default = 3)
        """
        self.max_retries = max_retries
