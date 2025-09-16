import pytest
from authenticator import Authenticator

#register() ユーザーが正しく登録されるか
def test_register():
    auth = Authenticator()
    auth.register("user1","pass1")
    assert auth.users["user1"] == "pass1"

#register() すでに存在するユーザー名で登録を試みた場合に、エラーメッセージが出力されるか
def test_register1():
    auth = Authenticator()
    auth.register("user1","pass1")
    with pytest.raises(ValueError,match="ユーザーは既に存在します"):
        auth.register("user1","pass1")

#login() 正しいユーザー名とパスワードでログインできるか
def test_login():
    auth = Authenticator()
    auth.register("user1","pass1")
    result = auth.login("user1","pass1")
    assert result == "ログイン成功"

#login() 誤ったパスワードでエラーが出るか
def test_login1():
    auth = Authenticator()
    auth.register("user1","pass1")
    with pytest.raises(ValueError,match="ユーザー名またはパスワードが正しくありません"):
        auth.login("user1","wrongpass")
