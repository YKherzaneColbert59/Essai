class Pile:
    def __init__(self):
        self.pile = []
        self.top = None
        
    def est_vide(self):
        return self.pile==[]
    
    def sommet(self):
        return self.top
    
    def empiler(self, el):
        self.pile.append(el)
        self.top = el
        
    def depiler(self):
        if self.pile==[]:
            self.top = None
        else:
            el = self.pile.pop()
            if not self.est_vide():
                self.top = self.pile[-1]
            else:
                self.top = None
            return el
        return None
        
def verifParentheses(chaine):
    p = Pile()
    
    for c in chaine:
        if c == '(':
            p.empiler(c)
            
        if c == ')':
            if p.sommet() == '(':
                p.depiler()
            else:
                return False
            
    return p.est_vide()

    
a = Pile()
a.empiler(1)
a.empiler(2)
a.empiler(3)
a.empiler(4)
a.empiler(5)

# a.depiler()
# a.depiler()
# a.depiler()
# a.depiler()
# a.depiler()