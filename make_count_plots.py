import matplotlib.pyplot as plt
import seaborn as sns
import sys

'''
This script will make 6 plots for the pre- and post- smoothing kmer counts accross a read 
The plots will be save to a folder called "PLOTS". You should probably either change where the files are saved or make a directory called PLOTS
The counts files (from kmc or a similar tool) need to be saved in a folder called COUNTS. If you havent made those yet, you probably should. 
'''

#Read number that you are interested in
r=sys.argv[1]
sns.set_palette('plasma',2)
plt.rcParams["figure.figsize"] = (25,8)
cnts_old=[]
#The counts file before smoothing. 
count_f_old = "COUNTS/counts_pre_smooth_"+r+".txt"
with open(count_f_old) as f:
        line = f.readline()
        while line:
            cnts_old.append(int(line.strip()))
            line = f.readline()

#Make plots for the original counts 

pos_old = range(0,len(cnts_old))

splot = sns.scatterplot(x= pos_old, y=cnts_old, alpha=0.1)
#splot.set(yscale="log")
plt.ylabel('Coverage')
plt.xlabel('Position in Read')
#plt.yscale('symlog')
plt.yscale('log')
plt.ylim(1e-1, 1e6)
plt.savefig("PLOTS/read"+r+".counts.pre.log.png")
plt.close()

sns.scatterplot(x=pos_old, y=cnts_old, alpha=0.1)
plt.ylim(0,60)
plt.ylabel('Coverage')
plt.xlabel('Position in Read')
plt.savefig("PLOTS/read"+r+".counts.pre.png")
plt.close()

#Plot with the minimiap found reads 

cnts_new=[]
#The counts file post smoothing 
count_f_new = "COUNTS/counts_"+r+"_post_smooth.txt"
with open(count_f_new) as f:
        line = f.readline()
        while line:
            cnts_new.append(int(line.strip()))
            line = f.readline()
pos_new = range(0,len(cnts_new))
sns.scatterplot(x= pos_new, y=cnts_new, alpha=0.1)
plt.ylabel('Coverage')
plt.xlabel('Position in Read')
plt.yscale('log')
plt.ylim(1e-1, 1e6)
plt.savefig("PLOTS/read"+r+".counts.post.log.png")
plt.close()

sns.scatterplot(x=pos_new, y=cnts_new, alpha=0.1)
plt.ylim(0,60)
plt.ylabel('Coverage')
plt.xlabel('Position in Read')
plt.savefig("PLOTS/read"+r+".counts.post.png")
plt.close()

#Make combined plots, with both the pre and post smoothing counts 
sns.set_palette('plasma_r',2)
sns.scatterplot(x= pos_old, y=cnts_old, alpha=0.5, label='Pre')
sns.scatterplot(x= pos_new, y=cnts_new, alpha=0.5, label='Post')
plt.ylabel('Coverage')
plt.xlabel('Position in Read')
plt.yscale('log')
plt.ylim(1e-1, 1e6)
plt.legend(loc='upper right')
plt.savefig("PLOTS/read"+r+".counts.combined.log.png")
plt.close()

sns.scatterplot(x= pos_old, y=cnts_old, alpha=0.5, label='Pre')
sns.scatterplot(x=pos_new, y=cnts_new, alpha=0.5, label='Post')
plt.ylim(0,60)
plt.ylabel('Coverage')
plt.legend(loc='upper right')
plt.xlabel('Position in Read')
plt.savefig("PLOTS/read"+r+".counts.combined.png")
plt.close()
