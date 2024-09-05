import numpy, m8r

inp = m8r.Input('test.rsf')
n1 = inp.int("n1")
n2 = inp.int("n2")

data =inp.read(shape=(n2,n1))
data = data.transpose() # Example of numpy in action

print(data)
