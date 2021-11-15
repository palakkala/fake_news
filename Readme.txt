1. Use requirement.txt to setup an enviorment 
2. Please download GoogleNews-vectors-negative300.bin.gz and unzip it in the root directory of the project folder 

https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit?resourcekey=0-wjGZdNAUop6WykTtMip30g

3. Please use config.txt for the required configuration 

4.Please train the model using below script
python train.py --file config.ini

5 to test the model with the test.csv run the below command 
python predict.py --file test.csv

6 my_model folder is trained model using google news word2vec embedding please unzip and download in the root folder 

