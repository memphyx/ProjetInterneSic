from django import forms



class EquipementForm(forms.ModelForm):
    date_abonmt_compt = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Numero du "
                                                                                              "compteur"}))
    date_dinstallation = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "placeholder": "Numero du "
                                                                                              "compteur"}))

    class Meta:
      #  model = Equipement
        fields = '__all__'
