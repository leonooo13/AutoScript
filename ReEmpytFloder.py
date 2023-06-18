import os
current_floder="E:\Algorithms"
def delete_empty(current_floder:str):
    if len(current_floder)==0:
        current_floder=os.getcwd()
    print("current path is ",current_floder)
    for root,dir,filename in os.walk(current_floder):
        for dirname in dir:
            dirpath=os.path.join(root,dirname)
            if not os.listdir(dirpath):
                # delete empty floder
                try:
                    os.removedirs(dirpath)
                    print("delete empty floder is ",dirpath)
                except Exception as e:
                    print("delete Error, ",str(e))
if __name__=="__main__":
    print("*"*10)
    print("input the floder which is you want to delete empty floder")
    print("for example: | E:\Algorithms| it will delete all empty floders automatically")
    print("if you willn't to keyin you need it place it target dir blow,This way you entry Enter")
    print("*"*10)
    floder=input()
    delete_empty(floder)