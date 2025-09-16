import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Definição dos eventos
A = {x for x in range(1, 7) if x % 2 == 0}  # {2, 4, 6}
B = {x for x in range(1, 7) if x > 4}       # {5, 6}

# Criar o diagrama de Venn
venn = venn2([A, B], set_labels=('A (Par)', 'B (>4)'))

# Adicionar os números nas regiões manualmente
# Subconjunto apenas de A (A - B)
venn.get_label_by_id('10').set_text('\n'.join(str(x) for x in A - B))

# Subconjunto apenas de B (B - A)
venn.get_label_by_id('01').set_text('\n'.join(str(x) for x in B - A))

# Interseção (A ∩ B)
venn.get_label_by_id('11').set_text('\n'.join(str(x) for x in A & B))

plt.title("Regra da Adição - Mostrando Elementos de A, B e A∩B")
plt.show()