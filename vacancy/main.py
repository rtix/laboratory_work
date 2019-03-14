import InstitutesHandler as ih
import re


def compare(list,word):
    res=[]
    for i in list:
        if re.search(r'(?i){}'.format(word),i['title']):
            res.append(i)
    return res


def search(word):
    kfu = ih.kfu.get_vacancy()
    inno = ih.inno.get_vacancy() 
    
    result = {"Казанский (Приволжский) федеральный университет:":compare(kfu,word),
                "Университет Иннополис:":compare(inno,word)}

    return result
    

def main():
    result = search(input("Введите искомую вакансию"
                            "(Enter, если нет предпочтений):"))
    for uni in result.items():
        print(uni[0])
        for i, k in enumerate(uni[1], 1): 
            print(str(i)+'.', k['title'], k['salary'], k['url'], sep='\n')
        print('\n')


if __name__=='__main__':
    main()
