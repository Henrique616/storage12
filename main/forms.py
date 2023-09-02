class AlunoForm(forms.ModelForm):

#mascara do telefone(funciona com JS.)
    telefone = forms.CharField(widget=forms.TextInput(attrs={'minlength':'15', 'maxlength':'15','onkeyup':'handlePhone(event)'}))

#calendario no input
    data_nascimento = forms.DateField(
        widget= forms.Textinput(
        attrs= {'type': 'data'}    
        )
    )
    class Meta:
        model = Aluno 
        field = ['nome', 'telefone','email','data_nascimento','description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefone'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['data_nascimento'].widget.attrs.update({'class':'form-control'})
        self.field['description'].widget.attrs.update({'class':'form-control'})
