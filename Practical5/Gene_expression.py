#1

import matplotlib.pyplot as plt
import numpy as np

#create dictionary and add a gene
gene_expression = { 'TP53' : 12.4 ,
                    'EGFR' : 15.1 ,
                    'BRCA1' : 8.2 , 
                    'PTEN' : 5.3 , 
                    'ESR1' : 10.7 }
print( "initial gene expression dictionary: " )
print( gene_expression )
gene_expression ['MYC'] = 11.6
print( "final gene expression dictionary: " )
print( gene_expression )

#bar chart
bars = plt.bar ( gene_expression.keys(), gene_expression.values(), width = 0.5 )
plt.title("Gene Expression Levels")
plt.xlabel("Genes")
plt.ylabel("Expression Level")
plt.yticks(np.arange(0, 21, 2))

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.1f}",
        ha='center',
        va='bottom'
    )
plt.grid(axis='y', linestyle='--', alpha=0.5)

#expression value
#the variable genetype is the gene of interest
gene_name = "TP53"
if gene_name in gene_expression:
    print(f"Expression value of {gene_name}: {gene_expression[gene_name]}")
else:
    print(f"Error: {gene_name} is not in the dictionary.")

#calcualte average gene expression
average_expression = sum( gene_expression.values () ) / len ( gene_expression )
print( f"Average gene expression level: {average_expression:.2f}" )

plt.tight_layout()
plt.show()