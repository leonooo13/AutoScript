import os
current_floder="E:\Algorithms"
def delete_empty(current_floder:str):
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
    floder=input()
    delete_empty(floder)