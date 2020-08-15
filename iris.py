import streamlit as st

def main():
	""" A simple Iris EDA App """
	st.title("Streamlit example")
	
	st.write("""
	# Explore different classifiers
	Which one is the best?
	""")

	dataset_name = st.selectbox("Select dataset",("Iris","Breast Cancer","Wine dataset"))
	st.write(dataset_name)

if __name__ == '__main__':
	main()