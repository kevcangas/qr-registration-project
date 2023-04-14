



#Function to get the id for create objects
def id(model, start=0):
    i = start
    while True:
        try:
             model.get_by_id(i)
             i+=1
        except:
             return i


if __name__ == '__main__':
    print("This is a module")