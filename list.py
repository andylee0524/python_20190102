empty_list = [];
print("emptyList=",empty_list);
weekdays = ["Monday", "Tuesday", "wednesday"];
print(weekdays);
print(type(weekdays));
another_empty_lsit = list();
print(list('cat'));
a_tupe = ('ready', 'fire', 'aim');
#a_tupe[0] = 'notReady';
print(a_tupe[0]);
print(list(a_tupe));
birthday = "1/11/2019";
print(birthday.split('/'));

marxes = ["Groucho", "Chico", "Harpo"];
print(marxes[0]);
print(marxes[1]);
print(marxes[2]); 
#print(marxes[3]);
print(marxes[-1]);
print(marxes[-2]);
print(marxes[-3]);

small_birds = ['hummingbird', 'finch'];
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue'];
all_birds = [small_birds, extinct_birds, 'macaw'];
print(all_birds[0][0]);

marxes = ['Groucho', 'Chico', 'Harpo'];
#marxes[2] = 'Wanda'
print(marxes);
print(marxes[0:2]);
print(marxes[::2]);

marxes.append("Zeppo");
print(marxes);
others = ["Gummo", "karl"];
#marxes.extend(others);
marxes += others;
print(marxes);

marxes.insert(20, 'Gummoo');
print(marxes);

del marxes[-1];
print(marxes);
marxes.remove('Chico')
print(marxes);
print(marxes.index('Zeppo'));

print('Zeppo' in marxes);
marxes = ["Groucho", "Chico", "Harpo"];
#marxes.sort();
#print(marxes);
sorted_marxes = sorted(marxes);
print(marxes);
print(sorted_marxes);
marxes.sort(reverse=True);
print(marxes);

print(len(marxes));

a = [1, 2, 3];
print(a);
b = a;
print(b);
del a[0]
print(b);

a = [1, 2, 3];
print(a);
b = a.copy();
b = list(a);

del b[0];
print(a);
print(b);
