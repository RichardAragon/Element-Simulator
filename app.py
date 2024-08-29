import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

class Element:
    def __init__(self, atomic_number, symbol, electronegativity, valence_electrons):
        self.atomic_number = atomic_number
        self.symbol = symbol
        self.electronegativity = electronegativity
        self.valence_electrons = valence_electrons

    def __repr__(self):
        return f"Element({self.symbol})"

class Interaction:
    def __init__(self, elements, interaction_type):
        self.elements = elements
        self.interaction_type = interaction_type

    def __repr__(self):
        return f"Interaction({' + '.join([e.symbol for e in self.elements])})"

def simulate_interaction(interaction):
    # Use improved simulation with bond detection using swarm intelligence concepts
    diff = abs(interaction.elements[0].electronegativity - interaction.elements[1].electronegativity)
    avg_valence = (interaction.elements[0].valence_electrons + interaction.elements[1].valence_electrons) / 2

    # Determine the bond type and strength using Monte Carlo and Gaussian principles
    if diff > 1.7:  # Ionic bond
        bond_type = "ionic"
        strength = min(100, np.exp(-0.5 * (diff - 1.7) ** 2 / (avg_valence + 1e-5)) * 100)
    elif 0.4 <= diff <= 1.7:  # Polar covalent bond
        bond_type = "polar covalent"
        strength = min(100, np.exp(-0.5 * (diff - 1.0) ** 2 / (avg_valence + 1e-5)) * 100)
    else:  # Covalent bond
        bond_type = "covalent"
        strength = min(100, np.exp(-0.5 * (diff) ** 2 / (avg_valence + 1e-5)) * 100)

    return {
        "type": "bond",
        "bond_type": bond_type,
        "strength": strength,
        "description": f"{bond_type.capitalize()} bond strength: {strength:.1f}%"
    }

def find_stable_reactions(elements):
    stable_reactions = []

    # Generate all possible pairs of elements
    for e1, e2 in combinations(elements, 2):
        interaction = Interaction([e1, e2], "chemical_reaction")
        result = simulate_interaction(interaction)
        strength = result["strength"]
        if strength > 60:
            new_compound = f"{e1.symbol}{e2.symbol}"  # Simplified combination notation
            stable_reactions.append((e1.symbol, e2.symbol, strength, new_compound))

    # Print the stable reactions
    print("Stable Reactions (Strength > 60%):")
    for reaction in stable_reactions:
        print(f"Combination: {reaction[0]} + {reaction[1]}, Predicted Stability: {reaction[2]:.1f}%, Predicted Compound: {reaction[3]}")
    return stable_reactions

def visualize_interactions(elements, interactions):
    G = nx.Graph()
    for element in elements:
        G.add_node(element.symbol, atomic_number=element.atomic_number)

    for interaction in interactions:
        e1, e2 = interaction.elements
        result = simulate_interaction(interaction)
        G.add_edge(e1.symbol, e2.symbol, weight=result.get("strength", 50))

    pos = nx.spring_layout(G)
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue',
            node_size=500, font_size=10, font_weight='bold')

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.title("Element Interactions")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Example usage
elements = [
    Element(1, "H", 2.20, 1),    # Hydrogen
    Element(2, "He", 0.00, 2),   # Helium
    Element(3, "Li", 0.98, 1),   # Lithium
    Element(6, "C", 2.55, 4),    # Carbon
    Element(7, "N", 3.04, 5),    # Nitrogen
    Element(8, "O", 3.44, 6),    # Oxygen
    Element(9, "F", 3.98, 7),    # Fluorine
    Element(10, "Ne", 0.00, 8),  # Neon
    Element(11, "Na", 0.93, 1),  # Sodium
    Element(12, "Mg", 1.31, 2),  # Magnesium
    Element(13, "Al", 1.61, 3),  # Aluminum
    Element(14, "Si", 1.90, 4),  # Silicon
    Element(15, "P", 2.19, 5),   # Phosphorus
    Element(16, "S", 2.58, 6),   # Sulfur
    Element(17, "Cl", 3.16, 7),  # Chlorine
    Element(18, "Ar", 0.00, 8),  # Argon
    Element(19, "K", 0.82, 1),   # Potassium
    Element(20, "Ca", 1.00, 2),  # Calcium
    Element(26, "Fe", 1.83, 2),  # Iron
    Element(29, "Cu", 1.90, 1),  # Copper
    Element(30, "Zn", 1.65, 2),  # Zinc
    Element(35, "Br", 2.96, 7),  # Bromine
    Element(36, "Kr", 3.00, 8),  # Krypton
    Element(47, "Ag", 1.93, 1),  # Silver
    Element(53, "I", 2.66, 7),   # Iodine
    Element(54, "Xe", 2.60, 8),  # Xenon
    Element(79, "Au", 2.54, 1),  # Gold
    Element(80, "Hg", 2.00, 2),  # Mercury
    Element(82, "Pb", 2.33, 4)   # Lead
]

# Find and print stable reactions for all possible element combinations
stable_reactions = find_stable_reactions(elements)

# Visualize
interactions = [Interaction([e1, e2], "chemical_reaction") for e1, e2 in combinations(elements, 2)]
visualize_interactions(elements, interactions)
