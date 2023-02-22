# Commonality Metric  for enhancing Cultural citizenship

This is the Python code that tries to reproduce the algorithm presented in the 
[Measuring Commonality in Recommendation of Cultural
Content: Recommender Systems to Enhance Cultural
Citizenship](https://841.io/doc/commonality.pdf)

## Notes: 
- For now it creates dummy ranking lists with the defines categories. The editorial selected categories are 30% present in the rankings
- TODO: calculate the system metric and not just the Commonality per category.


## How to run

```python
python3 main.py -m 1 -n 100 -p 0.8
```
where: 
* -m : number of users/ ranking lists
* -n size of ranking lists
* -p the user's patience that represents how far down the ranking the user will "listen"