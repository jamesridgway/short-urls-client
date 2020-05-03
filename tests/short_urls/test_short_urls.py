from assertpy import assert_that
from short_urls.short_urls import ShortUrls
import vcr

class TestShortUrls:
    @vcr.use_cassette('tests/fixtures/short_urls/list.yaml')
    def test_list(self):
        urls = ShortUrls('mydoma.in', 'letmein').list()
        assert_that(urls).is_equal_to({
            "https://jmsr.io/cwM1iQ": "https://www.james-ridgway.co.uk/blog/build-your-own-custom-short-url-generator-using-aws",
            "https://jmsr.io/dotfiles.sh": "https://raw.githubusercontent.com/jamesridgway/dotfiles/master/dotfiles.sh"
        })

    @vcr.use_cassette('tests/fixtures/short_urls/create.yaml')
    def test_create(self):
        short_urls = ShortUrls('mydoma.in', 'letmein')
        assert_that(short_urls.create('https://github.com/jamesridgway/short-urls-client')).is_equal_to('https://jmsr.io/aBUMYb')
    
    @vcr.use_cassette('tests/fixtures/short_urls/create_conflict.yaml')
    def test_create_conflict(self):
        short_urls = ShortUrls('mydoma.in', 'letmein')
        assert_that(short_urls.create)\
            .raises(ValueError)\
            .when_called_with('https://github.com/jamesridgway/short-urls-client')\
            .is_equal_to('This URL has already been created')

    @vcr.use_cassette('tests/fixtures/short_urls/create_custom.yaml')
    def test_create_custom(self):
        short_urls = ShortUrls('mydoma.in', 'letmein')
        assert_that(short_urls.create('https://github.com/jamesridgway/short-urls-client', 'client')).is_equal_to('https://jmsr.io/client')
    
    @vcr.use_cassette('tests/fixtures/short_urls/delete.yaml')
    def test_delete(self):
        short_urls = ShortUrls('mydoma.in', 'letmein')
        assert_that(short_urls.delete('https://github.com/jamesridgway/short-urls-client')).is_true()
    
    @vcr.use_cassette('tests/fixtures/short_urls/delete_fail.yaml')
    def test_delete_fail(self):
        short_urls = ShortUrls('mydoma.in', 'letmein')
        assert_that(short_urls.delete('https://github.com/jamesridgway/short-urls-client')).is_false()
