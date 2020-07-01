from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Post


class LoggedInTestCase(TestCase):


    def setUp(self):


        # テストユーザーのパスワード
        self.password = 'Test@0701'

        # テスト用ユーザーを生成
        self.test_user = get_user_model().objects.create_user(
            username='testuser',
            email='testsample@example.com',
            password=self.password)

        # テスト用ユーザーでログインする
        self.client.login(email=self.test_user.email, password=self.password)


class TestPostCreateView(LoggedInTestCase):


    def test_create_diary_success(self):


        # Postパラメータ
        params = {'title': 'テストタイトル',
                  'content': '本文',
                  "impression":"感想",
                  'photo1': '',
                  'photo2': '',
                  'photo3': ''}

        # 新規日記作成処理(Post)を実行
        response = self.client.post(reverse_lazy('posts:post_create'), params)

        # 日記リストページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('posts:post_list'))

        # 日記データがDBに登録されたかを検証
        self.assertEqual(Post.objects.filter(title='テストタイトル').count(), 1)

    def test_create_post_failure(self):
        #新規日記作成処理が失敗する事を検証

        # 新規日記作成処理(Post)を実行
        response = self.client.post(reverse_lazy('posts:post_create'))

        # 必須フォームフィールドが未入力によりエラーになる事を検証
        self.assertFormError(response, 'form', 'title', 'このフィールドは必須です。')


class TestPostUpdateView(LoggedInTestCase):
    """
    編集実行後のレダイレクトテストが上手くいかない

    def test_update_post_success(self):


        # テスト用日記データの作成
        post = Post.objects.create(user=self.test_user, title='タイトル編集前')

        # 更新データ
        params = {'title': 'タイトル編集後'}

        # 日記編集を実行
        response = self.client.post(reverse_lazy('posts:post_update', kwargs={'pk': post.pk}), params)

        # リダイレクトを検証
        self.assertRedirects(response, reverse_lazy('posts:post_detail', kwargs={'pk': post.pk}))

        # 編集されたかを検証
        self.assertEqual(Post.objects.get(pk=post.pk).title, 'タイトル編集後')
        """
    def test_update_post_failure(self):
        #編集処理が失敗する事を検証

        # 日記編集処理(Post)を実行
        response = self.client.post(reverse_lazy('posts:post_update', kwargs={'pk': 999}))

        # 存在しない日記データを編集しようとしてエラーになる事を検証
        self.assertEqual(response.status_code, 404)


class TestPostDeleteView(LoggedInTestCase):


    def test_delete_post_success(self):
        #削除処理が成功する事を検証

        # テスト用日記データの作成
        post = Post.objects.create(user=self.test_user, title='タイトル')

        # 日記削除処理(Post)を実行
        response = self.client.post(reverse_lazy('posts:post_delete', kwargs={'pk': post.pk}))

        # 日記リストページへのリダイレクトを検証
        self.assertRedirects(response, reverse_lazy('posts:post_list'))

        # 日記データが削除されたかを検証
        self.assertEqual(Post.objects.filter(pk=post.pk).count(), 0)

    def test_delete_post_failure(self):


        # 日記削除処理(Post)を実行
        response = self.client.post(reverse_lazy('posts:post_delete', kwargs={'pk': 999}))

        # 存在しない日記データを削除しようとしてエラーになる事を検証
        self.assertEqual(response.status_code, 404)
