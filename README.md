# MP4
 

Both models have similar accuracy and performance metrics.

- **Decision Tree Classifier:**
- Higher precision for predicting attrition (1), but lower recall.
- Better at correctly identifying non-attrition cases (0).
- Good overall accuracy.

- **Naïve Bayes Classifier:**
- Slightly better recall for predicting attrition (1), but lower precision.
- Better at correctly identifying attrition cases.
- Good overall accuracy.

- Naïve Bayes is slightly better


- **Clusters**
- Optimal number of clusters: 2
- Silhouette Score: 0.5402

- number of employees in claster 0: 1171
- number of employees in claster 1: 297

- **Cluster 0:**
- MonthlyIncome: $4,667.23 (approximately)
- Age: 34.11 years (approximately)
- TotalWorkingYears: 8.21 years (approximately)

- **Cluster 1:**
- MonthlyIncome: $13,753.04 (approximately)
- Age: 48.05 years (approximately)
- TotalWorkingYears: 23.41 years (approximately)
<br>
<br>

## Which machine learning methods did you choose to apply in the application?
We used decision tree classifier.

## Which are the most decisive factors for quitting a job?
The most deciding factors for quitting the job seems to be 
Overtime work, Marital status, TotalWorkingYears, JobLevel and MonthlyIncome, showcased by the correlation matrix.

## Which work positions and departments are in higher risk of losing employees?
The Sales department seems to be the department with highest risk of losing employees, with the Sale Representative Job role being the highest risk.

## Are employees of different gender paid equally in all departments?
It seems to very equal across the board. The differences seem very small and in some of the jobs the women have higher average, while in others the men have higher average. Both by small margins.

## Do the family status and the distance from work influence the work-life balance?
They do not seem to show a strong corrolation no.
DistanceFromHome vs WorkLifeBalance corrolation coefficient is -0.026556, indicating a weak negative relationship.

As for marital status:
Divorced correlation coefficient is -0.009080, showing a very weak negative relationship with worklifebalance.  <br>
Married correlation coefficient is -0.006388, again showing a very weak negative relationship with worklifebalance.  <br>
Single correlation coefficient is 0.014921, this time showing a very weak positive relationship with worklifebalance.  

This all in all seems to indicate there doesn't seem to be a strong correlation between either marital status or distance from work.

## Does education make people happy (satisfied from the work)?
Education and JobSatisfaction seems to be similar across the board with every education level having JobSatisfaction 3 or 4 being the highest value. However, it should be noted that in Education level 5, JobSatisfaction being 1 is nearly as high as 3 and 4.
To answer the question bluntly: No, higher education does not indicate to make people happy in this case.

## Which were the challenges in the project development?
Mainly Streamlit. It was really hard to figure out how to make it work and it was running veeeeery slowly, so testing the inbuilt user input stuff took incredibly long time. 



P.S. There's additional info, pictures, prediction model, etc in the Streamlit.
