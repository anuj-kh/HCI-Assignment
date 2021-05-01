# HCI-Assignment

The problem statement can be found [here](./selenium-assignment-2-21.pdf)
## Part A
The selenium script, first opens a few websites, and then follows all the hyperlinks on the home page using selenium. 
It notes down the link, the time for the corresponding pages to load (average of 5 attempts), the number of deadlinks and the number of links that work.
It then calculates the website score using the following formulae:

```
col1: Average link load time
col2: Number of dead links
col3: Number of working links
A: normalized Average Link Load Time (Mobile Network)
A = (val(col1) - min(col1)) / (max(col1) - min(col1))
B: Fraction of dead links
B = val(col2) / (val(col2) + val(col3))
Website score = (A + B) / 2
```

The observations can be found in this [document](./Part_A/HCI%20A2%20part%201.pdf)

## Part B
It includes the user evaluation for a few websites using the selenium IDE. Then a script is used to analyse the recordings to find the number of clicks required by the users
to add the product to cart in Flipkart and SnapDeal. 

The observations can be found in this [document](./Part_B/HCI%20A2%20part%202.pdf)
