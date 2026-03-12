import math as m
class InvalidChoiceError(Exception):
    def __init__(self,msg="Invalid Choice!"):
        self.msg=msg
class InvalidHeightError(Exception):
    def __init__(self,msg="Invalid Height Value!"):
        self.msg=msg
class InvalidWeightError(Exception):
    def __init__(self,msg="Invalid Weight Value!"):
        self.msg=msg
class BMI:
    def __init__(self):
        self.HEIGHT=0.0
        self.WEIGHT=0.0
        self.AGE=0.0
        self.GEN=""
    def get_details(self):
        height=float(input("\nEnter your Height: "))
        weight=float(input("Enter your Weight: "))
        age=float(input("Enter your age: "))
        gen=input("Your Gender: ")
        if (height>=24 and height<=251) or (height>=0.82 and height<=8.3):
            self.HEIGHT=height
        else:
            raise InvalidHeightError
        if (0.212<=weight and weight<=610.05) or (1<=weight and weight<=1345):
            self.WEIGHT=weight
        else:
            raise InvalidWeightError
        self.AGE=age
        self.GEN=gen
class Metric_bmi(BMI):
    def __init__(self):
        self.BMIPM=0.0
    def calculate_bmi(self):
        self.BMIPM=self.WEIGHT/m.pow(self.HEIGHT/100.0,2)
    def display_bmi(self):
        print(f"Your Body Mass Index:{self.BMIPM:.2f}")
    def display_details(self):
        print("Age:",self.AGE,"years")
        print("Height:",self.HEIGHT,"cm")
        print("Weight:",self.WEIGHT,"kg")
    def bmi_range(self):
        if self.BMIPM<16:
            self.bmi_category="Severe Thinness"
        elif 16<=self.BMIPM and self.BMIPM<17:
            self.bmi_category="Moderate Thinness"
        elif 17<=self.BMIPM and self.BMIPM<18.5:
            self.bmi_category="Mild Thinness"
        elif 18.5<=self.BMIPM and self.BMIPM<25:
            self.bmi_category="Normal"
        elif 25<=self.BMIPM and self.BMIPM<30:
            self.bmi_category="Overweight"
        elif 30<=self.BMIPM and self.BMIPM<35:
            self.bmi_category="Obese Class I"
        elif 35<=self.BMIPM and self.BMIPM<40:
            self.bmi_category="Obese Class II"
        elif self.BMIPM>=40:
            self.bmi_category="Obese Class III"
        else:
            pass
        return self.bmi_category
class US_bmi(BMI):
    def __init__(self):
        self.BMIPU=0.0
    def calculate_bmi(self):
        self.BMIPU=self.WEIGHT*703/m.pow(self.HEIGHT*12,2)
    def display_bmi(self):
        print(f"Your Body Mass Index:{self.BMIPU:.2f}")
    def display_details(self):
        print("Age:",self.AGE,"years")
        print("Height:",self.HEIGHT,"feet")
        print("Weight:",self.WEIGHT,"lbs")
    def bmi_range(self):
        if self.BMIPU<16:
            self.bmi_category="Severe Thinness"
        elif 16<=self.BMIPU and self.BMIPU<17:
            self.bmi_category="Moderate Thinness"
        elif 17<=self.BMIPU and self.BMIPU<18.5:
            self.bmi_category="Mild Thinness"
        elif 18.5<=self.BMIPU<25:self.bmi_category="Normal"
        elif 25<=self.BMIPU and self.BMIPU<30:
            self.bmi_category="Overweight"
        elif 30<=self.BMIPU and self.BMIPU<35:
            self.bmi_category="Obese Class I"
        elif 35<=self.BMIPU and self.BMIPU<40:
            self.bmi_category="Obese Class II"
        elif self.BMIPU>=40:
            self.bmi_category="Obese Class III"
        else:
            pass
        return self.bmi_category
print("----------------Welcome to Know-your-Body BMI Calc----------------")
ch="yes"
while(ch.lower()=="yes"):
    try:
        system=int(input("1. Metric system\n2. US system\nPlease enter your choice: "))
        if system==1:
            a=Metric_bmi()
            a.get_details()
            print()
            a.display_details()
            a.calculate_bmi()
            a.display_bmi()
            print("BMI Category:",a.bmi_range())
        elif system==2:
            b=US_bmi()
            b.get_details()
            print()
            b.display_details()
            b.calculate_bmi()
            b.display_bmi()
            print("BMI Category:",b.bmi_range())
        else:
            raise InvalidChoiceError
    except (InvalidChoiceError,InvalidHeightError,InvalidWeightError) as e:
        print("Processing Terminated :(",e.msg)
    ch=input("\nDo you want to try again [Yes/No]:- ")
