#pip3 install matplotlib and
#use for data visulatization or creating chart graph

from matplotlib import pyplot as plt
import seaborn as sns


#use styles from seaborn
sns.set()

#data
ages=[10,20,30,40,50,60,70]
salaries=[3000,4000,500,600,7000,8000,9000]
#expensese=[1000,2000,3000,4000,5000,6000,7000]

#line chart
plt.plot(ages,salaries,color='green',label="salaries")
#plt.plot(ages,expensese,color="red",label="expensese")

#add titles
plt.title('ages vs salary')
plt.xlabel('age')
plt.ylabel('salary')

#fit the graph
plt.tight_layout()

plt.show()


def barchart_of_ages_salaries():
    left_edges=ages
    height=salaries
    plt.bar(left_edges, height)
    plt.title("Ages Vs Salaries graph")
    plt.xlabel("ages")
    plt.ylabel("salaries")
    plt.show()

#legend()
plt.legend()
barchart_of_ages_salaries()





