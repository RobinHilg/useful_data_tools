from scipy import stats


#Check for normality of a dataset
def check_norm(data):
    test_stat, p_value=stats.shapiro(data)
    if p_value <0.05:
        print("Data isn't normally distributed according to the Shapiro-Wilk test.")
    else:
        print("Data is normally distributed according to the Shapiro-Wilk test.")  
    print("p value:%.4f" % p_value)

#Check for equal variances on two datasets
def check_variance(group1, group2):
    test_stat, p_value= stats.levene(group1,group2)
    print("p value:%.4f" % p_value)
    if p_value <0.05:
        print("The variances of the samples are different according to the Levene test.")
    else:
        print("The variances of the samples are same according to the Levene test.")
    print("p value:%.4f" % p_value)
        
