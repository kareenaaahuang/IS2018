# 2018 MMLA ANALYSIS
#### Karina Huang

This folder presents analyses of the MMLA study using EDA, JVA and Kinect data. Please follow the directory structure for navigation:

```
Analysis/
	analysis_clustering/
			   Correlation_Markov_Chain.ipynb
			   EDA_JVA_Kinect_HeadDiff.ipynb
			   EDA_JVA.ipynb
			   EDA_JVA_4_to_10_Clusters_Demo.ipynb
			   EDA_JVA_Kinect_MoveDiff.ipynb
			   EDA_JVA_Kinect_MoveDiff_5_to_10_Clusters_Demo.ipynb
			   EDA_JVA_Kinect_ShoulderDiff.ipynb
			   EDA_JVA_Kinect_all.ipynb
			   Multicollinearity_Check.ipynb
	analysis_exploratory/
			    EDA+JVA+MOT_Clustering_111518_Draft.ipynb
			    Mediation_103118.ipynb
			    Mediation_110718.ipynb
			    Regression_110318.ipynb
	data_master/
		   EDA_JVA_Kinect_MasterScaled.csv
		   EDA_JVA_MasterScaled.csv
		   sessions.csv
		   sumMovement.csv
	data_visualization/
			  ...csv files of clustering results
	img/
	   optimalK_eda_jva.png
	   optimalK_eda_jva_kinect.png
	src/
	   CombineData.ipynb
	   cluster.py
	visualizations/
		      EDA_JVA.ipynb
		      EDA_JVA_Kinect_HeadDiff.ipynb
		      EDA_JVA_Kinect_MoveDiff.ipynb
		      EDA_JVA_Kinect_ShoulderDiff.ipynb
	README.md
```

### analysis_clustering

Final analyses used for summarizing K-Means Clustering results. Please consult individual notebooks for details regarding analyses.

### analysis_exploratory

Exploratory analyes conducted for independent study.

### data_master

1. `EDA_JVA_Kinect_MasterScaled.csv`: scaled data used for clustering with EDA, JVA, and Kinect.

2. `EDA_JVA_MasterScaled.csv`: scaled data used for clustering with EDA and EDA.

3. `sessions.csv`: qualitative outcome measures by group.

4. `sumMovement.csv`: original data used for exploring combined Kinect movement measures; this is irrelevant to the final analysis.

### data_visualization

All csv files generated from clustering, saved for visualizations.

### img

Saved figures for paper.

### src

1. `CombineData.ipynb`: notebook used to combine clustering datasets.

2. `cluster.py`: module used to perform clustering and correlation. Please see comments in the py file for interpretation.
