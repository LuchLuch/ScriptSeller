from django import forms

class ChatForm(forms.Form):
    your_name = forms.CharField()

# class UploadFileForm(forms.Form):
#     file = forms.ImageField()


# def handle_uploaded_file(f):
#     with open('/home/usr/PycharmProjects/NewProject/uploads/ss.img', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
