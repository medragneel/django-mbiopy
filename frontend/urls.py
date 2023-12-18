
from django.urls import  path
from . import views




urlpatterns = [
        path('',views.home,name="home"),
        path('login/',views.signIn,name="login"),
        path('logout/',views.Logout,name="logout"),
        path('register/',views.register,name="register"),
        path('tools/',views.tools,name="tools"),
        path('tools/seq_length',views.length,name="seq_length"),
        path('tools/dna_cmp/', views.cmp, name="dna_cmp"),
        path('tools/gc/', views.gc, name="gc"),
        path('tools/mutations_count/', views.mutations_count, name="mutations_count"),
        path('tools/pmass/', views.protein_mass, name="pmass"),
        path('tools/rna/', views.dnaTorna, name="rna"),
        path('tools/pseq/', views.rnaToprotein, name="pseq"),
        path('tools/pdbViewer/', views.pdbViewer, name="pdbViewer"),
]
