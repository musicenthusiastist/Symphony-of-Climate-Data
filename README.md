# Team_Data-Quintet
**Project Descriptions**

Have you ever wondered how data can be represented aurally? And to musicians/ music lovers: are you looking for new inspirations of your music? If you answered yes, I encourage you to take a look at our **Data Sonification** project. 

Our project provides a method to transform meteorological data into a unique piece of music. **Unlike most music compositions, our piece of music is encoded with climate data** - `annual temperature` and `annual total number of natural disasters` of Ontario from 1930 to 2016. By listening to our music, you will get the overall pattern of the Ontario's climate in this period. We added our own interpretation when assigning instruments for the background. In our opinion, our data sonification music is more expressive than a 2-dimensional data visualization product, because it adds the time dimension in. 

**Our approaches include:**
- Find data from databases: 
  + **annual temperature of Ontario from 1930 to 2016** (hereinafter referred to as `*temp_data*`), 
  + **annual total number of natural disasters in Ontario from 1930 to 2016** (hereinafter referred to as `*count_disaster*`).
- Statistical analysis using **SAS**: 
  + write scripts to analyse the correlation of `*temp_data*` and `*count_disaster*`. 
- **Javascript** JSON to CSV converter: 
  + extract relevent data
  + convert machine readable format JSON to human readable format CSV.
- Employ a **Music Algorithm** to transform the CSV to MIDI: 
  + `pitch input` = `*temp_data*`, and `note-duration input` = inverse of `*count_disaster*`. That is, at a specific instant of time, the higher a pitch is, the hotter that year used to be; the faster the notes are played, the more natural disasters that year used to have.
- **Music composition** in **Digital Audio Workstation (DAW)**: 
  + find an appropriate key (C minor, in our case), listen to the MIDI's pattern, get an understanding of what this pattern conveys, then compose background music based on the above. Lastly, add the MIDI on top. 

This project is meant to show how data science and artworks can be combined; and to explore new ways of data representations.


