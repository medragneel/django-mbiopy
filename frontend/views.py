from email import message
from django.shortcuts import redirect, render
from .forms import Register
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home(r):
    context = {}
    return render(r,'index.html',context)

def signIn(r):
    if r.method == 'POST':
        username = r.POST.get('username')
        password = r.POST.get('password')
        user = authenticate(r,username=username ,password=password)
        print(user,password)
        if  user is not None:
            login(r,user)
            return redirect('home')
        else:
            messages.error(r,'username Or password Incorrect')


    context = {}
    return render(r,'login.html',context)

def register(r):
    form = Register()
    if r.method == 'POST':
        form = Register(r.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(r, f"User Created {user}")
        return redirect('login')
    else:
        form = Register()

    context = {'form': form}
    return render(r,'register.html',context)

def Logout(r):
    logout(r)
    return redirect('login')

@login_required(login_url='login')
def tools(r):
    tools = [
    {"name": "Sequence Length", "url": "seq_length", "icon": "icons/length.svg"},
    {"name": "Dna Complementary", "url": "dna_cmp", "icon": "icons/cmp.svg"},
    {"name": "GC% Calculator", "url": "gc", "icon": "icons/gc.svg"},
    {"name": "Count Point Mutations", "url": "mutations_count", "icon": "icons/mutation.svg"},
    {"name": "Calculating Protein Mass", "url": "pmass", "icon": "icons/proteins.svg"},
    {"name": "Rna Sequence", "url": "rna", "icon": "icons/dna.svg"},
    {"name": "From Rna to Protein", "url": "pseq", "icon": "icons/prot.svg"},
]


    context = {"tools":tools}
    return render(r,'tools.html',context)
