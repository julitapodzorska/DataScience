from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .predict import predict_image
from django.views import View


def handle_uploaded_file(f):
    with open('C:\\Users\\t659699\\Tools\\PortableGit\\repo\\Cat_Or_Not\\cats\\statics\\cat_dog.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def predict(request):
    form = FileUploadForm
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return redirect('/prediction')

    return render(request, 'upload.html', {'form': form})


def show_prediction(request):
    predicted = predict_image()
    context = {'predicted': predicted}
    return render(request, 'predicted.html', context)

