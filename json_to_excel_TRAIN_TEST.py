import pandas as pd
import gzip
from sklearn.model_selection import train_test_split

def parse(path):
  g = gzip.open(path, 'rb')
  for l in g:
    yield eval(l)

def getDF(path):
  i = 0
  df = {}
  for d in parse(path):
    df[i] = d
    i += 1
  return pd.DataFrame.from_dict(df, orient='index')

df = getDF('reviews.gz')
#train_test_split(80-20%)
train, test = train_test_split(df, test_size=0.2)

train_writer=pd.ExcelWriter('pandas_sample_TRAIN.xlsx',engine='xlsxwriter')
test_writer=pd.ExcelWriter('pandas_sample_TEST.xlsx',engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
train.to_excel(train_writer, sheet_name='Sheet1')
test.to_excel(test_writer,sheet_name="Sheet1")


train_writer.save()
test_writer.save()

# Close the Pandas Excel writer and output the Excel file.
print('Files written to EXCEL file!! ')

