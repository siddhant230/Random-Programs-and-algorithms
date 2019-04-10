C='CdC' 
alpha = {
  'A': ['aH','J']+[C]*2+['J']*2+[C]*2,
  'B': ['I','J',C,'I'],
  'C': ['aH','J',C,'Cg'],
  'D': ['G','I']+[C]*2,
  'E': ['I']*2+['C','I'],
  'F': ['I']*2+['C']+['H']*2+['C']*3,
  'G': ['aH','J','C']+['CbE']*2+[C,'J','aH'],
  'H': [C]*3+['J'],
  'I': ['H']*2+['bD']*2,
  'J': ['fD']*5+['CcD','J','aH'],
  'K': ['CcD','CbD','CaD','G'],
  'L': ['C']*6+['I']*2,
  'M': ['CgC','DeD','EcE','M','CaEaC','CbCbC']+['CgC']*2,
  'N': [C,'DcC','EbC','FaC','CaF','CbE','CcD',C],
  'O': ['aH','J']+[C]*2,
  'P': ['I','J',C,'J','I']+['C']*3,
  'Q': ['aH','J','DcC','CaAbC','CbAaC','CcD','J','aH'],
  'R': ['I','J',C,'J','I','CaD','CbD','CcD'],
  'S': ['aI','K','C','J','aJ','hC','K','aI'],
  'T': ['L']*2+['dD']*6,
  'U': ['CfC']*5+['DdD','aJ','cF'],
  'V': ['CgC']*3+['aCeC','bCcC','cCaC','dE','eC'],
  'W': ['CgC']*3+['CbCbC','CaEaC','M','EcE','DeD'],
  'X': ['DeD','aDcD','bDaD','cG'],
  'Y': ['CgC','aCeC','bCcC','cCaC','dE']+['eC']*3,
  'Z': ['I']*2+['dD','cD','bD','aD']+['I']*2
  }

for t in ['B','C','D','E','H','I','K','O','X']: alpha[t]+=reversed(alpha[t])

def disp(CdC):
  for c in range(len(CdC)):
    flag=CdC[c].isupper()
    print(('0' if flag else ' ')*(ord(CdC[c])-(64 if flag else 96)), end='')
  print()

text=input('enter a string :').upper()
print('\n\n')

for i in range(len(text)):
    if not text[i].isalpha():
        print('\n\n')
        continue
    for r in range(8):
        disp('p'+alpha[text[i]][r])
    print()