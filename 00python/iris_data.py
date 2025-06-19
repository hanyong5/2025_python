#pip install -U scikit-learn
#pip uninstall scikit-learn
#pip install scikit-learn
from sklearn import datasets

iris = datasets.load_iris()

print(iris.keys())
