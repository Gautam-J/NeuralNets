from django.views import generic
from django.shortcuts import render
from .models import IrisData

import joblib


class CreateIrisDataView(generic.CreateView):
    model = IrisData
    template_name = 'Iris\\create.html'

    fields = [
        'sepal_length',
        'sepal_width',
        'petal_length',
        'petal_width'
    ]

    def get(self, request, *args, **kwargs):
        print('Loading necessary files')
        global svc_model, encoder, scaler
        svc_model = joblib.load('Iris\\iris_model\\model.pkl')
        encoder = joblib.load('Iris\\iris_model\\encoder.pkl')
        scaler = joblib.load('Iris\\iris_model\\scaler.pkl')
        print('Files loaded')

        return super(CreateIrisDataView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            s_l = form.cleaned_data['sepal_length']
            s_w = form.cleaned_data['sepal_width']
            p_l = form.cleaned_data['petal_length']
            p_w = form.cleaned_data['petal_width']

            data = [[s_l, s_w, p_l, p_w]]
            data = scaler.transform(data)
            prediction = svc_model.predict(data)
            prediction = encoder.inverse_transform(prediction)[0]

            args = {'form': form, 'prediction': prediction}

            instance = form.save(commit=False)
            instance.prediction = prediction
            instance.save()

            return render(request, self.template_name, args)

        else:
            return self.form_invalid(form)
