# 2018 MMLA ANALYSIS
#### Karina Huang

This folder presents analyses of the MMLA study using EDA, JVA and Kinect data. A demo of the study can be found at this [GitHub page](https://kareenaaahuang.github.io/IS2018_demo/).Please follow the directory structure for navigation:

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


### img

Saved figures for paper.

### src

1. `CombineData.ipynb`: notebook used to combine clustering datasets.

2. `cluster.py`: module used to perform clustering and correlation. Please see comments in the py file for interpretation.
