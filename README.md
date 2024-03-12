# Joint Dimension Reduction Integration using AJIVE

Price, B.A., Marron, J.S., Mose, L.E. et al. Translating transcriptomic findings from cancer model systems to humans through joint dimension reduction. Commun Biol 6, 179 (2023). https://doi.org/10.1038/s42003-023-04529-3


Improving clinical translation of model system genomics through joint dimension reduction and horizontal data integration.

### Setup Environment

```bash
git clone https://github.com/baprice/AJIVE-jDR-Integration.git
conda env create --file environment.yaml
conda activate jDR_ajive
```
### Launch Jupyter and follow along the notebook to run AJIVE

Publically available data used in the manuscript and example notebooks can be found at <https://webshare.bioinf.unc.edu/public/baprice/AJIVE_jDR_Integration/>

```bash
cd notebooks/
jupyter notebook jDR_AJIVE_Template.ipynb
```

### For analyzing AJIVE results and calculating joint statistics, follow the analysis notebook

```bash
jupyter notebook jDR_Paper_Analysis.ipynb
```

![alt text](jDR_diagram.png)
