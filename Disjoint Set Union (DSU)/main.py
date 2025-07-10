# First we write a Recursive function, 
# Iske parameter me jo "i" hai wo denote karta hai jiska mujhe find karna hai aur jo parent hai wo set ka leader hai
def Find(i, parent):
    if i == parent[i]:
        return i
    return Find(parent[i], parent)

# Uske baad hum Union ka function likhenge

def Union(x, y, parent):
    x_ka_parent = Find(x, parent)
    y_ka_parent = Find(y, parent)

    if x_ka_parent != y_ka_parent:
        parent[x_ka_parent] = y_ka_parent   
        # Hum yahan pe kisi ko v parent bana sakte hai
        # Ye humare upar hai Like main iss line ki jagah
        # parent[y_ka_parent] = x_ka_parent v likh sakta hun ye totally humare control me hai.

# The above code is worst case TC because agar Jyada number of sets hue to jyada time lega ekk ekk karke check karte jaayega ki ye iska parent hai yaa nahi
# TC - O(N) because recursive function har ekk element ko check karke dhundhega ki bhai tum parent ho yaa nahi...

# Ab ekk cheez kar skte hain ki pure path ko hum compree kar dein to thora improve ho jaayega time complexity

# Kuch Nhi karna hai bus ekk line change karni hai upar waale find function me 

def Find(i, parent):
    if i == parent[i]:
        return i
    parent[i] = Find(parent[i], parent) # path compression
    return parent[i]

def Union(x, y, parent):
    x_ka_parent = Find(x, parent)
    y_ka_parent = Find(y, parent)

    if x_ka_parent != y_ka_parent:
        parent[x_ka_parent] = y_ka_parent   

# Now The TC of this above code is nearly nearly about O(1) (basically it's O(α(N)) which is nearly constant)


# Now ab Optimised code likhte hain Union ka according to Rank and path compression

def Find(i, parent):
    if i == parent[i]:
        return i
    parent[i] = Find(parent[i], parent) # path compression
    return parent[i]

def Union(x, y, parent, rank):
    x_ka_parent = Find(x, parent)
    y_ka_parent = Find(y, parent)

    if x_ka_parent == y_ka_parent:
        return
    
    if rank[x_ka_parent] > rank[y_ka_parent]:
        parent[y_ka_parent] = x_ka_parent
    elif rank[x_ka_parent] < rank[y_ka_parent]:
        parent[x_ka_parent] = y_ka_parent
    else:
        parent[x_ka_parent] = y_ka_parent
        rank[y_ka_parent] += 1

# Time complexity ~ O(1) which is most optimised code for DSU

''' Logic --> 
              (1) - Rank agar equal hai to kisi ekk ko parent bana do (it's your choice) aur rank ko +=1 kar do
              (2) - Rank agar equal nahi hai then jiska rank sabse upar hai ussi ko parent bana do.
'''

    