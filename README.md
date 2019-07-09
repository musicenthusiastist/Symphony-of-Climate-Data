# Team_XX
**Project Descriptions**

Hey, data scientists! It's very well-known that data can be visualized, but have you ever wondered how data can be represented aurally? Hey, musicians! Are you looking for new inspirations of your compositions? And hello to fellow coding enthusiasts -- want to try using some music algorithms in your works? In other words, **are you fascinated by the idea of Data Sonification**? 

Our project provides a method to transform meteorological data into a unique piece of music. **Unlike most music compositions, our piece of music is encoded with severial aspects of information**, including climate data of Ontario from 1930 to 2016, the overall pattern of the climate change in this period, our inferrence of the climate in the past, and our hope for the future. In our mind, data sonification is more expressive than a 2-dimensional data visualization product, because it adds the time dimension in. How did we achieve all these?

**Our approaches include:**
- Find data from databases: **annual temperature of Ontario from 1930 to 2016** (hereinafter referred to as *temp_data*), and **number of natural disasters in Ontario from 1930 to 2016** (hereinafter referred to as *count_disaster*).
- Statistical analysis using **SAS**: write scripts to analyse the correlation of *temp_data* and *count_disaster*. 
- **Javascript** JSON to CSV converter: extract relevent data, and convert machine readable format JSON to human readable format CSV.
- Employ a **Music Algorithm** to transform the CSV to MIDI: `pitch input` = *temp_data*, and `note-duration input` = inverse of *count_disaster*. That is, at a specific instant of time, the higher a pitch is, the hotter that year used to be; the faster the notes are played, the more natural disasters that year used to have.
- **Music composition** in **Digital Audio Workstation (DAW)**: find an appropriate key (C minor, in our case), listen to the MIDI's pattern, get an understanding of what this pattern conveys, then compose background music based on the above. Lastly, add the MIDI on top. 

This project is meant to show how data science and artworks can be combined; and to explore new ways of data representations.


