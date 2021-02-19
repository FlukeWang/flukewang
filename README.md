# My first Library - Class

# how to install

open CMD / Terminal

``` python
pip install flukewang
```

# how to play
open IDE and type ....
``` python
from flukewang import Shohoku, NYC
print('-----1 Jan 2021 -------')
player1 = NYC('Kevin Durant', 'Nets')
player1.askexp()
player1.showexp()
student1 = Shohoku('Rukawa')
print(student1.name)
student1.Hello()
student2 = Shohoku('Akagi')
print(student2.name)
student2.Hello()

print('-----2 Jan 2021 -------')
print('Who want to traing basketball today for 10 exp ? ')
print(student1.name, ' : Me !')
student1.addexp(10)

print('-----3 Jan 2021 -------')
print('Total individul exp : ')
student1.name = 'Rukawa Kaede'
print(student1.name, student1.exp)
print(student2.name, student2.exp)

print('-----4 Jan 2021 -------')
for i in range(5):
    student2.coding()
student1.showexp()
student2.showexp()


```


By: Thammasorn Wongapdklang
