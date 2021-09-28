import os
from pathlib import Path
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from jive.AJIVE import AJIVE
from jive.PCA import PCA
import warnings
import time, datetime
from random import shuffle

warnings.filterwarnings(action='once')

def getVarianceExplained(original, joint, individual, label):
    from numpy.linalg import norm
    joint_var = norm(joint)**2/norm(original)**2
    individual_var = norm(individual)**2/norm(original)**2
    residual_var = 1-joint_var-individual_var
    return pd.DataFrame([residual_var, individual_var, joint_var], index=['Residual','Individual','Joint'], columns=[label])

def plotVarianceExplained(df, figsize=[10,6]):
    var_plot = plt.figure(figsize=figsize, facecolor='w')
    df.plot.bar(stacked=True, figsize=figsize, table=True)
    plt.xticks([])
    plt.tight_layout()
    return var_plot

parser = argparse.ArgumentParser(description='Run AJIVE')
parser.add_argument('-a', required=True, type=str, help='input matrix 1')
parser.add_argument('-ra', required=True, type=int, help='initial signal rank 1')
parser.add_argument('-rb', required=True, type=int, help='initial signal rank 2')
parser.add_argument('-n', required=True, type=str, help='name prefix')
parser.add_argument('-o', required=True, type=str, help='output files path')

args = parser.parse_args()
a_path = args.a
ra = args.ra
rb = args.rb
name_prefix = args.n
output_dir = Path(args.o)

#Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

#Read in files
a = pd.read_csv(a_path, index_col=0)
a = a.sample(frac=1)

#Randomly split in half
a1 = a.iloc[:a.shape[0]//2]
a2 = a.iloc[a.shape[0]//2:]

a = a1.T
b = a2.T

#Run AJIVE
jive_start = time.time()
ajive = AJIVE(init_signal_ranks={'A': ra, 'B': rb})
ajive.fit(blocks={'A': a, 'B': b})
jive_end = time.time()
jive_time = str(datetime.timedelta(seconds=jive_end-jive_start))
print('AJIVE time: ' + jive_time)

#Diagnostic Plot
sns.set_context('notebook', font_scale=1)
diag_plot = plt.figure(0, figsize=[10,10])
ajive.plot_joint_diagnostic()
diag_plot.savefig(os.path.join(output_dir, name_prefix + '_diagnostic.png'))

#Save AJIVE matrices
a_joint_full = pd.DataFrame(ajive.blocks['A'].joint.full_, index=a.index, columns=a.columns)
a_individual_full = pd.DataFrame(ajive.blocks['A'].individual.full_, index=a.index, columns=a.columns)
b_joint_full = pd.DataFrame(ajive.blocks['B'].joint.full_, index=b.index, columns=b.columns)
b_individual_full = pd.DataFrame(ajive.blocks['B'].individual.full_, index=b.index, columns=b.columns)

#Variance Plot
plt_df = getVarianceExplained(a, a_joint_full, a_individual_full, 'A').join(getVarianceExplained(b, b_joint_full, b_individual_full, 'B')).T
                        
plt_df.to_csv(os.path.join(output_dir, name_prefix + '_var_explained.csv'))
