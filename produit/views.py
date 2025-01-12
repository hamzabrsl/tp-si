from django.shortcuts import get_object_or_404, redirect, render
from .models import Commande, product
from .forms import CommandeForm

def afficher_produits(request):
    produits=product.objects.all()
    return render(request, "index.html",{"products":produits})

def rechercher_produits(request):
    if request.method == "GET":
        query=request.GET.get('search')
        if query:
            produits=product.objects.filter(name__contains=query)
            return render(request,'search.html', {'products': produits })
        return render(request,'search.html')



def commander_prd(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            form = CommandeForm()
            mssg="commande envoyée, vous pouvez saisir une autre"
            # return redirect("listing") #redirection vers la page de l’url: listing
            return render(request,"commande.html",{"form":form,"message":mssg})
    else:
        form = CommandeForm() #créer une instance de formulaire vierge
        mssg ="veuillez remplir tous les champs!"
        return render(request,"commande.html",{"form":form,"message":mssg})
    
def afficher_cmd(request):
    cmds=Commande.objects.all()
    return render(request,"CmdList.html",{"commandes":cmds})    

def edit_cmd(request, pk):
    cmd=Commande.objects.get(id=pk) # récupérer l'instance de "commande" correspondante
    if request.method=='POST':
        form =CommandeForm(request.POST, instance=cmd)
        #create new order instance (commande) from post data. This instance will
        # replace an existing one in the database (the cmd instance).
        if form.is_valid():
            form.save()
            return redirect("CmdList") #rediriger vers l’url: CmdList.
    else:
        form=CommandeForm(instance=cmd) #fournir une instance pré-remplie de formulaire
        return render(request,'CmdEdit.html',{"form":form})
    
def delete_cmd(request, pk):
    # Récupérer l'instance de la commande
    cmd =Commande.objects.get(id=pk)

    if request.method == "POST":
        # Si l'utilisateur confirme, supprimer la commande
        cmd.delete()
        return redirect("CmdList")  # Rediriger vers la liste des commandes après suppression

    # Rendre une page de confirmation
    return render(request, 'CmdDelete.html', {"commande": cmd})    