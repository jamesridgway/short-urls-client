from assertpy import assert_that
import tempfile
from short_urls.config import Config

class TestConfig:
    def test_set_and_get_credentials(self):
        test_directory = tempfile.mkdtemp()
        config = Config(test_directory)

        assert_that(config.get_credentials()).is_none()

        config.set_credentials('mydoma.in', 'letmein')
        
        assert_that(config.get_credentials()).is_equal_to({
            'domain': 'mydoma.in',
            'api_key': 'letmein'
        })
