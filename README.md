# OXF_autotrader

This is the code created for the oxford hackathon 2019. 

It contains the code used to input the data from the auto-listener into the google sheets as well as some tools that could create bollinger bands used for the initial strategy of mean reversion. 
I have lost most of the code of the initial mean reversion due to a laptop crash but I am reuploading the strategy_1.py file from Anmol's code as we worked on this together. 

The idea behind the strategy is to fix the number of data points to 10 and create an vector which keeps track of the volume of sellers and buyers for the instruments and calculate the ratio of buyers to sellers. And we make trades based on the value of this ratio. 

We later then combined this information with the mean-reversion data and moving volatilty but i can not seem to find the code on my laptop. 
