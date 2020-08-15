import streamlit as st
from sklearn import datasets
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

if __name__ == '__main__':
	main()