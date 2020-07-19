from django.test import TestCase
from app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="My title", description="Sample desc", wiki="Post Body")
        self.assertEqual(post.title, "My title")
        self.assertEqual(post.description, "Sample desc")
        self.assertEqual(post.wiki, "Post Body")
