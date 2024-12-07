from django import forms
from articles.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean_title(self):
        title = self.cleaned_data.get('title')
        qs = Article.objects.filter(title__iexact=title)
        if qs.exists():
            raise forms.ValidationError(f"An article with the title '{title.lower()}' already exists.")
        return title
    
    def clean(self):
        # this is tutorial example:
        data = self.cleaned_data
        #title = data.get('title')
        #qs = Article.objects.filter(title__iexact=title)
        #if qs.exists():
        #    self.add_error('title',f"An article with the title '{title.lower()}' already exists.")
        return data
        
        
        # this is chatgpt example:
        # data = super().clean()  # Ensure field-level validation runs first
        #title = data.get('title')  # Safely get the title field
        #if title:
        #    # Check for similar titles
        #    qs = Article.objects.filter(title__icontains=title)
        #    if qs.exists():
        #        raise forms.ValidationError(f"An article with the title '{title.lower()}' already exists.")
        #return data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean_title(self):
        cleaned_data = self.cleaned_data # a dictionary
        print(cleaned_data)
        title = cleaned_data.get('title')
        if 'another' in title.lower():
            raise forms.ValidationError('another what?')
        print(title)
        return title
    
    def clean(self):
        cleaned_data = self.cleaned_data
        print('all of the datas:', cleaned_data)
        return cleaned_data
    
class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=10, required=True)
    password = forms.CharField(label= 'Password', widget=forms.PasswordInput, required=True)
        
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data