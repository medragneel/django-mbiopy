from django.shortcuts import redirect, render

from frontend.bpt import calculate_pms,find_mut
from .forms import Register
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from Bio.Seq import Seq
from Bio.SeqUtils import GC

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
    {"name": "Pdb Viewer", "url": "pdbViewer", "icon": "icons/pdb.svg"},
    {"name": "Phylogenie Viewer", "url": "phylo", "icon": "icons/phylo.svg",'coming': True},
]


    context = {"tools":tools}
    return render(r,'tools.html',context)
@login_required(login_url='login')
def length(r):
    context={}
    if r.method == 'POST':
        seq = r.POST.get('len')
        try:
            sq = Seq(seq)
        except Exception as e:
            messages.error(r,f'Invalid sequence: {e}')
            return render(r, 'length.html', context)
        length = len(sq)
        context['sq'] = sq
        context['length'] = length
    return render(r,'length.html',context)
@login_required(login_url='login')
def cmp(r):
   context={}
   if r.method == 'POST':
        seq = r.POST.get('dna_cmp')
        try:
            bio_seq = Seq(seq)

            reverse_complement = bio_seq.reverse_complement()

            context['f'] = seq
            context['cmp'] = reverse_complement

        except Exception as e:
            messages.error(r,f'Invalid sequence: {e}')
   return render(r,'cmp.html',context)


@login_required(login_url='login')
def gc(r):
    context={}
    if r.method == 'POST':
        seq = r.POST.get('gc_seq')
        try:

            gc_per = GC(seq)

            context['per'] = gc_per
            context['seq'] =seq

        except Exception as e:
            messages.error(r,f'Invalid sequence: {e}')

    return render(r,'gc.html',context)


@login_required(login_url='login')
def mutations_count(r):
    context = {}
    if r.method == 'POST':
        seq1 = r.POST.get('seq1')
        seq2 = r.POST.get('seq2')

        try:
            mutations = find_mut(seq1, seq2)
            mut_len = len(mutations)

            context['seq1'] = seq1
            context['seq2'] = seq2
            context['mc'] = mutations
            context['l'] = mut_len

        except ValueError as e:
            messages.error(r,e)
    return render(r,"mutation.html",context)


@login_required(login_url='login')
def protein_mass(r):
    context={}
    if r.method == 'POST':
        protein_seq = r.POST.get('pmass')

        try:
            mass = calculate_pms(protein_seq)

            context['pm'] = mass

        except Exception as e:
            messages.error(r,f"Invalid Sequence {e}")

    return render(r,'pmass.html',context)

@login_required(login_url='login')
def dnaTorna(r):
    context = {}
    if r.method == 'POST':
        dna_seq = r.POST.get('dna')

        try:
            bio_seq = Seq(dna_seq)

            rna_seq = bio_seq.transcribe()

            context['rna'] = rna_seq
            context['sq'] = bio_seq

        except Exception as e:
            messages.error(r,e)

    return render(r, 'rna.html', context)


@login_required(login_url='login')
def rnaToprotein(r):
    context={}
    if r.method == 'POST':
        dna_seq = r.POST.get('rna_seq')

        try:
            bio_seq = Seq(dna_seq)

            protein_seq = bio_seq.translate()

            context['psq'] = dna_seq
            context['pep'] = protein_seq

        except Exception as e:
            messages.error(r,f'Invalid Sequence ,{e}')
    return render(r,'proteinSeq.html',context)


@login_required(login_url='login')
def pdbViewer(r):
    context={}
    return render(r,'pdb-viewer.html',context)


