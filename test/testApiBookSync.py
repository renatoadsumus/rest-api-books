import tornado
from tornado.testing import *
from api import *

class MyTestCase(AsyncTestCase):
    def get_app(self):
        return make_app()

    def get_url(self, path):
        """Returns an absolute url for the given path on the test server."""
        return '%s://localhost:%s%s' % (self.get_protocol(),
                                        self.get_http_port(), path)

    @tornado.testing.gen_test
    def testAddBooksInCart(self):
        response = yield self.fetch('/v1/addbook?title="R"&author="Bill Ward"', method="GET")

        assert response.code == 200