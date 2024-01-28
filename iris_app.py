import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load dataset (iris)
def load_data():
    iris = sns.load_dataset('iris')
    return iris

iris_data = load_data()

# write something on streamlit
# Create the title for the App
st.title("Iris Experiment")
st.write("## Navigate through the Various Iris types")
st.write("A platform created by a researcher from the University of Hull allows users explore various iris types")

# let's show the full iris table on the streamlit app. 
st.write(iris_data)

# control s to save
# change directory at terminal - cd streamlit_sample
# run it; streamlit run iris_app.py : when you see email, click enter

# creating sidebar for feature selection
st.sidebar.subheader("Select features for Bivariate Plot")
#select all features except the last one (the target)
# selectbox is like a drop down; we are selecting a features for users to select except the target 
# the target is the last column on the dataset/dataframe
x_feature = st.sidebar.selectbox('X-axis Feature', 
                                 iris_data.columns[:-1]) #excluding the target
# do same for y
y_feature = st.sidebar.selectbox('Y-axis Feature', 
                                 iris_data.columns[:-1]) #similar box, without target

#st.subheader('Segmenting data')
st.write('## Segmenting data')
st.write("#### Explore the iris table based on your iris specie preference")
# the target is 'specie'
# this is by the way, has nothing to do with the plots. This will create a subset of the table,
# depending on what you select as your target. the table changes ater you select a target 
target_cat = st.sidebar.selectbox('Target Categories',
                                   iris_data['species'].unique()) #
segment_data = iris_data[iris_data['species']== target_cat]
st.write(segment_data)

#st.subheader('Iris Table Visualization')
st.write('## Iris Table Visualization')
st.write('#### Visually exploring the iris table using dashboards/plots')
# Create a bivariate scatter plot
st.write(f"### Bivariate Plot between {x_feature} and {y_feature}") # title changes depending on what the user selects
fig, ax = plt.subplots()
sns.scatterplot(data = iris_data, x = x_feature, y = y_feature, 
                hue = "species")
plt.xlabel(x_feature)
plt.ylabel(y_feature)
st.pyplot(fig)
#  Filtering the dataset based on the user input
# note that the target category was used to filter the data in the 'segmenting data' stage; it's not relevant here
## Create a slider for selecting the sepal length range
st.subheader("Creating Slider")
sepal_length_min= st.slider("Minimum Sepal Length", min_value= 0.0,
                             max_value=10.0,value = 5.2)

sepal_length_max= st.slider("Maximum Sepal Length", min_value= 0.0,
                             max_value=10.0,value = 10.0)
st.write(sepal_length_min) # to display whatever vale the user picks
st.write(sepal_length_max)

# select species using a radio button
species = st.radio('select a specie', iris_data['species'].unique())

filtered_data = iris_data[
    (iris_data["sepal_length"] >= sepal_length_min) &
    (iris_data["sepal_length"] <= sepal_length_max)| #or
     (iris_data["species"] == species)]
#Filter the dataset and display to the screen
st.write(filtered_data)


