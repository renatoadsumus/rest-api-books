from tornado.httpclient import AsyncHTTPClient
from tornado.testing import AsyncHTTPTestCase

from api import *

class testApiBook(AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def get_url(self, path):
        """Returns an absolute url for the given path on the test server."""
        return '%s://localhost:%s%s' % (self.get_protocol(),
                                        self.get_http_port(), path)

    @tornado.testing.gen_test
    def testAddBooksInCart(self):
        headers = {
            "Content-Type": "<meta http-equiv=\"Content-type\" content=\"text/html; charset=utf-8\" />",
        }
        response = yield self.fetch('/v1/addbook?title="R"&author="Bill Ward"', headers=headers, method="GET")

        assert response.code == 200