# Programming and Scripting Project
by: Daniel Finnerty

## Introduction

This project is for demonstrating the ability to analyse the Fisher Iris data set using Python through both recently learned knowledge and research. In addition to the Python program (analysis.py), the Jupyter notebook outlines reasoning for certain coding, discussions of outputs, and references for any external material used.

## Tasks
- Week 1
  - Create Jupyter notebook.  
  - Research and review the Fisher Iris data set.  
  - Provide overview and findings.  

- Week 2
  - Download data set to repository.  
  - Create Python file.  
  - Write coding to log summary of each variable to text file.  

- Week 3
  - Create code for histogram generation.  
  - Capture outputs and record analysis of findings.  

- Week 4
  - Draft code for scatter plot creation.  
  - Review results and provide comments.  

- Week 5
  - Review full program, outputs and findings.  
  - Investigate if any further analysis is required.  
  - Creaate associated code.  

- Week 6
  - Final run through and adjustments as required. 
  - Update README file with instructions on how to run the Python file.   
  - <ins>**Submission - No later than May 12th.**</ins>  

## Data Set Research Summary
Through online reasearch of the Fisher iris data set, it can be clearly seen from the extensive availability of reviews and assessments that it is a regularly used source of data for people to practice their analystics knowledge and capabilities <sup>[1], [2]</sup>.

As documented, it is one of the most popular data sets used for learning and statistics. This can be attributed to several factors, but noteably 2 distinct aspects help make it so favourable. Its simplicity allows for new and less experienced researchers to easily understand the data presented to them, and apply analytical learnings with ease. In addition to this, it is also suggest that the versatility of the data set allows clear differences accross the different species to be discovered using various methods.

The data set itself consists of 150 samples, broken into equal quantities of 50 for each of the 3 species; Setosa, Versicolor, and Virginica. Each of the 150 samples contains 4 different measurements; sepal length, sepal width, petal length, and petal width, all of which are measured in centimetres.

There is no other data captured, but by running the Analysis program through the process documented below, clear analysis can be seen with discussion of such in the project_comments Jupyter notebook.

## Running analysis.py program
The analysis.py file needs to be ran, to create the summary file, and various plots which form parts of the data review, and is the basis for which the assessment is compiled in the project_comments notebook. To run the file:

1. Download anaconda (python) from:  
https://www.anaconda.com/download
    * When installing, ensure to check below 2 boxes:  
        i.  Add to PATH variable  
        ii. Make this version your default Python  
<br>
  
2. Download and install VS Code from:  
https://code.visualstudio.com/Download  
<br>

3. Go to Terminal in VSCode, and set where you want the repository to be stored.  
<br>

4. Once set, and still in terminal, enter the below code.

```
git clone https://github.com/danielfinnerty/principles_of_data_analytics.git
```
<br>

5. Now set new repository as directory  
<br>

6. Enter the below code to set the pull mode for repository  

```
git config pull.rebase false
```  
<br>

7. Pull all content from the repository

```
git pull
```  
<br>

8. Enter the below code to run the analysis.py program

```
python analysis.py
```


## Summary.txt file Review
After running the analysis.py program, a text file titled 'summary' is created. The difference with this file is that not only does it present the measurements again, this time they are in a string format rather than the original CSV file format, making them easier visually. In addition to this, headers for each column are now added, allowing clarity on which measurements are sepal length, sepal width, petal length, and petal width.

In addition to this, at the start of the file, a brief summary table is generated. In this, for each variable, the count is verified, matching that in the 'iris.names' file, along with confirmation of the mean, standard deviation, minimum measurement, maximum measurement, and the quartiles. While this information is already provided as part of the data set, capturing the same information in the 'summary' file, verifies that the data is being pulled in correctly for further assessment

Overview of mean and standard deviation? **

## References

[1] Geeks for Geeks. Iris data set. https://www.geeksforgeeks.org/iris-dataset/  
[2] Medium. Exploring the Iris dataset. https://eminebozkus.medium.com/exploring-the-iris-flower-dataset-4e000bcc266c#:~:text=It%20consists%20of%20150%20observations,multiple%20measurements%20in%20taxonomic%20problems.%E2%80%9D

# End