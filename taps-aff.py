# in future could pass input_file as an argument

input_file = 'input.csv'
import pandas as pd
df = pd.read_csv(input_file)
#print(df)




def is_fahrenheit(location):
    return location in {'Boston'}



# this is not an ideal solution, probably best to fetch a bunch of place names from an API and have a fahrenheit dict
# but also this is a bad solution because of cambridge england, cambridge massachusetts etc. There is no way to accurately distinguish these
# without more data. 



# a piece of supporting (but definitely not definitive) evidence is the range in which the raw temp is. e.g. if it's 90 then thats very 
# unlikely to be celsius. However 10 fahrenheit is a perfectly plausible, if cold, temperature so this doesn't help a vast amount

# if low memory then I propose having just a fahrenheit dict and if something is in the dict then just accepting it as fahrenheit

# if memory is less of an issue then could have a fahrenheit and celsius dict. If a location appears in only one then great.
# if it appears in both then if raw temp  > 45 or 50 (or some other magic number) then accept it as fahrenheit. Else there isn't really 
# much you can do and to make it deterministic I would just say if above 20, call it fahrenheit.
# This can introduce consistent errors though and give the pretence of a trend. Another way would be
# to say its fahrenheit if it is even, this however doesn't take into account that higher numbers 
# are probably more likely to be fahrenheit



def in_celsius(location, temp):
    if is_fahrenheit(location):
        return (temp - 32) * 5/9
    else:
        return temp



locs_raw_temps = list(zip(df['location'], df['temperature']))




clothes = ['tshirt' if in_celsius(loc, temp) >= 15 else 'jumper' 
           for loc, temp in locs_raw_temps]

df['what_to_wear'] = clothes


#print(df.columns)
#print(df)

df.to_csv('output.csv', index=False)





