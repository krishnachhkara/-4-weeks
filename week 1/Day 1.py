# Starting day 1 with basic code

# creating a class for bike and using it to apply opps concept

class Bike:
    def __init__(self):
        self.model = self.vehicle()
        self.years = self.year()
        self.rider = self.riders()
       

    def riders(self):
        print(f"we have following riders...")
        print("press 1 for Krishna")
        print("press 2 for Tyagi")    
        print("press 3 for vishal")    
        print("press 4 for Shuvidhu")
        rider = int(input("Choose your rider: "))
        match rider:
            case 1 : rider = "Krishna"
            case 2 : rider = "Tyagi"
            case 3 : rider = "vishal"
            case 4 : rider = "Shuvidhu"
            case _ : print("Riders are busy")
        return rider    

    def vehicle(self):
        print("We have following bikes...")
        print("press 1 for Dugati")
        print("press 2 for BMW")
        print("press 3 for special i.e Anmol")
        model = int(input("Choose your vehicle: "))
        match model:
            case 1 : model = "Dugati"
            case 2 : model = "BMW"
            case 3 : model = "Anmol"
            case _ : print("Bikes have no fuel and Anmol is in use")
        return model   

    def year(self):
        print("We have following year models available...")
        print("press 1 for 2024")
        print("press 2 for 2025")
        print("press 3 for 2026")
        year = int(input("Choose your preferred year: "))
        match year:
            case 1 : year = "2024"
            case 2 : year = "2025"
            case 3 : year = "2026"
            case _ : print("Chutiye upar wale option me se select kar")
        return year  
    
    def output(self):
        return f"You choosed {self.model} model {self.years} with rider as {self.rider}"


one = Bike()
print(one.output())

