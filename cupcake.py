from collections import Counter
import collections

paragraphs = """
Jelly beans bear claw tart. Lemon drops cotton candy ice cream fruitcake cake croissant marzipan sesame snaps topping. Wafer sweet jujubes. Cupcake candy biscuit chupa chups toffee. Cupcake cake fruitcake cotton candy candy canes. Tiramisu jujubes jelly-o dessert. Jelly beans muffin lollipop. Cheesecake wafer muffin sweet roll carrot cake. Chupa chups candy canes gingerbread chocolate cake sweet dessert. Cotton candy dragée chocolate cake. Tart cotton candy jelly beans sesame snaps ice cream. Bonbon ice cream tart powder.
Cheesecake tiramisu gummies brownie pie bonbon liquorice cotton candy oat cake. Donut chupa chups pie chocolate bar gingerbread cupcake oat cake apple pie jujubes. Chocolate chocolate oat cake jelly-o cotton candy chocolate bar. Cake sugar plum halvah soufflé croissant bear claw dragée soufflé. Donut jelly cheesecake halvah topping pastry. Ice cream marshmallow cookie gummies macaroon topping topping lemon drops sweet. Pie soufflé tootsie roll cake wafer chocolate powder. Lollipop soufflé sweet jujubes jelly-o powder pastry sweet roll. Ice cream topping candy canes. Pie wafer lemon drops powder lemon drops. Chocolate bar powder candy cupcake pastry halvah cake. Chocolate cake bonbon jujubes liquorice fruitcake gummi bears jujubes. Tootsie roll topping caramels toffee pie.
Lemon drops macaroon jelly-o sweet roll sweet roll. Halvah wafer marshmallow dessert cake. Pastry jelly-o gummi bears biscuit biscuit. Tootsie roll powder cake gingerbread. Gingerbread cookie carrot cake fruitcake bonbon jujubes candy pudding. Gummi bears croissant sweet marshmallow pudding marzipan. Lemon drops marzipan soufflé liquorice soufflé chocolate bar halvah jelly-o danish. Pie jelly oat cake brownie pudding powder chupa chups cupcake. Tootsie roll donut marzipan sesame snaps halvah gingerbread. Cake pudding sweet soufflé. Muffin pastry icing pie cheesecake wafer fruitcake. Pie chocolate cake jelly cookie cookie jelly beans pie.
Chocolate cake cupcake pastry jujubes cotton candy. Chocolate bar gingerbread jujubes icing liquorice jujubes powder candy canes toffee. Ice cream macaroon brownie pie ice cream topping cotton candy lollipop. Pie danish dragée danish sweet apple pie cake carrot cake jelly beans. Gummi bears lollipop donut bonbon caramels. Gummi bears cupcake soufflé chocolate bar jelly beans halvah marshmallow pie cake. Pastry caramels sesame snaps lollipop tootsie roll tiramisu gummi bears sesame snaps. Donut marshmallow dessert pudding jujubes cupcake dragée sesame snaps cupcake. Fruitcake tootsie roll sweet roll candy canes cupcake marzipan. Jujubes cake tart cheesecake. Fruitcake jelly cake muffin apple pie oat cake pudding cheesecake. Soufflé apple pie lemon drops toffee. Candy sesame snaps brownie cotton candy soufflé sweet roll gingerbread donut liquorice.
Bear claw lemon drops candy canes gummi bears toffee dragée. Muffin toffee powder soufflé sugar plum topping. Ice cream ice cream sweet roll cake. Bear claw jelly-o muffin jelly-o toffee apple pie brownie. Oat cake liquorice pastry pie cookie pie. Muffin biscuit jujubes jujubes pie sweet roll tiramisu gummi bears bonbon. Tiramisu marzipan halvah candy powder pastry chupa chups ice cream. Gummi bears sesame snaps donut pastry lemon drops. Oat cake pastry donut. Candy chocolate cake marzipan pastry cake. Candy marzipan tootsie roll jelly beans cheesecake candy canes chocolate cake sugar plum. Jelly jelly-o brownie sweet roll. Danish candy canes danish tootsie roll tiramisu chupa chups jujubes lollipop.
"""
paragraphs = paragraphs.split()
new_paragraphs = []
for word in paragraphs:
    if '.' in word:
        word = word[:-1]
    new_paragraphs.append(word)

counts = Counter(new_paragraphs)

collections.OrderedDict(sorted(counts.items()))

print(dir(counts))
print( list( sorted(counts.keys()) ) )
