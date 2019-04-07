def weight_on_planets():
    weight = input("What do you weigh on earth?")
    earthWeight = float(weight)
    weightMars = earthWeight * 0.38
    weightJupiter = earthWeight * 2.34
    print(" \nOn Mars you would weigh %s pounds.\nOn Jupiter you would weigh %s pounds." % (weightMars, weightJupiter))
   
if __name__ == '__main__':
   weight_on_planets()