print("\t\t**********Session Expired**********")
choice="yes"
while choice.lower()=="yes":
    try:
        choice=input("\nDo you want to find the ideal weight for your height [yes/no]: ")
        if choice.lower()!="yes":
            break
        m_h=0.0
        us_h=0.0
        upper_range=0.0
        lower_range=0.0
        h=float(input("Enter your height in cm/feet: "))
        if 0.82<=h<=8.3:
            us_h=h
            upper_range=(24.9*pow((us_h*12),2))/703
            lower_range=(18.5*pow((us_h*12),2))/703
            print(f"Ideal Weight:{lower_range:.2f}lbs-{upper_range:.2f}lbs")
        elif 24<=h<=251:
            m_h=h
            upper_range=24.9*pow((m_h/100),2)
            lower_range=18.5*pow((m_h/100),2)
            print(f"Ideal Weight:{lower_range:.2f}Kg-{upper_range:.2f}Kg")
        else:
            raise InvalidHeightError
    except InvalidHeightError as e:
        print("Processing Terminated :(",e.msg)
print("-----------------Session Ended-----------------")
opt="yes"
while(opt.lower()=="yes"):
    opt=input("\nAre you interested in finding your body type?[yes/no]: ")
    if opt.lower()!="yes":
            break
    print("You'll have to attempt a questionnarie with only integers [1/2/3] based on your answers.")
    d={}
    q1=input("Is losing weight 1.easy/2.moderate/3.difficult for you? ")
    q2=input("Is gaining weight 1.difficult/2.moderate/3.easy for you? ")
    q3=input("Are you in your ideal weight (1.No,I'm less/2.Yes,I'm /3.No,I'm too much): ")
    q4=input("Which is your BMI category?(1.Underweight/2.Healthy3.Overweight): ")
    q5=input("Which describes your upper to lower body ratio?(1.I don't know/2.Almost equal/3.Out of proportion): ")
    q6=input("How is your general appearance (1.skinny/2.normal/3.bulky): ")
    q7=input("Which explains your muscles the best? (1.lean/2.quite muscular/3.prominent): ")
    q8=input("How is your metabolism (1.pretty good/2.Average/3.Poor): ")
    q9=input("How is it for you to maintain your weight (1.Easy/2.Moderate/3.Difficult): ")
    q10=input("How is the fat distribution of your body? (1.Bony/2.Bony & Fleshy/3.Fleshy): ")
    s=[int(q1),int(q2),int(q3),int(q4),int(q5),int(q6),int(q7),int(q8),int(q9),int(q10)]
    o1=int(s.count(1))
    o2=int(s.count(2))
    o3=int(s.count(3))
    options=[o1,o2,o3]
    d[o1]="Ectomorph"
    d[o2]="Mesomorph"
    d[o3]="Endomorph"
    if o1>o2 and o1>o3:
        prior1=d[o1]
        print("Your Body type is:",prior1,(o1/10)*100,"%",end=" ")
        options.remove(o1)
        t=tuple(options)
        prior2=max(t)
        prior3=min(t)
        if prior2==prior3:
            print("+","Mesomorph",(o2/10)*100,"%",end=" ")
            print("+","Endomorph",(o3/10)*100,"%")
        else:
            print("+",d[prior2],(prior2/10)*100,"%")
    elif o2>o1 and o2>o3:
        prior1=d[o2]
        print("Your Body type is:",prior1,(o2/10)*100,"%",end=" ")
        options.remove(o2)
        t=tuple(options)
        prior2=max(t)
        prior3=min(t)
        if prior2==prior3:
            print("+","Ectomorph",(o1/10)*100,"%",end=" ")
            print("+","Endomorph",(o3/10)*100,"%")
        else:
            print("+",d[prior2],(prior2/10)*100,"%")
    else:
        prior1=d[o3]
        print("Your Body type is:",prior1,(o3/10)*100,"%",end=" ")
        options.remove(o3)
        t=tuple(options)
        prior2=max(t)
        prior3=min(t)
        options.remove(prior2)
        if prior2==prior3:
            print("+","Ectomorph",(o1/10)*100,"%",end=" ")
            print("+","Mesomorph",(o2/10)*100,"%")
        else:
            print("+",d[prior2],(prior2/10)*100,"%")
print("\n--------------Session Ended--------------")
print("\nWeight Loss tips:")
print("\n*Prioritize nutrient-dense foods.\n*Control portion sizes.\n*Incorporate regular physical activity.\n*Eliminate sugary drinks.\n*Stay hydrated.\n*Practice mindful eating.\n*Get enough sleep.\n*Manage stress.\n*Consider intermittent fasting.\n*Consult with a healthcare professional.\n")
print("Weight Gain tips:")
print("\n*Eat More Often.\n*Increase Calories.\n*Add Protein.\n*Healthy Carbs.\n*Healthy Fats.\n*Larger Portion.\n*Strength Training.\n*Stay Hydrated.\n*Sleep Well.\n*Track Progress.")
print("\n")
print("--------Thank You :),Feel free to post your queries. Subscribe to us for fresh updates------")