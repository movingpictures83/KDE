import matplotlib.pyplot as plt
import seaborn as sns
import pandas

class KDEPlugin:
 def input(self, inputfile):
  self.df = pandas.read_csv(inputfile)
 def run(self):
  sns.kdeplot(data=self.df, shade=True)
 def output(self, outputfile):
  plt.savefig(outputfile)
