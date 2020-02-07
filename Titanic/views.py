from django.views import generic
from django.shortcuts import render
from .models import TitanicData

import joblib
import numpy as np
import pandas as pd


class CreateTitanicDataView(generic.CreateView):
    model = TitanicData
    template_name = 'Titanic\\create.html'
    success_url = '/create'

    fields = [
        'passenger_class',
        'sex',
        'age',
        'siblings_or_spouse',
        'parents_or_children',
        'fare'
    ]

    def get(self, request, *args, **kwargs):
        print('Loading necessary files')
        global svc_model, encoder, scaler
        svc_model = joblib.load('Titanic\\titanic_model\\model.pkl')
        encoder = joblib.load('Titanic\\titanic_model\\encoder.pkl')
        scaler = joblib.load('Titanic\\titanic_model\\scaler.pkl')
        print('Files loaded')

        return super(CreateTitanicDataView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            p_class = form.cleaned_data['passenger_class']
            sex = form.cleaned_data['sex']
            age = form.cleaned_data['age']
            sibsp = form.cleaned_data['siblings_or_spouse']
            parch = form.cleaned_data['parents_or_children']
            fare = form.cleaned_data['fare']

            num_data = [age, sibsp, parch, fare]
            cat_data = [[p_class, sex]]

            df = pd.DataFrame(cat_data, columns=['pclass', 'sex'])
            cat_data = encoder.transform(df).toarray().reshape(-1,)
            data = np.hstack((num_data, cat_data)).reshape(1, -1)
            data = scaler.transform(data)
            pred = svc_model.predict(data)
            prediction = 'Not Survived' if pred[0] == 0 else 'Survived'

            args = {'form': form, 'prediction': prediction}

            instance = form.save(commit=False)
            instance.prediction = prediction
            instance.save()

            return render(request, self.template_name, args)

        else:
            return self.form_invalid(form)
