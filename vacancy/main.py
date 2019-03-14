import InstitutesHandler as ih
import re

def main():
    kfu = ih.kfu.get_vacancy() 
    print("Казанский (Приволжский) федеральный университет") 
    for i, k in enumerate(kfu, 1): 
        print(str(i)+'.', k['title'], k['salary'], k['url'], sep='\n')
    
    inno=ih.inno.get_vacancy()
    print("Университет Иннополис")
    for i,k in enumerate(inno,1):
        print(str(i)+'.',k['title'], k['salary'], k['url'], sep='\n')

def compare(list,word):
    res=[]
    for i in list:
        if re.search(r'(?i){}'.format(word),i['title']):
            res.append(i)
    return res

def search(word):
    kfu = ih.kfu.get_vacancy()
    inno=ih.inno.get_vacancy() 
    
    kfu_res=compare(kfu,word)
    inno_res=compare(inno,word)
    
    print("\nКазанский (Приволжский) федеральный университет")
    for i, k in enumerate(kfu_res, 1): 
        print(str(i)+'.', k['title'], k['salary'], k['url'], sep='\n')

    print("\nУниверситет Иннополис")
    for i,k in enumerate(inno_res,1):
        print(str(i)+'.',k['title'], k['salary'], k['url'], sep='\n')

if __name__=='__main__':
    # main()
    search("программисТ")   
