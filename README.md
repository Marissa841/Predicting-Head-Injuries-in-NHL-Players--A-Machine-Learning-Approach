# Business Case

Head injuries and concussions have become a serious issue in professional sports, affecting the health of players and the winning potential of teams. The goal of this project is to predict which NHL players are more likely to suffer head injuries based on their past performance and other relevant information. This analysis is targeted towards NHL teams and team managers to help them take proactive measures to prevent head injuries and minimize the impact of such injuries on the team’s performance.

# Data:

The data used in this project is from the Eliteprospect_scraper package which contains data of NHL players and https://nhlinjuryviz.blogspot.com/2015/11/nhl-injury-database.html which I corowsnvert to a csv file to view injuries over the past 20 years. The final dataset contains over 18,000 rows.

# Methods:

The methods used for this project were based on the OSEMN method and iterative modeling. For processing the data I cleaned the data, changed datatypes to integers/floats and made new features. For the modeling portion, I used a function called model_helper to run through five machine learning modes: Logistic Regression, Decision Tree Classifier, Random Forest Classifer, Support Vector Machine (SVM), and Gradient boosting. 

# Conclusion:

From the above-mentioned methods, I was able to obtain an overall f1 score of 0.24 using the RandomForestClassifer.  In this case, the F1 score for the training data is 0.9836642372455391, which is high, while the F1 score for the testing data is 0.24079320113314448, which is a lot lower, but still the best F1 score.

Below is a confusion matrix that shows the performance of the model: 



# Future Work:



# For more information:

​​See the full analysis in the [Jupyter Notebook](https://github.com/Marissa841/phase_5_project/blob/main/main_notebook.ipynb) or review this [presentation](https://github.com/Marissa841/phase_4_project/blob/main/phase_4_project_nontechnical.pdf). For additional info, my email is Marissabush.02@gmail.com



# Repository structure:

+ data
+ img
+ main_notebook.ipynb
+ data_notebook.ypynb
+ df.csv
+ phase_5_project_nontechnical.pdf
+ model_helper.py