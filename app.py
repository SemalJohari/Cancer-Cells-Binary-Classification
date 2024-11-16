import pickle as pk
import streamlit as st

# Load the model and the scaler
model = pk.load(open('model.pkl', 'rb'))

# Unique values for each feature
clump_values = [5, 3, 6, 4, 8, 1, 2, 7, 10, 9]
unif_size_values = [1, 4, 8, 10, 2, 3, 7, 5, 6, 9]
unif_shape_values = [1, 4, 8, 10, 2, 3, 5, 6, 7, 9]
marg_adh_values = [1, 5, 3, 8, 10, 4, 6, 2, 9, 7]
sing_epi_size_values = [2, 7, 3, 1, 6, 4, 5, 8, 10, 9]
bare_nuc_values = [1, 10, 2, 4, 3, 9, 7, 5, 8, 6]
bland_chrom_values = [3, 9, 1, 2, 4, 5, 7, 8, 6, 10]
norm_nucl_values = [1, 2, 7, 4, 5, 3, 10, 6, 9, 8]
mit_values = [1, 5, 4, 2, 3, 7, 10, 8, 6]

introduction = """
### About This Project:

This is a minor Machine Learning project made using Numpy, Streamlit, Pandas, and Scikit-learn  
libraries to classify a given cancer cell as Malignant or Benign. The model has been trained on  
the Cell Samples dataset which contains 600+ rows of features like 'Clump', 'UnifSize', 'UnifShape', 
'MargAdh', 'SingEpiSize', 'BareNuc', 'BlandChrom', 'NormNucl', 'Mit' classified as Malignant or Benign.
"""

def display_instruction_window():
    with st.expander("💡 Information about the features", expanded=False):
        st.markdown("""
            ### Terminologies:
            1. Clump: Clump Thickness – Measures the thickness of cell clusters.
            2. UnifSize: Uniformity of Cell Size – Evaluates how consistent the sizes of cells are.
            3. UnifShape: Uniformity of Cell Shape – Assesses the uniformity in the shapes of cells.
            4. MargAdh: Marginal Adhesion – Indicates how well cells adhere to each other at the margins.
            5. SingEpiSize: Single Epithelial Cell Size – Represents the size of isolated epithelial cells.
            6. BareNuc: Bare Nuclei – Refers to nuclei that are not surrounded by cytoplasm.
            7. BlandChrom: Bland Chromatin – Describes the texture and appearance of chromatin in the nucleus.
            8. NormNucl: Normal Nucleoli – Evaluates the presence and appearance of nucleoli in cells.
            9. Mit: Mitoses – Counts the number of mitotic figures, indicating cell division activity.
            """)

def page():
    st.title("Cancer Cells Binary Classification") 
    st.markdown(introduction)

page()
display_instruction_window()

# Create a 3x3 grid of dropdowns using columns
col1, col2, col3 = st.columns(3)

with col1:
    clump = st.selectbox('Clump Thickness', clump_values)
    unif_size = st.selectbox('Uniformity of Cell Size', unif_size_values)
    unif_shape = st.selectbox('Uniformity of Cell Shape', unif_shape_values)

with col2:
    marg_adh = st.selectbox('Marginal Adhesion', marg_adh_values)
    sing_epi_size = st.selectbox('Single Epithelial Cell Size', sing_epi_size_values)
    bare_nuc = st.selectbox('Bare Nuclei', bare_nuc_values)

with col3:
    bland_chrom = st.selectbox('Bland Chromatin', bland_chrom_values)
    norm_nucl = st.selectbox('Normal Nucleoli', norm_nucl_values)
    mit = st.selectbox('Mitoses', mit_values)

# Predict button
if st.button('Predict'):
    # Create a feature vector for the input values
    features = [
        clump,
        unif_size,
        unif_shape,
        marg_adh,
        sing_epi_size,
        bare_nuc,
        bland_chrom,
        norm_nucl,
        mit
    ]
    
    # Make the prediction
    result = model.predict([features])
    
    # Display the result
    if result[0] == 2:
        st.write('Benign Cell')
    else:
        st.write('Malignant Cell')

