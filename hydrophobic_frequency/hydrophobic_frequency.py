from bokeh.plotting import figure, output_notebook, show
from bokeh.charts import Bar, output_file, show
from bokeh.charts.attributes import cat
from numpy import cos, linspace
from collections import Counter,OrderedDict

import pandas as pd
import os
#x_file = open(direct+"/5_1.txt", "r")
# f=open(os.path.join(sub_dir,file))
#------------------------------------
#Store in secondary structures in a counter list
#------------------------------------

"""Dictionary to store the amino acids and their corresponding van der Walls volume"""
vdw_volume={}
vdw_volume['A']=67
vdw_volume['R']=148
vdw_volume['N']=96
vdw_volume['D']=91
vdw_volume['C']=86
vdw_volume['c']=86
vdw_volume['Q']=114
vdw_volume['E']=109
vdw_volume['G']=48
vdw_volume['H']=118
vdw_volume['I']=124
vdw_volume['L']=124
vdw_volume['K']=135
vdw_volume['M']=124
vdw_volume['F']=135
vdw_volume['P']=90
vdw_volume['S']=73
vdw_volume['T']=93
vdw_volume['W']=163
vdw_volume['Y']=141
vdw_volume['V']=105

vdw_volume_list=['67','148','96','91','86','86','114','109','48','118','124','124','135','124','135','90','73','93','163','141','105']

vdw_volume_list=sorted(vdw_volume_list, key=lambda x: float(x))
print vdw_volume_list
before_residue_list=[]
after_residue_list=[]
get=open('./../'+'angles_secondary_structure.txt','r')
for line in get:
	line=line.strip('\n')
	lines=line.split(',')
	cys1_ss=lines[-2:]
	cys2_ss=lines[-1:]+ lines[-2:-1]
	cys1_ss=",".join(cys1_ss)
	# cys1_ss=cys1_ss.strip('\n')


	cys2_ss=",".join(cys2_ss)
	# cys2_ss=cys2_ss.strip('\n')


	#------------------------------------#------------------------------------
	#Calculating the VDW volume of neighbouring amino acids
	#------------------------------------#---------------------------------
	"""Defining the neighbouring amino acids of the two Cys residues of a disulfide bond"""
	neighbouring_aminoacids1=[lines[37]] + [lines[47]] 
	neighbouring_aminoacids2=[lines[57]] + [lines[67].strip('\n')]
	#Van der walls volumes for residues before first Cys
	cys1_before=[(vdw_volume[neighbouring_aminoacids1[0]])]
	cys1_before=str(cys1_before)
	cys1_after=[(vdw_volume[neighbouring_aminoacids1[1]])]
	cys1_after=str(cys1_after)
	#Van der walls volumes for residues before second Cys
	cys2_before=[(vdw_volume[neighbouring_aminoacids2[0]])]
	cys2_before=str(cys2_before)
	cys2_after=[(vdw_volume[neighbouring_aminoacids2[1]])]
	cys2_after=str(cys2_after)
	

	before_residue_list.append(cys1_before)
	before_residue_list.append(cys2_before)

	after_residue_list.append(cys1_after)
	after_residue_list.append(cys2_after)

total=len(before_residue_list)
counts_before=Counter(before_residue_list)
counts_after=Counter(after_residue_list)
print total 
for key, value in counts_before.items():
	counts_before[key] = float(value) / float(total)
	print key
for key, value in counts_after.items():
    counts_after[key] = float(value) / float(total)


y_list_before=[]
y_list_after=[]
for value in vdw_volume_list:
	y_list_before.append(float(counts_before[value]))
	print counts_before[value]
	y_list_after.append(counts_before[value])

print y_list_before
# print y_list_after
#print counts_before
#print counts_after
#df=pd.DataFrame(counts.items(), columns=['Secondary Structure', 'Frequency'])
#print df
#df = df[['Frequency','Secondary Structure']]
#print df
#df=df.sort(['Frequency','Secondary Structure'], ascending=False)
##df=df.sort(inplace=True)
#print df
##------------------------------------
##Making x,y list
##------------------------------------
#x=[]
#y=[]
#print ''
#i=1
#for key in counts:
#	
#	x.append(i)
#	frequency=float(counts[key])/float(total)
#	y.append(frequency)
#	i=i+1
#
#print x
#y=sorted(y, key=float, reverse=True)
#
#
##x = linspace(-6, 6, 100)
##y = cos(x)
##p = figure(width=500, height=500,background_fill_color='lightgrey')
##p.line(x, y, color="blue", alpha=0.5,line_width=2,)
##p.square(x, y, color="blue", alpha=1,)
#
##------------------------------------
## Bar graph
##------------------------------------
#p = Bar(df,values='Frequency',label=cat(columns='Secondary Structure',sort=False),legend=None,color='blue',ylabel='Frequency (%)')
#p.xaxis.major_label_text_font_size='12pt'
#p.yaxis.major_label_text_font_size='12pt'
#p.yaxis.axis_label_text_font_size='13pt'
#p.xaxis.axis_label_text_font_size='13pt'
#show(p)#