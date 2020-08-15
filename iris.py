import streamlit as st
from sklearn import datasets

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

import numpy as np

def main():
	""" A simple Iris EDA App """
	st.title("Streamlit ML example")
	
	st.write("""
	# Explore different classifiers
	Which one is the best?
	""")

	dataset_name = st.selectbox("Select Dataset",("Iris", "Breast Cancer", "Wine dataset"))
	
	classifier_name = st.selectbox("Select Classifier",("KNN", "SVM", "Random Forest"))	

	def get_dataset(dataset_name):
		if dataset_name == "Iris":	
			data = datasets.load_iris()
		elif dataset_name == "Breast Cancer":
			data = datasets.load_breast_cancer()
		else:
			data = datasets.load_wine()
		X = data.data
		y = data.target
		return X, y

	X, y = get_dataset(dataset_name)
	st.write("shape of dataset", X.shape)
	st.write("number of classes", len(np.unique(y)))

	def add_parameter_ui(clf_name):
		params = dict()
		if clf_name == "KNN":
			K = st.slider("K",1,15)
			params["K"] = K
		elif clf_name == "SVM":
			C = st.slider("C",0.01,10.0)
			params["C"] = C
		else:
			max_depth = st.slider("max_depth", 2, 15)
			n_estimators = st.slider("n_estimators", 1, 100)
			params["max_depth"] = max_depth
			params["n_estimators"] = n_estimators
		return params

	add_parameter_ui(classifier_name)

if __name__ == '__main__':
	main()