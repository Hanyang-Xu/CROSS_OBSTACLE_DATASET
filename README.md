# CROSS_OBSTACLE_DATASET
***
## INTRODUCTION
Understanding what changes people make in order to **cross obstacles of different heights** is useful for designing wearable robots such as prosthetics and exoskeletons. However, previous studies have not systematically analyzed the changes in biomechanics as people cross obstacles of different heights.We used the motion capture system to collect the data, and used the ***Helen Hayes model*** to process the raw data to get hip, knee and ankle angles, torque data, and ground reaction. This dataset collected biomechanical data from 10 subjects *(6 men and 4 women, with an average age of around 20 years)* while crossing obstacles of different heights.
***
## HOW TO USE
1. Download the dataset in [Datasets](Datasets "Datasets")<br>
2. Download the code to extract data in [scripts](scripts "scripts")<br>
3. Changing the pathfile ``path = "D:\\lab\\experiment\\data\\AB01" `` in order to get all biomechanics data of any subject and draw the graph<br>
    **ATTENTION**  Only one subject's data can be processed at a time
### EXAMPLE
![alt](example/AB03_left.png "AB03_left")<br>
![alt](example/AB03_left_avg.png "AB03_left_average")<br>
### ADDITION
If you just want to extract the data of the individual joints without drawing a graph, you can delete the drawing code and just use part of the code like ``force = pd.read_excel(file_path, sheet_name='force')``
***
## Usage
This dataset can be used for research in multiple fields, including but not limited to exoskeletons, powered thigh prosthetics, and medical research.
