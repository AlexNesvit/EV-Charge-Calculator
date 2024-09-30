import tkinter as tk
from tkinter import ttk


def calculer_cout():
    a = 0.2068  # Coût par kWh pendant les heures creuses
    b = 3  # Puissance de l'appareil fixée à 3 kW
    c = float(duree_entry.get())  # Durée d'une charge en heures
    g = float(charges_par_mois_entry.get())  # Nombre de charges par mois

    d = b * c  # kWh consommé par charge
    e = a * d  # Coût en euros par charge
    f = g * e  # Coût total par mois

    # Mise à jour des labels pour afficher les résultats
    resultat_kwh.config(text=f"kWh par charge: {d:.2f} kWt")
    cout_par_charge_label.config(text=f"Coût par charge: {e:.2f} €")
    cout_par_mois_label.config(text=f"Coût par mois: {f:.2f} €")


# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculateur de coût électrique")

# Création et positionnement des widgets

duree_label = ttk.Label(root, text="Durée d'une charge en heures:")
duree_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
duree_entry = ttk.Entry(root)
duree_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

charges_par_mois_label = ttk.Label(root, text="Nombre de charges par mois:")
charges_par_mois_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
charges_par_mois_entry = ttk.Entry(root)
charges_par_mois_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

calculer_button = ttk.Button(root, text="Calculer", command=calculer_cout)
calculer_button.grid(column=0, row=2, columnspan=2, pady=10)

resultat_kwh = ttk.Label(root, text="kWh par charge: ")
resultat_kwh.grid(column=0, row=3, columnspan=2)

cout_par_charge_label = ttk.Label(root, text="Coût par charge: ")
cout_par_charge_label.grid(column=0, row=4, columnspan=2)

cout_par_mois_label = ttk.Label(root, text="Coût par mois: ")
cout_par_mois_label.grid(column=0, row=5, columnspan=2)

# Démarrage de la boucle principale de l'application
root.mainloop()
