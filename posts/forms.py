from django import forms
from django.core.mail import EmailMessage

from .models import Post

class InquiryForm(forms.Form):
    name = forms.CharField(label="お名前",max_length=30)
    email = forms.EmailField(label="メールアドレス")
    title = forms.CharField(label="タイトル", max_length=30)
    message = forms.CharField(label="メッセージ", widget=forms.Textarea)

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.fields["name"].widget.attrs["class"] = 'form-control-9'
        self.fields["name"].widget.attrs["placeholder"] = '名前を入力'

        self.fields["email"].widget.attrs["class"] = 'form-control-11'
        self.fields["email"].widget.attrs["placeholder"] = 'メールアドレスを入力'

        self.fields["title"].widget.attrs["class"] = 'form-control-11'
        self.fields["title"].widget.attrs["placeholder"] = 'タイトルを入力'

        self.fields["message"].widget.attrs["class"] = 'form-control-12'
        self.fields["message"].widget.attrs["placeholder"] = 'メッセージを入力'

    def send_email(self):
            name = self.cleaned_data["name"]
            email = self.cleaned_data["email"]
            title = self.cleaned_data["title"]
            message = self.cleaned_data["message"]

            subject = "お問い合わせ{}".format(title)
            message = "送信者:{0}\nメールアドレス:{1}\nメッセージ:{2}".format(name,email,message)

            from_email = "admin@example.com"
            to_list=[
                "test@example.com"
            ]
            cc_list=[
                email
            ]

            message = EmailMessage(subject=subject,body=message,from_email=from_email,
                                   to=to_list,cc=cc_list)
            message.send()

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'impression','photo1', 'photo2', 'photo3', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'