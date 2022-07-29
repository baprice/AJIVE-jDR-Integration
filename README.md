# Joint Dimension Reduction Integration using AJIVE

Brandon A. Price, J.S. Marron, Lisle E. Mose, Charles M. Perou, Joel S. Parker. (2021). Translating transcriptomic findings from model systems to humans through joint dimension reduction. *Under Review*.

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
