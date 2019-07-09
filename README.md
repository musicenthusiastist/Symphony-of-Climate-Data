# Team_XX
To all data scientists: we know that data can be visualized, but have you ever wondered if data can be represented aurally? To all musicians: are you looking for new inspirations of your compositions? To coding enthusiasts: want to try using some music algorithms in your works? In other words, are you fascinated by the idea of **Data Sonification**? 

Our project provides a method to transform meteorological data into a unique piece of music. Unlike most music compositions, our piece of music is encoded with severial aspects of information, including climate data of Ontario from 1930 to 2016, the overall pattern of the climate change in this period, our inferrence of the climate in the past, and our hope for the future. In our mind, data sonification is more expressive than a 2-dimensional data visualization product, because it adds the time dimension in.

Our approaches include:
- Find data from databases: annual temperature of Ontario from 1930 to 2016 (hereinafter referred to as *temp_data*), and number of natural disasters in Ontario from 1930 to 2016 (hereinafter referred to as *count_disaster*).
- Statistical analysis using SAS: write scripts to analyse the correlation of *temp_data* and *count_disaster*. 
- Javascript JSON to CSV converter: extract relevent data, and convert machine readable format to human readable format.
- Employ a Music Algorithm to transform the CSV from previous step to MIDI: pitch = *temp_data*, and note-duration = inverse of *count_disaster*. That is, at a specific instant of time, the higher a pitch is, the hotter that year used to be; the faster the notes are played, the more natural disasters that year used to have.
- MIDI editing and composition in Digital Audio Workstation (DAW):  


